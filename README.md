# AI-Powered Intelligent Candidate Discovery & Ranking System

An intelligent recruitment solution that helps recruiters discover and rank the most relevant candidates by combining semantic search with a hybrid scoring approach.

Instead of relying on traditional keyword matching, the system understands the context of both the job description and candidate profiles, making candidate discovery more accurate, transparent, and scalable.

---

# Introduction

Recruitment platforms receive thousands of applications for a single position. Reviewing every profile manually is time-consuming, while keyword-based filtering often overlooks highly qualified candidates simply because different terminology is used.

This project addresses that challenge by building an AI-driven candidate ranking engine capable of processing more than **100,000 candidate profiles**. It evaluates each candidate using multiple dimensions, including semantic relevance, professional experience, technical skills, career growth, behavioral signals, and hiring metadata.

The goal is not only to rank candidates accurately but also to explain *why* a candidate was ranked highly, making the system useful for recruiters as well as hiring managers.

---

# Problem Statement

Design an intelligent candidate ranking system that identifies the most relevant candidates for a job description using semantic understanding instead of simple keyword matching.

---

# Solution Overview

The system follows a complete end-to-end pipeline.

A job description is first analyzed to understand its semantic meaning. Every candidate profile is then converted into a dense embedding using Sentence Transformers.

Instead of comparing keywords, the model compares contextual meaning through cosine similarity. Additional information such as technical skills, years of experience, career progression, recruiter engagement, profile completeness, and hiring metadata is incorporated into a hybrid scoring model.

Finally, candidates are ranked according to their overall relevance, and an explainable summary is generated for every recommendation.

---

# Key Features

- Semantic candidate matching using Sentence Transformers
- Hybrid scoring model combining multiple ranking signals
- Career progression analysis
- Technical skill evaluation
- Behavioral signal analysis
- Metadata-aware candidate ranking
- Explainable ranking reasons
- Automatic CSV generation
- Modular and scalable architecture
- Supports ranking of more than **100,000 candidate profiles**

---

# System Workflow

```
Job Description
        │
        ▼
Requirement Extraction
        │
        ▼
Candidate Profile Processing
        │
        ▼
Sentence Transformer Embeddings
        │
        ▼
Semantic Similarity (Cosine)
        │
        ▼
Hybrid Candidate Scoring
        │
        ▼
Explainable Ranking
        │
        ▼
submission.csv
```

---

# Ranking Methodology

Candidate ranking is based on a weighted hybrid scoring model rather than a single metric.

| Component | Weight |
|-----------|---------|
| Semantic Similarity | 40% |
| Career Analysis | 25% |
| Skill Matching | 15% |
| Behavioral Signals | 10% |
| Metadata | 5% |
| Experience | 5% |

This approach ensures that the final ranking considers both technical relevance and practical hiring signals.

---

# Explainable AI

Every ranked candidate is accompanied by recruiter-friendly explanations.

Instead of simply assigning a score, the system highlights factors such as

- Relevant technical skills
- Career progression
- Years of experience
- Recruiter response behavior
- Interview completion rate
- Profile verification
- Availability and notice period

This improves transparency and makes the ranking easier to trust.

---

# Technology Stack

| Category | Technology |
|----------|------------|
| Programming Language | Python |
| NLP Model | Sentence Transformers |
| Embedding Model | all-MiniLM-L6-v2 |
| Similarity Metric | Cosine Similarity |
| Machine Learning | Scikit-learn |
| Deep Learning | PyTorch |
| Document Parsing | python-docx |
| Numerical Computing | NumPy |

---

# Project Structure

```
redrob-ai-ranker/

├── data/
│   ├── candidates.jsonl
│   └── job_description.docx
│
├── src/
│   ├── parser/
│   ├── embeddings/
│   ├── engine/
│   └── main.py
│
├── requirements.txt
├── submission.csv
└── README.md
```

---

# Installation

Clone the repository

```bash
git clone https://github.com/your-username/redrob-ai-ranker.git
```

Move into the project directory

```bash
cd redrob-ai-ranker
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
cd src
python main.py
```

---

# Output

The system generates a `submission.csv` file containing

- Candidate Rank
- Candidate ID
- Candidate Details
- Final Hybrid Score
- Semantic Score
- Career Score
- Skill Score
- Behavioral Score
- Metadata Score
- Experience Score
- Matched Skills
- Explainable Ranking Reasons

---

# Performance

- Successfully processed **100,000 candidate profiles**
- Semantic embedding generation using Sentence Transformers
- Hybrid ranking completed with explainable recommendations
- Automatically generated recruiter-ready ranked candidate list

---

# Future Enhancements

Although the current implementation is fully functional, there are several opportunities for further improvement.

- FAISS-based vector search for faster retrieval
- Batch embedding optimization
- Embedding caching
- GPU inference support
- REST API deployment
- Interactive recruiter dashboard
- LLM-powered explanation generation
- Real-time candidate recommendation

---

# Author

**MANAS GIRDHAR**

Bachelor of Technology (Computer Science Engineering)

Interested in Artificial Intelligence, Machine Learning, Software Engineering, and Intelligent Search Systems.

---

# License

This project was developed as part of the **Redrob Intelligent Candidate Discovery & Ranking Challenge** for educational and evaluation purposes.

---

## Author

MANAS GIRDHAR

B.Tech Computer Science Engineering
