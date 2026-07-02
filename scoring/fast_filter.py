from engine.career_engine import career_score
from engine.behavior_engine import get_behavior_score
from engine.metadata_engine import metadata_score

AI_SKILLS = {
    "python","machine learning","deep learning","nlp","llm",
    "rag","retrieval","ranking","embeddings","faiss","milvus",
    "pinecone","weaviate","qdrant","vector databases",
    "transformers","pytorch","tensorflow","bert","lora","qlora"
}

def skill_score(candidate):
    score = 0

    for skill in candidate["skills"]:
        name = skill["name"].lower()

        if name in AI_SKILLS:
            score += 2

            if skill["proficiency"] in ["advanced","expert"]:
                score += 2

            score += min(skill["endorsements"]/20,2)

    return score


def fast_score(candidate):

    return (
        career_score(candidate)*0.45 +
        skill_score(candidate)*0.25 +
        get_behavior_score(candidate)*0.20 +
        metadata_score(candidate)*0.10
    )