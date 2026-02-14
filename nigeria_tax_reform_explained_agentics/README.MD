# TaxPyre Nigeria 🇳🇬

**Agentic RAG System for Public Policy Interpretation**

---

## 📋 Table of Contents
1. Executive Summary
2. Real-World Impact
3. Problem Statement
4. System Architecture
5. Key Technical Features
6. Design Decisions
7. Limitations
8. Technology Stack
9. High-level Architecture
10. Setup (Backend / Frontend)
11. Future Improvements
12. Team & Contribution

---

### 1. Executive Summary

TaxPyre Nigeria is an applied GenAI system designed to make complex Nigerian tax reform legislation (500+ pages across four bills) accessible to citizens, businesses, and policymakers.

The 2024 reforms fundamentally reshape Nigeria’s tax administration beginning in 2026, affecting over 200 million people. However, public access to clear, searchable, and verifiable explanations of these reforms remains limited.

TaxPyre addresses this gap using an agentic Retrieval-Augmented Generation (RAG) architecture that combines structured document ingestion, semantic retrieval, and citation-backed response generation. The system delivers grounded, plain-language explanations while preserving traceability to official legislative sources.

Unlike basic chatbot implementations, the system integrates:
    - Conditional document retrieval to optimize efficiency
    - Conversation memory for contextual follow-up reasoning
    - Section- and page-level source attribution
    - Misconception detection to counter widespread misinformation

This project demonstrates end-to-end AI system design across ingestion, retrieval, orchestration, and frontend integration; with emphasis on transparency, reliability, and real-world applicability.

---

### 2. Real-World Impact

The Nigerian tax reform bills introduce significant structural changes to income tax brackets, VAT allocation formulas, corporate tax exemptions, and revenue administration frameworks.

TaxPyre aims to:

    - Improve accessibility of 500+ pages of legal documentation
    - Reduce misinformation through source-backed responses
    - Enable SMEs and individuals to understand tax obligations through plain-language explanations
    - Support informed financial and policy decision-making
    - Demonstrate how agentic RAG systems can enhance public-sector information transparency in emerging markets

The project illustrates the practical application of GenAI systems for policy interpretation in high-impact governance environments.

---

### 3. Problem Statement

The reform legislation spans multiple interdependent bills, written in dense legal language and distributed primarily as static PDFs. Citizens and businesses face barriers including:

    - Cross-referenced legal structures
    - Non-searchable documents
    - Legal terminology inaccessible to non-specialists
    - Conflicting narratives across media channels

There was no system capable of delivering contextual, verifiable answers to specific tax-related questions.

TaxPyre bridges this gap by combining semantic retrieval with structured AI reasoning to translate legal content into grounded, interpretable insights.

---

### 4. System Architecture

TaxPyre implements a modular Agentic RAG pipeline:

    1. Document Ingestion Pipeline
        - PDF parsing with structural preservation
        - Intelligent chunking (1000 chars, 200 overlap)
        - Metadata tagging (bill, section, page)
        - Embedding generation using Sentence-Transformers
        - Storage in ChromaDB vector database

    2. Conditional Retrieval Engine
        - Determines when document search is required
        - Avoids unnecessary retrieval for general prompts
        - Reduces latency and token usage
    
    3. Conversation-Aware Agent
        - Maintains rolling conversation memory (10 turns)
        - Supports contextual follow-up reasoning
        - Enables multi-step dialogue
    
    4. Source-Backed Generation Layer
        - GPT-4 generates plain-language explanations
        - Mandatory citation of bill name, section, and page
        - Excerpt previews for verification
        
    5. Frontend Interface
        - React-based information portal
        - Integrated AI chat modal
        - Expandable source citations
        - Mobile-optimized design

---

### 5. Key Technical Features
    
    - Semantic search with vector embeddings (384-dim MiniLM)
    - Agentic workflow orchestration (LangGraph)
    - Conditional retrieval logi
    - Conversation memory management
    - Misconception detection patterns
    - Citation-backed transparency
    - End-to-end system integration (FastAPI + React)

---

### 6. Design Decisions

    - RAG over fine-tuning: Legislation evolves; retrieval allows dynamic updates without retraining.
    - MiniLM embeddings: Selected for performance-speed tradeoff.
    - Conditional retrieval: Reduces hallucination risk and improves efficiency.
    - Structured chunk overlap: Preserves semantic continuity across legal sections.
    - Mandatory citation enforcement: Increases trust and verifiability.

---

### 7. Limitations

    - No formal quantitative evaluation (e.g., faithfulness scoring or benchmarking)
    - Possible hallucination in ambiguous edge cases
    - English-only interface (future multilingual expansion planned)
    - No production deployment or authentication layer
    - Limited real-world user testing

---

### 8. Technology Stack

Backend:
Python 3.9+, FastAPI, LangChain, LangGraph, GPT-4, Sentence-Transformers, ChromaDB

Frontend:
React 18, Vite, Tailwind CSS

---

### 9. High-Level Architecture
React Frontend
      ↓
FastAPI Backend
      ↓
Agentic RAG Layer
      ↓
ChromaDB Vector Store
      ↓
OpenAI GPT-4

---

### 10. Setup

Backend
    cd backend
    python -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    python -m app.rag.ingestion
    python -m app.main

Frontend
    cd frontend
    npm install
    npm run dev

---

### 11. Future Improvements

    - Formal hallucination and faithfulness evaluation metrics
    - Multilingual expansion (Yoruba, Hausa, Igbo)
    - Production-grade deployment infrastructure
    - Automated legislative update monitoring
    - Enhanced LLM evaluation and benchmarking

---

### 12. Team & Contribution

TaxPyre was developed by a small cross-functional team. All AI system design and RAG architecture decisions were collaboratively developed between the AI engineering team. 

AI Engineering (Architecture & RAG System) 
    - Kanyisola Fagbayi
    - Blessing James

Frontend Development
    - Ruqayat Odeleye

Research & Documentation
    - All members of the team
