# 🧾 ReceiptPilot Local
### Private AI-Powered Invoice & Receipt Organizer

![Reciptpilot]{Receiptpilot.png}

ReceiptPilot Local is an AI-powered application that helps freelancers and small businesses organize invoices and receipts. It uses an open-weight AI model running locally through Ollama to extract important financial information, categorize expenses, and export records to CSV or JSON.

The goal is to make bookkeeping easier, more affordable, and more privacy-friendly without depending on a hosted AI API.

## ✨ Features

- 📄 **Multiple file formats:** Upload PDF, TXT, MD, CSV, and image files.
- 🤖 **AI-powered extraction:** Identify vendor names, invoice numbers, dates, currencies, taxes, totals, and payment status.
- 🏷️ **Expense categorization:** Organize expenses into categories such as Software, Travel, Meals, Utilities, and Office Supplies.
- ✏️ **Editable results:** Review and correct extracted information before exporting.
- 📊 **CSV and JSON export:** Download organized financial records for further processing.
- 🔒 **Privacy-first processing:** Run AI locally using Ollama instead of sending documents to a hosted AI API.
- 🔧 **Flexible models:** Change the configured model to another compatible Ollama model.

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Application logic |
| Streamlit | Interactive web interface |
| Ollama | Local AI model runtime |
| Llama 3.2 | Default open-weight model |
| Pandas | Tabular data and CSV export |
| PyPDF | PDF text extraction |
| Pillow & Tesseract | Image processing and OCR |

## 📂 Project Structure

```text
receiptpilot-local/
├── app.py
├── requirements.txt
├── README.md
├── LICENSE
└── .gitignore
```

## ⚙️ Prerequisites

Before running the project, install:

1. [Python 3.10 or later](https://www.python.org/downloads/)
2. [Ollama](https://ollama.com/download)
3. An Ollama-compatible model, such as Llama 3.2
4. Tesseract OCR for image uploads

## 🚀 Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/receiptpilot-local.git
cd receiptpilot-local
```

Replace `YOUR-USERNAME` with your GitHub username and use the actual repository name.

### 2. Download the AI model

```bash
ollama pull llama3.2
```

Make sure Ollama is running and available at `http://localhost:11434`.

### 3. Create a virtual environment

**Windows PowerShell**

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
```

**Linux or macOS**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Run the application

```bash
streamlit run app.py
```

Open the local URL displayed in your terminal, usually:

```text
http://localhost:8501
```

## 📖 How to Use

1. Start the application.
2. Upload an invoice or receipt.
3. Click **Extract invoice details**.
4. Let the local AI model analyze the document.
5. Review and correct the extracted fields.
6. Export the results as CSV or JSON.

**Important:** AI-generated information may be inaccurate. Always verify dates, totals, tax amounts, and other financial details.

## 🔐 Privacy and Security

ReceiptPilot Local is designed for local-first processing.

- The default configuration sends document text to the local Ollama endpoint.
- No hosted AI API key is required for the default workflow.
- If you configure a remote Ollama endpoint, document text will be sent to that server.
- Avoid exposing Ollama directly to the public internet.
- Keep original financial documents and verify extracted information before using it for accounting or tax purposes.

Local processing helps reduce external data exposure, but it does not by itself provide encryption at rest, user authentication, or secure backups.

## 🌱 Why Open-Source AI?

Open innovation makes ReceiptPilot Local more flexible and accessible.

- **Cost control:** Avoid per-request charges from hosted AI APIs.
- **Privacy:** Process sensitive documents on your own computer.
- **Model flexibility:** Experiment with different compatible models.
- **Customization:** Adapt extraction prompts and expense categories to different business needs.
- **Reduced vendor lock-in:** Export results in standard formats.

The actual cost depends on hardware, electricity, model choice, and maintenance.

## 🗺️ Future Improvements

- [ ] Duplicate receipt detection
- [ ] Monthly expense summaries and charts
- [ ] Improved OCR for scanned invoices
- [ ] Custom expense categories
- [ ] Encrypted local storage and backup
- [ ] Vendor-specific extraction rules
- [ ] Accounting software integrations
- [ ] Batch processing improvements

## 🤝 Contributing

Contributions, suggestions, and bug reports are welcome!

1. Fork the repository.
2. Create a feature branch.
3. Make your changes.
4. Test the application.
5. Open a pull request describing your improvements.

## 💼 Side Hustle Potential

ReceiptPilot Local explores a practical business opportunity for freelancers, independent consultants, and small businesses that need a simpler way to organize receipts.

Potential services include local installation, custom expense categories, workflow configuration, and business-specific exports. Commercial demand should be validated through real user testing.

## 📄 License

This project is distributed under the MIT License. See the [LICENSE](LICENSE) file for details.

Check the applicable license and terms of the selected AI model before redistributing or using it commercially.

## 👨‍💻 Author

**Abhimanyu Sharma**

Built to explore practical applications of open-weight AI, privacy-first software, and automation.

---

⭐ If you find this project useful, consider giving the repository a star and sharing your feedback!

**Tags:** `Open-Source-AI` `Ollama` `Python` `Streamlit` `Invoice-Management` `Receipt-Scanner` `Privacy-First-AI` `Freelancer-Tools`
