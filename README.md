# 🏥 Healthcare AI System using LangGraph & RAG

AI-powered Healthcare Application for Medical Report Analysis using OCR, LangGraph, RAG, FastAPI, and Streamlit.

---

# 🚀 Features

* ✅ OCR Text Extraction using Tesseract OCR
* ✅ Medical Report Analysis
* ✅ Disease Detection
* ✅ Retrieval-Augmented Generation (RAG)
* ✅ AI-generated Medical Summary Report
* ✅ LangGraph Workflow Orchestration
* ✅ FastAPI Backend API
* ✅ Streamlit Interactive UI
* ✅ ChromaDB Vector Database
* ✅ Ollama / Groq LLM Support

---

# 🧠 AI Workflow

```text
Medical Report Image
        ↓
OCR Extraction
        ↓
Disease Detection Agent
        ↓
RAG Retrieval
        ↓
LLM Analysis
        ↓
Final AI Medical Report
```

---

# 🏗️ Project Architecture

```text
healthcare_ai/
│
├── app/
│   ├── agents/
│   │   ├── ocr_agent.py
│   │   ├── detection_agent.py
│   │   ├── rag_agent.py
│   │   └── report_agent.py
│   │
│   ├── graph/
│   │   └── graph_builder.py
│   │
│   ├── rag/
│   │   ├── chroma_db.py
│   │   └── medical_data.txt
│   │
│   ├── uploads/
│   │
│   └── main.py
│
├── streamlit_app.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

# ⚙️ Technologies Used

* Python
* LangGraph
* LangChain
* FastAPI
* Streamlit
* ChromaDB
* Tesseract OCR
* Ollama / Groq
* Pillow

---

# 📦 Installation

## 1️⃣ Clone Repository

```bash
git clone https://github.com/yourusername/healthcare-ai-langgraph.git

cd healthcare-ai-langgraph
```

---

## 2️⃣ Create Virtual Environment

### Windows

```bash
python -m venv venv

venv\Scripts\activate
```

---

## 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4️⃣ Install Tesseract OCR

Download and install:

https://github.com/UB-Mannheim/tesseract/wiki

### IMPORTANT

Enable the following option during installation:

```text
Add Tesseract to PATH
```

---

## 5️⃣ Verify Tesseract Installation

```bash
tesseract --version
```

---

# ▶️ Run FastAPI Backend

```bash
uvicorn app.main:app --reload
```

### API Documentation

```text
http://127.0.0.1:8000/docs
```

---

# ▶️ Run Streamlit Frontend

Open another terminal and run:

```bash
streamlit run streamlit_app.py
```

### Streamlit UI

```text
http://localhost:8501
```

---

# 🧪 Example Features

* ✅ Upload Medical Report Image
* ✅ OCR Text Extraction
* ✅ Disease Detection
* ✅ AI-generated Medical Summary
* ✅ Medical Knowledge Retrieval using RAG

---

# 📚 Example Diseases Supported

* Pneumonia
* Diabetes
* Cancer
* Urinary Tract Infection (UTI)
* Klebsiella Infection

---

# 🧠 LangGraph Workflow

```text
OCR Agent
    ↓
Detection Agent
    ↓
RAG Agent
    ↓
Report Agent
```

---

# 📸 Example Output

```json
{
  "disease": "Klebsiella Infection",
  "rag_response": "Klebsiella infection is a bacterial infection caused by Klebsiella species.",
  "final_report": "Patient may have Klebsiella bacterial infection."
}
```

---

# 🌐 Future Improvements

* ✅ Multi-Agent AI
* ✅ Doctor AI Copilot
* ✅ X-ray Image Detection
* ✅ PDF Medical Reports
* ✅ Autonomous RAG
* ✅ PostgreSQL Integration
* ✅ Docker Deployment
* ✅ Cloud Deployment
* ✅ Voice AI Assistant

---

# ☁️ Deployment

## Frontend

* Streamlit Cloud

## Backend

* Render

## Repository Hosting

* GitHub

---

# 👨‍💻 Author

Shubham Raut

* LinkedIn: https://www.linkedin.com/in/shubham-raut-37682b23a/

---

# 📄 License

This project is for educational and research purposes only.
