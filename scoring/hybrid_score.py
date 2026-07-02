from embeddings.semantic_engine import similarity
from engine.career_engine import career_score
from engine.behavior_engine import get_behavior_score


def build_candidate_text(candidate):
    profile = candidate["profile"]

    text = []

    text.append(profile["headline"])
    text.append(profile["summary"])
    text.append(profile["current_title"])

    # Skills
    for skill in candidate["skills"]:
        text.append(skill["name"])

    # Career History
    for job in candidate["career_history"]:
        text.append(job["title"])
        text.append(job["description"])

    return " ".join(text)


def metadata_score(candidate):

    score = 0

    signals = candidate["redrob_signals"]

    # Relocation
    if signals["willing_to_relocate"]:
        score += 3

    # Open To Work
    if signals["open_to_work_flag"]:
        score += 3

    # Hybrid preference
    if signals["preferred_work_mode"] in ["hybrid", "flexible"]:
        score += 2

    # Short notice
    if signals["notice_period_days"] <= 30:
        score += 2

    return score


def calculate_score(candidate, jd):

    candidate_text = build_candidate_text(candidate)

    semantic = similarity(jd, candidate_text) * 100

    career = career_score(candidate)

    behavior = get_behavior_score(candidate)

    metadata = metadata_score(candidate)

    final_score = (
        semantic * 0.35 +
        career * 0.35 +
        behavior * 0.20 +
        metadata * 0.10
    )

    return round(final_score, 2)