# multi-level-rag-hospital-assistant
Multi-Level RAG Hospital Assistant is an AI-powered question-answering system built with Python, LangChain, OpenAI, and ChromaDB. It uses department-specific knowledge bases and (RAG) to provide accurate, context-aware responses for hospital departments such as Reception, Billing, Insurance, Cardiology, Neurology, Pharmacy, and Emergency.


# 🏥 Multi-Level RAG Hospital Assistant

An AI-powered Hospital Assistant built using **Python**, **Flask**, **LangChain**, **OpenAI**, and **ChromaDB**. This project implements a **Multi-Level Retrieval-Augmented Generation (RAG)** architecture where each hospital department maintains its own vector database, enabling accurate, department-specific responses to user queries.

Unlike traditional chatbots that rely solely on an LLM's pre-trained knowledge, this application retrieves relevant information from dedicated department knowledge bases before generating responses. By combining semantic search with an OpenAI Large Language Model (LLM), the assistant delivers more accurate, reliable, and context-aware answers while reducing hallucinations.

This project demonstrates how modern RAG systems can be organized into multiple knowledge bases, making them scalable, maintainable, and suitable for real-world enterprise applications.

---

# 📖 Overview

The Multi-Level RAG Hospital Assistant is designed to simulate an intelligent hospital information system capable of answering user questions related to different hospital departments.

Instead of storing all hospital information in a single vector database, each department has its own dedicated knowledge base and ChromaDB vector database. When a user selects a department and submits a query, the application loads only the relevant vector database, performs semantic similarity search, retrieves the most relevant document chunks, and sends them as context to the OpenAI GPT-4o model for response generation.

This architecture significantly improves retrieval quality because unrelated documents from other departments are never included in the search process.

### Benefits of this Architecture

- ⚡ Faster document retrieval
- 🎯 More accurate responses
- 📂 Better organization of hospital knowledge
- 🔧 Easy maintenance and updates
- 📈 Highly scalable for adding new departments

---

# 🚀 Features

### 🧠 Multi-Level RAG Architecture

Implements a department-wise Retrieval-Augmented Generation pipeline where each hospital department has its own knowledge base and vector database.

### 📚 Department-wise Knowledge Bases

Each department stores its information independently, allowing the system to retrieve only relevant documents based on user selection.

### 🗂️ ChromaDB Vector Databases

All document chunks are converted into vector embeddings and stored inside separate ChromaDB databases for efficient semantic search.

### 🔢 OpenAI Embeddings

Uses **text-embedding-3-small** to convert document text into high-dimensional vector representations.

### 🤖 GPT-4o Response Generation

Uses OpenAI GPT-4o to generate natural language responses based on retrieved document context.

### 🔗 LangChain Integration

LangChain simplifies document loading, chunking, embedding generation, vector storage, prompt creation, and interaction with the LLM.

### 🌐 Flask Web Application

Provides an easy-to-use web interface where users can select departments and ask questions.

### 🔍 Semantic Search

Retrieves the most relevant document chunks using vector similarity rather than keyword matching.

### 💬 Context-Aware Responses

Answers are generated using retrieved context, improving reliability and reducing hallucinations.

### ➕ Easily Extendable

Adding a new hospital department requires only a new document and vector database without modifying the existing system.

---

# 🛠️ Technologies Used

| Technology | Purpose |
|------------|----------|
| **Python** | Core programming language used to develop the application. |
| **Flask** | Lightweight web framework used to build the user interface and backend routes. |
| **LangChain** | Framework used to build the Retrieval-Augmented Generation pipeline. |
| **OpenAI GPT-4o** | Large Language Model responsible for generating context-aware responses. |
| **OpenAI Embeddings** | Converts document text into vector embeddings for semantic retrieval. |
| **ChromaDB** | Vector database used to store and retrieve document embeddings efficiently. |
| **HTML** | Builds the frontend user interface. |
| **CSS** | Styles the web application to provide a clean and responsive design. |
| **python-dotenv** | Securely loads API keys and environment variables. |

---

# 🏥 Supported Hospital Departments

The application currently supports multiple hospital departments, each having its own document collection and ChromaDB vector database.

### 🏥 Reception

Provides information regarding appointments, registration procedures, visiting hours, hospital facilities, and patient guidance.

### 💳 Billing

Handles billing-related queries including payment methods, invoices, consultation fees, and payment procedures.

### 🛡️ Insurance

Provides details about supported insurance providers, claim procedures, required documentation, and reimbursement policies.

### ❤️ Cardiology

Contains information related to heart diseases, diagnostic procedures, treatments, specialist consultations, and cardiac care.

### 🧠 Neurology & Brain Tumor

Stores medical information regarding neurological disorders, brain tumor symptoms, diagnosis, treatments, and specialist recommendations.

### 💊 Pharmacy

Answers questions related to medicines, prescriptions, pharmacy timings, medication availability, and refill policies.

### 🚑 Emergency

Provides emergency contact information, ambulance services, emergency procedures, trauma care, and 24/7 emergency support.

---

# 🧠 System Architecture

The system follows a Retrieval-Augmented Generation workflow consisting of document loading, text chunking, embedding generation, vector storage, semantic retrieval, and response generation.

```text
Hospital Documents
        │
        ├── Reception
        ├── Billing
        ├── Insurance
        ├── Cardiology
        ├── Neurology
        ├── Pharmacy
        └── Emergency
                │
                ▼
        Document Loader
                │
                ▼
      Recursive Text Splitter
                │
                ▼
     OpenAI Embedding Model
                │
                ▼
 Department-wise ChromaDB
                │
───────────────────────────────────────
                │
         User Selects Department
                │
                ▼
          User Question
                │
                ▼
     Load Selected Vector Database
                │
                ▼
       Similarity Search
                │
                ▼
      Retrieve Relevant Chunks
                │
                ▼
        GPT-4o (OpenAI LLM)
                │
                ▼
        AI Generated Response
```

The modular architecture allows each department to remain independent, making future updates simple and scalable.

---

# 📂 Project Structure

The project is organized into separate folders for source code, department documents, vector databases, templates, and static assets.

```
multi-level-rag-hospital-assistant/

│── app.py
│── developer.py
│── requirements.txt
│── .env
│── README.md

├── data/
│      01_reception.txt
│      02_billing.txt
│      03_insurance.txt
│      04_cardiology.txt
│      05_neurology_brain_tumor.txt
│      06_pharmacy.txt
│      07_emergency.txt

├── db/
│      01_reception_database
│      02_billing_database
│      03_insurance_database
│      04_cardiology_database
│      05_neurology_database
│      06_pharmacy_database
│      07_emergency_database

├── templates/
│      index.html

├── static/
│      style.css

└── screenshots/
```

Each folder has a specific responsibility, keeping the application clean, modular, and easy to maintain.

---

# ⚙️ Installation

Follow these steps to set up the project on your local machine.

## Clone the Repository

```bash
git clone https://github.com/Gainaboina-Madhu/multi-level-rag-hospital-assistant.git
```

```bash
cd multi-level-rag-hospital-assistant
```

## Create a Virtual Environment

```bash
python -m venv .venv
```

Activate the environment:

**Windows**

```bash
.venv\Scripts\activate
```

**Linux/macOS**

```bash
source .venv/bin/activate
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🔑 Environment Variables

Create a `.env` file in the project root and add your OpenAI API key.

```env
OPEN_AI_KEY=your_openai_api_key
```

The application securely loads this key using the `python-dotenv` package to authenticate requests to the OpenAI API.

---

# ▶️ Run the Application

### Step 1: Create Vector Databases

Run the developer script to load the department documents, split them into chunks, generate embeddings, and store them in ChromaDB.

```bash
python developer.py
```

### Step 2: Start the Flask Application

```bash
python app.py
```

Open your browser and navigate to:


# 📸 Screenshots

Add screenshots here.

Example

# screenshots/home.png

<img width="1311" height="802" alt="image" src="https://github.com/user-attachments/assets/0e963b1b-495c-4db0-9e02-bcc2cab5ba41" />

# screenshots/question.png

<img width="1252" height="742" alt="image" src="https://github.com/user-attachments/assets/13a6d6f8-5d9d-4c78-bcf5-59fa5e1298c2" />


# screenshots/answer.png

<img width="1232" height="900" alt="image" src="https://github.com/user-attachments/assets/77d73be3-2d95-49a5-ad2c-1114a0938198" />




---

# 🎯 Future Improvements

- Multi-language Support
- Voice-based Interaction
- PDF Upload
- Chat History
- Authentication
- Doctor Recommendation System
- Appointment Booking
- Persistent Cloud Database
- Docker Deployment
- Render Deployment

---

```
http://127.0.0.1:5000
```

You can now select a department, enter a question, and receive an AI-generated response based on the department's knowledge base.
