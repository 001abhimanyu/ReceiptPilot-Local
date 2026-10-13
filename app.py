import io
import json
import re
import requests
import pandas as pd
import streamlit as st
from pypdf import PdfReader

st.set_page_config(page_title="ReceiptPilot Local", page_icon="🧾", layout="wide")
st.title("🧾 ReceiptPilot Local")
st.caption("Private AI-powered invoice and receipt organizer")

with st.sidebar:
    st.header("Local AI settings")
    endpoint = st.text_input("Ollama endpoint", "http://localhost:11434")
    model = st.text_input("AI model", "llama3.2")
    st.divider()
    st.write("For local processing, keep the endpoint on localhost.")

if "records" not in st.session_state:
    st.session_state.records = []

def extract_text(uploaded_file):
    filename = uploaded_file.name.lower()
    content = uploaded_file.getvalue()
    if filename.endswith(".pdf"):
        reader = PdfReader(io.BytesIO(content))
        return "\n".join(page.extract_text() or "" for page in reader.pages).strip()
    if filename.endswith((".txt", ".md", ".csv")):
        return content.decode("utf-8", errors="ignore").strip()
    if filename.endswith((".png", ".jpg", ".jpeg", ".tiff", ".bmp")):
        from PIL import Image
        import pytesseract
        return pytesseract.image_to_string(Image.open(io.BytesIO(content))).strip()
    raise ValueError("Unsupported file format.")

def extract_invoice_fields(text, endpoint, model):
    prompt = f"""
Extract invoice or receipt data. Return only valid JSON with keys:
vendor, document_type, invoice_number, document_date, due_date,
currency, subtotal, tax, total, category, payment_status, notes.
Use null for missing values; never invent data. Amounts should be numbers.
category: Software, Travel, Meals, Office Supplies, Utilities,
Marketing, Professional Services, Equipment, Other.
payment_status: Paid, Unpaid, Unknown.
DOCUMENT TEXT:
{text[:18000]}
"""
    response = requests.post(
        endpoint.rstrip("/") + "/api/generate",
        json={"model": model, "prompt": prompt, "stream": False, "format": "json"},
        timeout=180,
    )
    response.raise_for_status()
    result = response.json().get("response", "")
    try:
        return json.loads(result)
    except json.JSONDecodeError:
        match = re.search(r"\{.*\}", result, re.S)
        if not match:
            raise ValueError("AI did not return valid JSON. Try again.")
        return json.loads(match.group(0))

st.subheader("Upload invoices and receipts")
uploaded_files = st.file_uploader(
    "Choose documents",
    type=["pdf", "txt", "md", "csv", "png", "jpg", "jpeg", "tiff", "bmp"],
    accept_multiple_files=True,
)

if uploaded_files:
    for index, uploaded_file in enumerate(uploaded_files):
        with st.expander(f"📄 {uploaded_file.name}", expanded=True):
            st.write(f"File size: {len(uploaded_file.getvalue()) / 1024:.1f} KB")
            if st.button("Extract invoice details", key=f"extract_{index}_{uploaded_file.name}"):
                try:
                    with st.spinner("Reading document..."):
                        text = extract_text(uploaded_file)
                    if not text:
                        st.error("No text found. Scanned PDFs may need OCR preprocessing.")
                        continue
                    with st.spinner(f"Analyzing with {model}..."):
                        fields = extract_invoice_fields(text, endpoint, model)
                    fields["source_file"] = uploaded_file.name
                    st.session_state.records = [
                        r for r in st.session_state.records
                        if r.get("source_file") != uploaded_file.name
                    ] + [fields]
                    st.success("Extraction completed. Review the fields below.")
                except requests.exceptions.ConnectionError:
                    st.error("Cannot connect to Ollama. Make sure Ollama is installed and running.")
                except requests.exceptions.HTTPError as error:
                    st.error(f"Ollama API error: {error}")
                except Exception as error:
                    st.error(f"Processing failed: {error}")

if st.session_state.records:
    st.divider()
    st.subheader("Extracted invoice records")
    st.warning("AI can make mistakes. Verify amounts and dates before using these records.")
    dataframe = pd.DataFrame(st.session_state.records)
    edited = st.data_editor(dataframe, num_rows="dynamic", use_container_width=True, key="invoice_editor")
    st.session_state.records = edited.fillna("").to_dict(orient="records")
    col1, col2 = st.columns(2)
    with col1:
        st.download_button(
            "Download CSV",
            data=edited.to_csv(index=False).encode("utf-8-sig"),
            file_name="receiptpilot-expenses.csv",
            mime="text/csv",
            use_container_width=True,
        )
    with col2:
        st.download_button(
            "Download JSON",
            data=json.dumps(st.session_state.records, indent=2, ensure_ascii=False),
            file_name="receiptpilot-expenses.json",
            mime="application/json",
            use_container_width=True,
        )
    if st.button("Clear all records"):
        st.session_state.records = []
        st.rerun()

st.divider()
st.caption("ReceiptPilot Local | Open-weight AI | Verify extracted financial information.")
