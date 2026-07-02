AI_TITLES = {
    "ai engineer",
    "machine learning engineer",
    "ml engineer",
    "data scientist",
    "applied scientist",
    "nlp engineer",
    "computer vision engineer",
    "search engineer",
    "recommendation engineer",
    "backend engineer",
    "software engineer",
    "research engineer",
    "deep learning engineer",
    "generative ai engineer",
    "llm engineer"
}

NEGATIVE_TITLES = {
    "marketing",
    "sales",
    "hr",
    "accountant",
    "graphic designer",
    "content writer",
    "customer support",
    "operations",
    "civil engineer",
    "mechanical engineer"
}

CAREER_KEYWORDS = {
    "retrieval",
    "ranking",
    "recommendation",
    "search",
    "embedding",
    "vector",
    "llm",
    "transformer",
    "rag",
    "semantic",
    "information retrieval",
    "faiss",
    "pinecone",
    "weaviate",
    "qdrant",
    "milvus",
    "langchain",
    "huggingface",
    "pytorch",
    "tensorflow",
    "bert",
    "gpt",
    "openai",
    "fine tuning",
    "lora",
    "agent",
    "airflow",
    "spark",
    "kafka"
}


def get_total_experience(candidate):
    return candidate["profile"].get(
        "years_of_experience",
        0
    )


def career_score(candidate):

    profile = candidate["profile"]

    score = 0

    ####################################################
    # Current Title
    ####################################################

    current_title = profile.get(
        "current_title",
        ""
    ).lower()

    if any(title in current_title for title in AI_TITLES):
        score += 35

    if any(title in current_title for title in NEGATIVE_TITLES):
        score -= 20

    ####################################################
    # Career History
    ####################################################

    ai_jobs = 0

    keyword_hits = 0

    for job in candidate.get("career_history", []):

        title = job.get("title", "").lower()

        description = job.get(
            "description",
            ""
        ).lower()

        if any(t in title for t in AI_TITLES):
            ai_jobs += 1
            score += 10

        keyword_hits += sum(
            1
            for kw in CAREER_KEYWORDS
            if kw in description
        )

    score += min(keyword_hits * 2, 25)

    ####################################################
    # Experience
    ####################################################

    exp = get_total_experience(candidate)

    if exp >= 10:
        score += 20

    elif exp >= 7:
        score += 18

    elif exp >= 5:
        score += 15

    elif exp >= 3:
        score += 10

    elif exp >= 1:
        score += 5

    ####################################################
    # Career Stability
    ####################################################

    jobs = len(candidate.get("career_history", []))

    if jobs == 1:
        score += 8

    elif jobs <= 3:
        score += 6

    elif jobs <= 5:
        score += 4

    ####################################################
    # Final Clamp
    ####################################################

    score = max(score, 0)

    score = min(score, 100)

    return round(score, 2)