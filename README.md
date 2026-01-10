# 🛒 Agentic AI | GenAI RAG Product Recommender

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://universal-pdf-rag-chatbot-mhsi4ygebe6hmq3ij6d665.streamlit.app/)
[![Python 3.9+](https://img.shields.io/badge/python-3.9%2B-blue.svg)](https://www.python.org/downloads/release/python-390/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=flat&logo=docker&logoColor=white)](https://www.docker.com/)
[![Kubernetes](https://img.shields.io/badge/kubernetes-%23326ce5.svg?style=flat&logo=kubernetes&logoColor=white)](https://kubernetes.io/)

<img width="940" height="499" alt="image" src="https://github.com/user-attachments/assets/b987b30f-0683-4ffc-96a8-ec48a180d4da" />

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

```mermaid
graph TD
    User([User]) -->|Interacts| UI[Streamlit UI]
    subgraph "Application Layer"
        UI -->|HTTP Request| API[Flask Backend]
        API -->|Orchestrate| Chain[LangChain RAG]
    end
    subgraph "Data & AI Layer"
        Chain -->|Retrieve| VDB[(AstraDB)]
        Chain -->|Generate| LLM[Groq Llama 3]
        HF[HuggingFace] -->|Embed| VDB
    end
    subgraph "Infrastructure & Observability"
        Docker[[Docker Container]]
        K8s{Kubernetes Cluster}
        Prometheus((Prometheus))
        Grafana[Grafana Dashboards]
    end
    K8s -.-> Docker
    Prometheus -.->|Monitor| API
    Grafana -.->|Visualize| Prometheus
```

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
## 🌐🎬 Live Demo
🚀 **Try it now:**
- **Streamlit Profile** - https://share.streamlit.io/user/ratnesh-181998
- **Project Demo** - https://flipkart-appuct-recommender-rag-qpisu9s2oo4dyjr3fpp4yf.streamlit.app/
  
---

### 🎬 Live Project Demo
> Experience the full flow:

![Project Demo Walkthrough](Combined_Walkthrough.gif)

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
<img width="1913" height="833" alt="image" src="https://github.com/user-attachments/assets/753004b2-c2fd-4c03-b9ac-f4f1e23a5c15" />
<img width="1903" height="827" alt="image" src="https://github.com/user-attachments/assets/4a1fd530-7c79-473d-a97e-e530962cc290" />
<img width="1896" height="812" alt="image" src="https://github.com/user-attachments/assets/d2126e6d-b39e-412d-b753-bebdbd8d97c7" />
<img width="1909" height="837" alt="image" src="https://github.com/user-attachments/assets/6e0fe089-c674-4258-96d1-fe7a2adeeef6" />
<img width="1898" height="834" alt="image" src="https://github.com/user-attachments/assets/20849c60-6884-473a-9fca-af275037f687" />
<img width="1865" height="815" alt="image" src="https://github.com/user-attachments/assets/aa270177-b811-4b88-b4e5-7cdaf1e2af80" />
<img width="1897" height="793" alt="image" src="https://github.com/user-attachments/assets/28954617-902a-4be6-a79f-401d9798b291" />


### 2️⃣ 📖 About Project Tab
Context and Education.
- Explains the **Problem Statement** (limitations of keyword search) and the **GenAI Solution**.
<img width="1894" height="797" alt="image" src="https://github.com/user-attachments/assets/225eb011-96cd-4004-b1cc-8d857bf2c886" />
<img width="1863" height="791" alt="image" src="https://github.com/user-attachments/assets/46b42be4-d786-4dba-8dd1-61cf926a4160" />
<img width="1590" height="747" alt="image" src="https://github.com/user-attachments/assets/4bc5d253-87de-44cd-be61-915b57e84695" />
<img width="1576" height="751" alt="image" src="https://github.com/user-attachments/assets/1bde9437-642e-4920-a3c8-4ffbbd779127" />
<img width="1814" height="760" alt="image" src="https://github.com/user-attachments/assets/16c3b413-626f-4b6c-a5b4-8fabd450e059" />
<img width="1575" height="740" alt="image" src="https://github.com/user-attachments/assets/eb063480-b865-4cb5-bc81-691fe32532a1" />
<img width="1581" height="758" alt="image" src="https://github.com/user-attachments/assets/75275ceb-75b1-4595-89e5-a6b37e27010e" />

### 3️⃣ 🔧 Tech Stack Tab
Transparency.
- Visually displays the technologies used, building trust in the system's robustness.
<img width="1882" height="813" alt="image" src="https://github.com/user-attachments/assets/d3c89d56-bb46-4fb4-a9ed-4d315ffecf42" />
<img width="1892" height="802" alt="image" src="https://github.com/user-attachments/assets/db6f6f48-bced-4473-93e2-072e4be05705" />
<img width="1865" height="787" alt="image" src="https://github.com/user-attachments/assets/b54bbbe0-31dc-46d4-ba81-441ce5de199d" />
<img width="1897" height="778" alt="image" src="https://github.com/user-attachments/assets/26cfee24-2289-4e49-9492-2bb86ec8d545" />
<img width="1891" height="765" alt="image" src="https://github.com/user-attachments/assets/d44bd035-7f06-4e84-8dc2-64013301e9a9" />

### 4️⃣ 🏗️ Architecture Tab
System Design.
- Interactive diagrams allowing users to explore the data flow and infrastructure.
<img width="1877" height="816" alt="image" src="https://github.com/user-attachments/assets/244f4cf0-2592-41c2-9a0a-ec0f91f0e30a" />
<img width="1586" height="747" alt="image" src="https://github.com/user-attachments/assets/a87de07f-93aa-4d62-bc0b-b82c4af22ca1" />
<img width="1591" height="767" alt="image" src="https://github.com/user-attachments/assets/f3a2667b-97a7-4122-a589-b0826845682c" />
<img width="1575" height="785" alt="image" src="https://github.com/user-attachments/assets/b7e6d756-2e2d-4bc3-930a-d8dfca2b7813" />
<img width="1550" height="755" alt="image" src="https://github.com/user-attachments/assets/479b06ee-f052-417d-9595-bdf7a10e4bd3" />
<img width="1563" height="759" alt="image" src="https://github.com/user-attachments/assets/df6bf670-9cdf-493c-b29c-3e0f9c0a48ae" />
<img width="1606" height="762" alt="image" src="https://github.com/user-attachments/assets/5e76dc29-86f1-4de7-adc2-a132f35aea4f" />

### 5️⃣ 📋 System Logs Tab
Observability for Developers.
- Real-time stream of application logs (Info, Warning, Error).
- Health check status for API, Database, and LLM connections.
<img width="1798" height="762" alt="image" src="https://github.com/user-attachments/assets/4bc58423-79fd-4dc9-b5ea-c8c6a580da92" />
<img width="1478" height="714" alt="image" src="https://github.com/user-attachments/assets/73d20ed0-1814-498b-b5ad-31066476ef4c" />
<img width="1526" height="647" alt="image" src="https://github.com/user-attachments/assets/68abf806-998f-4b51-a397-8b4a5673f909" />
<img width="1529" height="654" alt="image" src="https://github.com/user-attachments/assets/bcdb98f1-66cb-40ca-bfe2-ab5f40675ad5" />

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
### Project Links

- 🌐 **Live Demo**: [Streamlit App](https://flipkart-appuct-recommender-rag-qpisu9s2oo4dyjr3fpp4yf.streamlit.app/)
- 📖 **Documentation**: [GitHub Wiki](https://github.com/Ratnesh-181998/Flipkart-Product-Recommender-RAG/wiki)
- 🐛 **Issue Tracker**: [GitHub Issues](https://github.com/Ratnesh-181998/Flipkart-Product-Recommender-RAG/issues)
- 💬 **Discussions**: [GitHub Discussions](https://github.com/Ratnesh-181998/Flipkart-Product-Recommender-RAG/discussions)
---
## 📄 License & Contact

**License**: Distributed under the MIT License.

**Author**: **RATNESH KUMAR SINGH**  
*Data Scientist (AI/ML)*  
- 📧 [Email](mailto:rattudacsit2021gate@gmail.com) | 💼 [LinkedIn](https://www.linkedin.com/in/ratneshkumar1998/) | 🐙 [GitHub](https://github.com/Ratnesh-181998)

  ---
*Built with passion for the AI Community. 🚀*

</div>

---

---


<img src="https://capsule-render.vercel.app/api?type=rect&color=gradient&customColorList=24,20,12,6&height=3" width="100%">


## 📜 **License**

![License](https://img.shields.io/badge/License-MIT-success?style=for-the-badge&logo=opensourceinitiative&logoColor=white)

**Licensed under the MIT License** - Feel free to fork and build upon this innovation! 🚀

---

# 📞 **CONTACT & NETWORKING** 📞


### 💼 Professional Networks

[![LinkedIn](https://img.shields.io/badge/💼_LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/ratneshkumar1998/)
[![GitHub](https://img.shields.io/badge/🐙_GitHub-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Ratnesh-181998)
[![X](https://img.shields.io/badge/X-000000?style=for-the-badge&logo=x&logoColor=white)](https://x.com/RatneshS16497)
[![Portfolio](https://img.shields.io/badge/🌐_Portfolio-FF6B6B?style=for-the-badge&logo=google-chrome&logoColor=white)](https://share.streamlit.io/user/ratnesh-181998)
[![Email](https://img.shields.io/badge/✉️_Email-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:rattudacsit2021gate@gmail.com)
[![Medium](https://img.shields.io/badge/Medium-000000?style=for-the-badge&logo=medium&logoColor=white)](https://medium.com/@rattudacsit2021gate)
[![Stack Overflow](https://img.shields.io/badge/Stack_Overflow-F58025?style=for-the-badge&logo=stack-overflow&logoColor=white)](https://stackoverflow.com/users/32068937/ratnesh-kumar)

### 🚀 AI/ML & Data Science
[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://share.streamlit.io/user/ratnesh-181998)
[![HuggingFace](https://img.shields.io/badge/HuggingFace-FFD21E?style=for-the-badge&logo=huggingface&logoColor=black)](https://huggingface.co/RattuDa98)
[![Kaggle](https://img.shields.io/badge/Kaggle-20BEFF?style=for-the-badge&logo=kaggle&logoColor=white)](https://www.kaggle.com/rattuda)

### 💻 Competitive Programming
[![LeetCode](https://img.shields.io/badge/LeetCode-FFA116?style=for-the-badge&logo=leetcode&logoColor=black)](https://leetcode.com/u/Ratnesh_1998/)
[![HackerRank](https://img.shields.io/badge/HackerRank-00EA64?style=for-the-badge&logo=hackerrank&logoColor=black)](https://www.hackerrank.com/profile/rattudacsit20211)
[![CodeChef](https://img.shields.io/badge/CodeChef-5B4638?style=for-the-badge&logo=codechef&logoColor=white)](https://www.codechef.com/users/ratnesh_181998)
[![Codeforces](https://img.shields.io/badge/Codeforces-1F8ACB?style=for-the-badge&logo=codeforces&logoColor=white)](https://codeforces.com/profile/Ratnesh_181998)
[![GeeksforGeeks](https://img.shields.io/badge/GeeksforGeeks-2F8D46?style=for-the-badge&logo=geeksforgeeks&logoColor=white)](https://www.geeksforgeeks.org/profile/ratnesh1998)
[![HackerEarth](https://img.shields.io/badge/HackerEarth-323754?style=for-the-badge&logo=hackerearth&logoColor=white)](https://www.hackerearth.com/@ratnesh138/)
[![InterviewBit](https://img.shields.io/badge/InterviewBit-4285F4?style=for-the-badge&logo=google&logoColor=white)](https://www.interviewbit.com/profile/rattudacsit2021gate_d9a25bc44230/)


---

## 📊 **GitHub Stats & Metrics** 📊



![Profile Views](https://komarev.com/ghpvc/?username=Ratnesh-181998&color=blueviolet&style=for-the-badge&label=PROFILE+VIEWS)





<img src="https://github-readme-streak-stats.herokuapp.com/?user=Ratnesh-181998&theme=radical&hide_border=true&background=0D1117&stroke=4ECDC4&ring=F38181&fire=FF6B6B&currStreakLabel=4ECDC4" width="48%" />




<img src="https://github-readme-activity-graph.vercel.app/graph?username=Ratnesh-181998&theme=react-dark&hide_border=true&bg_color=0D1117&color=4ECDC4&line=F38181&point=FF6B6B" width="48%" />

---

<img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&size=24&duration=3000&pause=1000&color=4ECDC4&center=true&vCenter=true&width=600&lines=Ratnesh+Kumar+Singh;Data+Scientist+%7C+AI%2FML+Engineer;4%2B+Years+Building+Production+AI+Systems" alt="Typing SVG" />

<img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&size=18&duration=2000&pause=1000&color=F38181&center=true&vCenter=true&width=600&lines=Built+with+passion+for+the+AI+Community+🚀;Innovating+the+Future+of+AI+%26+ML;MLOps+%7C+LLMOps+%7C+AIOps+%7C+GenAI+%7C+AgenticAI+Excellence" alt="Footer Typing SVG" />


<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=6,11,20&height=120&section=footer" width="100%">




