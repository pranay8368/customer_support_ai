# Documentation Report

# AI-Powered Customer Support Automation System

Course: IBM Agentic AI – VIT May 2026 Batch
Author: Pranay

---

# 1. Project Overview

ABC Technologies receives a large number of customer support requests every day related to product information, technical issues, billing, account management, and refund requests. Handling these requests manually increases response time and operational costs.

This project implements an **AI-Powered Customer Support Automation System** using **LangGraph** to automate the customer support workflow. The system classifies customer queries, retrieves relevant information from company documents using Retrieval-Augmented Generation (RAG), remembers previous customer interactions using SQLite memory, routes requests to specialized department agents, and requests human approval for sensitive operations before generating the final response.

---

# 2. System Architecture

The system is implemented as a LangGraph workflow consisting of multiple interconnected nodes.

## 1. Intent Classification

The customer's query is analyzed and classified into one of the following departments:

* Sales
* Technical Support
* Billing
* Account Management

---

## 2. RAG Retrieval

Relevant company documents are searched using a Retrieval-Augmented Generation (RAG) pipeline to provide accurate contextual information for the response.

---

## 3. Memory Lookup

The workflow retrieves previous customer conversations stored in a SQLite database, allowing the system to maintain context across multiple interactions.

---

## 4. Department Agent (Conditional Routing)

Depending on the classified intent, the request is routed to one of the specialized agents:

* Sales Agent
* Technical Support Agent
* Billing Agent
* Account Agent

Each department agent generates an initial response using the retrieved documents and previous conversation history.

---

## 5. Human-in-the-Loop Approval

Sensitive requests such as:

* Refunds
* Subscription Cancellations
* Account Closures
* Compensation Requests
* Escalations

require manual approval before the response is sent to the customer.

---

## 6. Supervisor Review

A supervisor agent performs a final quality review to improve clarity, professionalism, and completeness before returning the response.

---

## 7. Memory Storage

After the final response is generated, the customer's interaction is stored in SQLite for future memory recall.

---

# 3. State Design

The workflow uses a shared **SupportState (TypedDict)** that is passed through every LangGraph node.

The state contains the following fields:

* `customer_name`
* `query`
* `intent`
* `retrieved_context`
* `memory_context`
* `draft_response`
* `needs_approval`
* `approval_status`
* `final_response`

Each workflow node updates only the information it is responsible for, making the architecture modular, reusable, and easy to maintain.

---

# 4. RAG Implementation

The Retrieval-Augmented Generation (RAG) pipeline loads all text documents from the **knowledge_base** folder, including:

* company_policy.txt
* pricing_guide.txt
* technical_manual.txt
* faq.txt

The documents are loaded using **TextLoader** and divided into overlapping chunks using **RecursiveCharacterTextSplitter** with a chunk size of **500 characters** and an overlap of **50 characters**.

Each chunk is converted into vector embeddings using the **sentence-transformers/all-MiniLM-L6-v2** embedding model provided by HuggingFace.

The embeddings are stored in a **FAISS vector store**, which enables efficient similarity search. Whenever a customer submits a query, the system retrieves the top three most relevant document chunks and supplies them as context to the language model, enabling accurate and context-aware responses.

---

# 5. Memory Implementation

Conversation history is stored in a local SQLite database named **memory.db**.

Each interaction stores:

* Customer Name
* Customer Query
* Classified Intent
* Generated Response
* Timestamp

When a customer submits another query, the workflow retrieves previous interactions and includes them as context for the department agent.

This enables the system to answer follow-up questions such as:

> "What was my previous support issue?"

while maintaining continuity across conversations.

---

# 6. Human-in-the-Loop Design

The system detects sensitive customer requests using a keyword-based approval mechanism.

Keywords include:

* refund
* cancel
* compensation
* escalate
* account closure

When one of these keywords is detected, the workflow pauses and requests approval from a human supervisor through terminal input.

If the supervisor approves the response, the workflow continues normally.

If rejected, the generated response is replaced with an appropriate review message before being returned to the customer.

---

# 7. Testing and Demonstration

The application was tested using the five sample customer support queries provided in the assignment.

| Customer Query                                | Expected Routing         | Result                                            |
| --------------------------------------------- | ------------------------ | ------------------------------------------------- |
| What are your pricing plans available?        | Sales                    | Successfully routed to Sales Agent                |
| I forgot my account password.                 | Account                  | Successfully routed to Account Agent              |
| My application crashes while uploading files. | Technical Support        | Successfully routed to Technical Support Agent    |
| I need a refund for my annual subscription.   | Billing + Human Approval | Successfully triggered Human-in-the-Loop approval |
| What was my previous support issue?           | Memory Recall            | Successfully retrieved previous conversation      |

The workflow successfully demonstrated:

* Intent Classification
* Conditional Agent Routing
* Retrieval-Augmented Generation (RAG)
* FAISS Similarity Search
* SQLite Memory Storage
* Memory Recall
* Human-in-the-Loop Approval
* Supervisor Review
* Final Response Generation

---

# 8. Technology Stack

* Python 3.x
* LangGraph
* LangChain
* Groq API (Llama 3.x)
* FAISS Vector Store
* HuggingFace Embeddings (`sentence-transformers/all-MiniLM-L6-v2`)
* SQLite
* Python-dotenv

---

# 9. Conclusion

This project demonstrates a complete Agentic AI workflow for intelligent customer support automation.

The system combines LangGraph workflow orchestration, Retrieval-Augmented Generation (RAG), conversation memory, conditional routing, Human-in-the-Loop approval, and supervisor review to generate accurate, context-aware, and reliable customer support responses.

The modular architecture makes the project easy to extend with additional department agents, new knowledge base documents, advanced approval policies, or integration with web applications and enterprise customer support platforms.

Overall, the project satisfies the requirements of the IBM Agentic AI assignment while demonstrating practical applications of multi-agent workflows, RAG, persistent memory, and human oversight in AI-powered customer support systems.

---

# Author

Pranay

IBM Agentic AI Course Assignment

VIT-AP University

May 2026 Batch
