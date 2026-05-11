# 🏥 Healthcare AI System using LangGraph & RAG

AI-powered Healthcare Application using OCR, LangGraph, RAG, FastAPI, and Streamlit.

---

# 🚀 Features

✅ OCR Text Extraction using Tesseract OCR  
✅ Medical Report Analysis  
✅ Disease Detection  
✅ RAG (Retrieval Augmented Generation)  
✅ AI-generated Medical Report  
✅ LangGraph Workflow  
✅ FastAPI Backend  
✅ Streamlit Frontend UI  
✅ ChromaDB Vector Database  
✅ Ollama / Groq LLM Support  

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

🏗️ Project Architecture

```
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

⚙️ Technologies Used
Python
LangGraph
LangChain
FastAPI
Streamlit
ChromaDB
Tesseract OCR
Ollama / Groq
Pillow


---
cd healthcare-ai-langgraph
🔹 Create Virtual Environment
Windows
python -m venv venv

venv\Scripts\activate
🔹 Install Dependencies
pip install -r requirements.txt
🔹 Install Tesseract OCR
---
Download and install:

https://github.com/UB-Mannheim/tesseract/wiki

IMPORTANT:
Enable:

Add Tesseract to PATH
🔹 Verify Installation
tesseract --version
▶️ Run FastAPI Backend
uvicorn app.main:app --reload
---
API Docs:

http://127.0.0.1:8000/docs
▶️ Run Streamlit UI

Open another terminal:

streamlit run streamlit_app.py

UI URL:

http://localhost:8501
---
🧪 Example Features

✅ Upload Medical Report
✅ OCR Text Extraction
✅ Detect Disease
✅ Generate AI Medical Summary
✅ Retrieve Medical Knowledge using RAG

---
📚 Example Diseases Supported
Pneumonia
Diabetes
Cancer
Urinary Tract Infection
Klebsiella Infection

🧠 LangGraph Workflow
OCR Agent
    ↓
Detection Agent
    ↓
RAG Agent
    ↓
Report Agent
📸 Sample Output
{
  "disease": "Klebsiella Infection",
  "rag_response": "Klebsiella infection is a bacterial infection caused by Klebsiella species.",
  "final_report": "Patient may have Klebsiella bacterial infection."
}

---
🌐 Future Improvements

✅ Multi-Agent AI
✅ Doctor AI Copilot
✅ X-ray Image Detection
✅ PDF Medical Reports
✅ Autonomous RAG
✅ PostgreSQL Integration
✅ Docker Deployment
✅ Cloud Deployment
✅ Voice AI Assistant

---


GitHub
👨‍💻 Author
Shubham Raut
