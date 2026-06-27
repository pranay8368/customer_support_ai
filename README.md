# AI-Powered Customer Support Automation System

An Agentic AI application built using **LangGraph** that automates customer support by classifying customer queries, routing them to specialized department agents, retrieving relevant information from company documents using **Retrieval-Augmented Generation (RAG)**, storing previous conversations using **SQLite Memory**, and requesting **Human-in-the-Loop Approval** for sensitive operations before generating the final response.

This project was developed as part of the **IBM Agentic AI Course Assignment**.

---

# Features

* Automatic Intent Classification
* Conditional Agent Routing using LangGraph
* Retrieval-Augmented Generation (RAG)
* FAISS Vector Store for Semantic Search
* HuggingFace Embeddings (all-MiniLM-L6-v2)
* SQLite Conversation Memory
* Memory Recall for Previous Customer Interactions
* Human-in-the-Loop Approval
* Supervisor Review before Final Response
* Modular LangGraph Workflow

---

# Tech Stack

* Python 3.x
* LangGraph
* LangChain
* Groq API (Llama 3.x)
* FAISS
* HuggingFace Embeddings (`sentence-transformers/all-MiniLM-L6-v2`)
* SQLite
* Python-dotenv

---

# Project Structure

```text
AI-Customer-Support-System/

│── knowledge_base/
│   ├── company_policy.txt
│   ├── pricing_guide.txt
│   ├── technical_manual.txt
│   └── faq.txt
│
├── agents.py
├── graph.py
├── main.py
├── memory.py
├── rag.py
├── state.py
├── requirements.txt
├── README.md
├── Documentation_Report.md
├── workflow_diagram.png
├── screenshots.pdf
├── memory.db
├── .gitignore
└── .env (Local Only - Not Uploaded)
```

---

# Installation

## 1. Clone the Repository

```bash
git clone https://github.com/pranay8368/customer_support_ai.git
cd CUSTOMER_SUPPORT
```

---

## 2. Create a Virtual Environment

```bash
python -m venv venv
```

### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Configure Environment Variables

Create a file named `.env` in the project root directory.

Add your Groq API key.

```env
GROQ_API_KEY=your_groq_api_key_here
```

> **Important:** Never upload your `.env` file or API key to GitHub.

---

# Running the Project

Run the application using:

```bash
python main.py
```

The application processes sample customer support queries through the complete LangGraph workflow.

For sensitive requests such as refunds, cancellations, or account closures, the system pauses and requests human approval.

Example:

```text
Approve this response? (yes/no):
```

Enter **yes** or **no** to continue.

---

# Workflow

1. Customer submits a query.
2. Intent Classification identifies the customer request.
3. LangGraph routes the request to the appropriate department agent.
4. Relevant company information is retrieved using RAG.
5. Previous customer conversations are retrieved from SQLite Memory.
6. Sensitive requests require Human-in-the-Loop approval.
7. Supervisor Agent reviews the generated response.
8. Final response is returned to the customer.
9. Conversation is stored in SQLite for future memory recall.

---

# Sample Queries

| Customer Query                                | Department                        |
| --------------------------------------------- | --------------------------------- |
| What are your pricing plans?                  | Sales                             |
| I forgot my account password.                 | Account Support                   |
| My application crashes while uploading files. | Technical Support                 |
| I need a refund for my annual subscription.   | Billing (Human Approval Required) |
| What was my previous support issue?           | Memory Recall                     |

---

# Project Components

The project demonstrates the following Agentic AI capabilities:

* Intent Classification
* Conditional Routing
* Retrieval-Augmented Generation (RAG)
* FAISS Similarity Search
* Conversation Memory
* Memory Recall
* Human-in-the-Loop Approval
* Supervisor Review
* Final Response Generation

---

# Submission Contents

This repository includes:

* Complete Source Code
* README.md
* Documentation_Report.md
* Workflow Diagram
* Screenshots PDF
* SQLite Memory Database (`memory.db`)
* Task Output Screenshots

---

# Future Improvements

* Web-based User Interface
* Multiple Language Support
* Customer Authentication
* Real-time Database Integration
* Voice-based Customer Support
* Analytics Dashboard
* Multi-Agent Collaboration

---

# Author

**Pranay**

IBM Agentic AI Course Assignment

VIT-AP University

May 2026 Batch

---
