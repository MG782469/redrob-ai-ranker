# AI-Powered Intelligent Candidate Discovery & Ranking System

## Overview

Hiring teams often receive thousands of applications for a single role, making manual screening slow and difficult. Traditional keyword-based filtering can miss strong candidates because it relies on exact word matches rather than understanding the actual context of a candidate's experience.

This project presents an intelligent candidate ranking system that uses semantic search and a hybrid scoring approach to identify the most relevant candidates for a given job description. Instead of relying only on keywords, the system evaluates multiple aspects of a candidate profile, including professional experience, technical skills, career progression, behavioral indicators, and hiring metadata.

The final result is an explainable ranking that helps recruiters identify the most suitable candidates quickly and consistently.

---

## Key Features

- Semantic matching between resumes and job descriptions using Sentence Transformers
- Hybrid scoring model combining multiple candidate signals
- Career progression and experience analysis
- Skill-based evaluation
- Behavioral signal analysis
- Metadata-based scoring
- Explainable ranking with human-readable reasons
- Automatic generation of the final ranked candidate list

---

## System Workflow

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
Cosine Similarity
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

## Hybrid Scoring Strategy

The final score is calculated using the following weighted components:

| Component | Weight |
|-----------|--------|
| Semantic Similarity | 40% |
| Career Analysis | 25% |
| Skill Matching | 15% |
| Behavioral Signals | 10% |
| Metadata | 5% |
| Experience | 5% |

This combination allows the system to evaluate candidates from multiple perspectives instead of relying on a single metric.

---

## Technology Stack

- Python
- Sentence Transformers
- Hugging Face
- PyTorch
- NumPy
- Scikit-learn
- python-docx

---

## Project Structure

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

## Installation

Clone the repository

```bash
git clone https://github.com/your-username/redrob-ai-ranker.git
```

Install the required dependencies

```bash
pip install -r requirements.txt
```

Run the project

```bash
cd src
python main.py
```

---

## Output

The system generates a `submission.csv` file containing:

- Candidate Rank
- Candidate ID
- Candidate Information
- Final Hybrid Score
- Individual Component Scores
- Matched Skills
- Ranking Explanation

---

## Future Improvements

- Batch embedding generation
- Embedding caching
- FAISS-based vector search
- REST API deployment
- Real-time candidate search
- Dashboard for recruiters

---

## Author

MANAS GIRDHAR

B.Tech Computer Science Engineering
