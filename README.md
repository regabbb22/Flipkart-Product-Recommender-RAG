# 🛒 GenAI RAG Product Recommender

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://universal-pdf-rag-chatbot-mhsi4ygebe6hmq3ij6d665.streamlit.app/)
[![Python 3.9+](https://img.shields.io/badge/python-3.9%2B-blue.svg)](https://www.python.org/downloads/release/python-390/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=flat&logo=docker&logoColor=white)](https://www.docker.com/)
[![Kubernetes](https://img.shields.io/badge/kubernetes-%23326ce5.svg?style=flat&logo=kubernetes&logoColor=white)](https://kubernetes.io/)

> **A Production-Grade E-commerce Recommendation System built with RAG Architecture, Groq Llama 3, LangChain, and AstraDB.** 
> *Deployed on Kubernetes with Prometheus/Grafana O11y.*

---

## 📑 Table of Contents

- [⚡ Executive Overview](#-executive-overview)
- [🏗️ System Architecture & Visuals](#-system-architecture--visuals)
- [🚀 Quick Links](#-quick-links)
- [🛠️ Technical Ecosystem](#-technical-ecosystem)
- [🔄 RAG Pipeline & Workflow](#-rag-pipeline--workflow)
- [📱 Key Features](#-key-features)
- [📂 Project Structure](#-project-structure)
- [🛠️ Installation & Setup](#-installation--setup)
- [🔮 Roadmap](#-roadmap)
- [📄 License & Contact](#-license--contact)

---

## ⚡ Executive Overview

The **Flipkart Product Recommender** is an intelligent conversational AI designed to revolutionize e-commerce discovery. Moving beyond traditional keyword search, it leverages **Retrieval-Augmented Generation (RAG)** to understand user intent deeply and semantically retrieve relevant product reviews from **AstraDB**, generating highly contextual responses using the ultra-fast **Groq Llama 3.1** engine.

This project showcases a complete **End-to-End LLMOps Pipeline**, featuring data ingestion, vector storage, RAG chain orchestration, a robust Flask backend, an interactive Streamlit UI, and cloud-native deployment on Kubernetes with full observability.

---

## 🏗️ System Architecture & Visuals

A high-level visual guide to the system's design, workflow, and monitoring capabilities.

### 🔹 High-Level Architecture
> *User → UI → Backend → LLM + Vector DB → Response → UI*

![Architecture](https://mermaid.ink/img/pako:eNqVVE1v2zAM_SuEzsmwG_0AHQosW4t22GGH7bCluyDwxEhsZcmQ6KSB4f8-SrZSx06bYQc_Pz-REiVfqaQVSk_sU_1EHzS9M6a6vK4UvTdWj-tO3zS3lX7R-v6h1nrdKq2UbnWrtV6pY6u1frp5uH1-vnl4fPiqnzQdNa3S-vH24etNfX93_1vfNvrxvn54rO9vH54e7mu9q5XWO91cf37SX9Sf3-qHe_2iH2_qXf10_7DeXdX64bHS-vGffvzhQf_Wqn-tX_W6U-Sjs_H1w8P93f1tvW5uPz1c_9Y-1_S19cM34wyIeQ-IowdEPwPiJCAuHhBdD4gzgLh5QHQ8IC4C4uYB0fGAuAuImwdExwPiISBuHhCeB8RjQDw8IDwPiKeAeHhAeB4QzwHx8IDwPCAeA-LhAeF5QDwHxEOGuE6QOEuQZAmSLEGSI_B_lCBxjiBxliDJEqQYggSHEOQAQY4Q5AhBjiDIIQQ5QJAjBDlCkCMIcghBDhDkCEGOEOQIgryHIO8hyHsI8h6C_C9CkBMEOUCQIwQ5QpAjCHIIMi8gyLyAIPMCgswLCPK-gCDzAoLMiwgyLyDIPIMg8wyCzDMIMs8gyDxDkOcM4jKDuMwgLjOIywziMgO5zEAwM5DLDAQzA7nMQC4zkMsMBDMDucxAMDMeT555PHnm8eSZx5NnHk-e-Q95FjFkMUNWMyT6N2S9Q9Z3ZF1H1nTkeUeeceRJR5ZvZHlHFncMeceQbwzpxpBpDFm-Ics3ZPmGLN-Q5RuCzCDIDILMIMgMguwgyA6C7CDIDoLsIMgBgswgyAyCzCDIDoJ8hyDfIci3CPIigrwin3nkM4985pHPvIh85pHPPIvIZx75zCOf_wFw0Y2H)

### 🔹 Comprehensive Workflow Integration
> *Detailed data flow from Ingestion to Generation.*
![Tech Stack Workflow](workflow_diagram.png)

### 🔹 LLMOps & Observability Dashboard
> *Real-time monitoring of System Health and Latency using Prometheus & Grafana.*
![Monitoring Dashboard](monitoring_diagram.png)

### 🔹 Technology Stack Overview
> *Full stack breakdown including AI, DevOps, and Backend components.*
![Tech Stack Banner](tech_stack_banner.png)

---

## 🚀 Quick Links

- 🌐 **Live Application:** [Launch Streamlit App](https://universal-pdf-rag-chatbot-mhsi4ygebe6hmq3ij6d665.streamlit.app/)
- 📖 **Documentation:** [View Wiki](https://github.com/Ratnesh-181998/Flipkart-Product-Recommender-RAG)
- 🐛 **Report Issues:** [Issue Tracker](https://github.com/Ratnesh-181998/Flipkart-Product-Recommender-RAG)
- 🐙 **Source Code:** [GitHub Repository](https://github.com/Ratnesh-181998/Flipkart-Product-Recommender-RAG)

---

## 🛠️ Technical Ecosystem

This project creates a robust synergy between modern AI frameworks and cloud-native infrastructure.

### 💻 Core Tech Stack
1.  **Groq**: Ultra-low latency LLM Inference Engine (LPU).
2.  **HuggingFace**: State-of-the-art Embedding Models.
3.  **LangChain**: Orchestration framework for RAG workflows.
4.  **AstraDB**: Serverless, high-performance Vector Database.
5.  **Flask**: Lightweight Backend API.
6.  **Streamlit**: Interactive Frontend UI.
7.  **Docker**: Containerization for consistent environments.
8.  **Kubernetes (Minikube)**: Container Orchestration & Scaling.
9.  **GCP VM**: Cloud Infrastructure host.
10. **Prometheus**: Metrics Collection & Monitoring.
11. **Grafana**: Data Visualization & Dashboards.
12. **GitHub**: Version Control & CI/CD.

### 🧠 Deep Dive: Core AI Layer

#### 1. Groq (LLM)
*   **Role**: The brain of the system.
*   **Why**: Selected for its **LPU (Language Processing Unit)** technology which delivers near-instant inference speeds, critical for real-time chat experiences.

#### 2. Hugging Face (Embeddings)
*   **Role**: The semantic translator.
*   **Function**: Converts raw text reviews into high-dimensional vectors, capturing the *meaning* behind the words for accurate retrieval.

#### 3. AstraDB (Vector Store)
*   **Role**: The knowledge base.
*   **Why**: A cloud-native, serverless vector store based on Cassandra. It offers scalability and zero-management overhead, perfect for handling large datasets of product reviews.

---

## 🔄 RAG Pipeline & Workflow

The system follows a precise logic flow to ensure accurate and grounded responses.

### Logic Flow
1.  **Ingestion**: Raw review data (CSV) is loaded and cleaned.
2.  **Chunking**: Text is split into semantic chunks using `RecursiveCharacterTextSplitter`.
3.  **Embedding**: Chunks are vectorized using `BAAI/bge-base-en-v1.5`.
4.  **Storage**: Vectors are stored in **AstraDB**.
5.  **Retrieval**: User queries are embedded; similarity search finds the top-k relevant contexts.
6.  **Generation**: **Groq** synthesizes the context and query into a helpful response.

### Pipeline Visualization
```mermaid
graph TD;
    Documents[Raw Data] --> Chunking;
    Chunking --> Embeddings_HF[HF Embeddings];
    Embeddings_HF --> Vector_Store_AstraDB[(AstraDB)];
    User_Query --> Embeddings_HF;
    Embeddings_HF --> Similarity_Search;
    Vector_Store_AstraDB --> Similarity_Search;
    Similarity_Search --> Context;
    Context --> LLM_Groq[Groq LLM];
    LLM_Groq --> Response;
```

---

## 📱 Key Features

### 1️⃣ 🎬 Live Demo Tab
The heart of the application.
- **ChatGPT-Style Interface**: Familiar and intuitive chat experience.
- **Dynamic Product Cards**: AI auto-generates structured product cards with images, prices, and links based on the conversation.

### 2️⃣ 📖 About Project Tab
Context and Education.
- Explains the **Problem Statement** (limitations of keyword search) and the **GenAI Solution**.

### 3️⃣ 🔧 Tech Stack Tab
Transparency.
- Visually displays the technologies used, building trust in the system's robustness.

### 4️⃣ 🏗️ Architecture Tab
System Design.
- Interactive diagrams allowing users to explore the data flow and infrastructure.

### 5️⃣ 📋 System Logs Tab
Observability for Developers.
- Real-time stream of application logs (Info, Warning, Error).
- Health check status for API, Database, and LLM connections.

---

## 📂 Project Structure

```plaintext
Flipkart-Product-Recommender-RAG/
├── .streamlit/          # Streamlit configuration
├── data/                # Raw dataset (CSV/JSON)
├── flipkart/            # Core application logic package
├── grafana/             # Grafana dashboard configurations
├── prometheus/          # Prometheus monitoring rules
├── static/              # CSS styles and images
├── templates/           # HTML templates for Flask
├── utils/               # Helper functions (logger, exceptions)
├── .env.example         # Template for environment variables
├── .gitignore           # Git ignore rules
├── Dockerfile           # Docker build configuration
├── LICENSE              # MIT License
├── README.md            # Project documentation
├── app.py               # Flask backend entry point
├── flask-deployment.yaml# Kubernetes deployment for Flask
├── requirements.txt     # Python dependencies
├── setup.py             # Package installation script
└── streamlit_app.py     # Streamlit frontend entry point
```

---

## 🛠️ Installation & Setup

Follow these steps to run the project locally.

### Prerequisites
- Python 3.9+
- Docker & Minikube (Optional, for K8s deployment)
- Git

### Quick Start
1.  **Clone the Repository**
    ```bash
    git clone https://github.com/Ratnesh-181998/Flipkart-Product-Recommender-RAG.git
    cd Flipkart-Product-Recommender-RAG
    ```

2.  **Environment Setup**
    ```bash
    python -m venv venv
    source venv/bin/activate  # Windows: venv\Scripts\activate
    pip install -r requirements.txt
    ```

3.  **Configuration**
    Create a `.env` file:
    ```env
    GROQ_API_KEY=your_key
    ASTRA_DB_TOKEN=your_token
    ASTRA_DB_API_ENDPOINT=your_endpoint
    ```

4.  **Run Application**
    ```bash
    streamlit run streamlit_app.py
    ```

---

## 🔮 Roadmap

- [ ] **CI/CD Pipeline**: GitHub Actions for automated testing.
- [ ] **User Authentication**: Persist chat history per user.
- [ ] **Voice Interaction**: Speech-to-Text integration.
- [ ] **Multi-Modal Output**: Image generation for product visualization.

---

## 📄 License & Contact

**License**: Distributed under the MIT License.

**Author**: **RATNESH KUMAR SINGH**  
*Data Scientist (AI/ML)*  
- 📧 [Email](mailto:rattudacsit2021gate@gmail.com) | 💼 [LinkedIn](https://www.linkedin.com/in/ratneshkumar1998/) | 🐙 [GitHub](https://github.com/Ratnesh-181998)
