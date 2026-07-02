from parser.candidate_loader import load_candidates
from engine.skill_engine import extract_skills
from engine.career_engine import (
    get_total_experience,
    get_current_title,
    get_current_company,
)
from engine.behavior_engine import get_behavior_score
from scoring.hybrid_score import calculate_score
from engine.jd_engine import extract_jd_features
from embeddings.semantic_engine import similarity

candidates = load_candidates("data/candidates.jsonl")

print("Total Candidates:", len(candidates))

print("\nFirst Candidate ID:")
print(candidates[0]["candidate_id"])

print("\nCurrent Title:")
print(candidates[0]["profile"]["current_title"])

print("\nSkills:")
print(len(candidates[0]["skills"]))

from parser.jd_parser import load_job_description

jd = load_job_description("data/job_description.docx")

print("\nJob Description Loaded:", len(jd), "characters")
skills = extract_skills(candidates[0])

print("\nFirst 5 Skills:")
print(skills[:5])

print("\nExperience:", get_total_experience(candidates[0]))
print("Current Title:", get_current_title(candidates[0]))
print("Current Company:", get_current_company(candidates[0]))

print("\nBehavior Score:", get_behavior_score(candidates[0]))
print("\nHybrid Score:", calculate_score(candidates[0]))

features = extract_jd_features(jd)

print("\nJD Features:")
print(features)

candidate_text = (
    candidates[0]["profile"]["headline"] + " " +
    candidates[0]["profile"]["summary"]
)

score = similarity(jd, candidate_text)

print("\nSemantic Similarity:", round(score, 4))