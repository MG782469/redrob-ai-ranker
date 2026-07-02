from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

print("Loading Sentence Transformer...")

model = SentenceTransformer("all-MiniLM-L6-v2")


def create_embedding(text):
    """
    Create normalized embedding for a single text.
    """
    return model.encode(
        text,
        convert_to_numpy=True,
        normalize_embeddings=True
    )


def create_embeddings_batch(texts, batch_size=64):
    """
    Create embeddings for multiple texts efficiently.
    """
    return model.encode(
        texts,
        batch_size=batch_size,
        convert_to_numpy=True,
        normalize_embeddings=True,
        show_progress_bar=True
    )


def similarity_from_embeddings(emb1, emb2):
    """
    Cosine similarity between two normalized embeddings.
    """
    return float(
        cosine_similarity([emb1], [emb2])[0][0]
    )


def candidate_text(candidate):
    """
    Convert candidate JSON into a single text representation.
    """

    profile = candidate["profile"]

    parts = [
        profile.get("headline", ""),
        profile.get("summary", ""),
        profile.get("current_title", "")
    ]

    # Career History
    for job in candidate.get("career_history", []):
        parts.append(job.get("title", ""))
        parts.append(job.get("description", ""))

    # Skills
    for skill in candidate.get("skills", []):
        parts.append(skill.get("name", ""))

    # Education
    for edu in candidate.get("education", []):
        parts.append(edu.get("degree", ""))
        parts.append(edu.get("field_of_study", ""))

    # Certifications
    for cert in candidate.get("certifications", []):
        if isinstance(cert, dict):
            parts.append(cert.get("name", ""))
        else:
            parts.append(str(cert))

    return " ".join(
        str(part) for part in parts if part
    )