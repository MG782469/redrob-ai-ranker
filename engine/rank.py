import csv
from embeddings.semantic_engine import (
    create_embedding,
    similarity_from_embeddings
)
from engine.career_engine import career_score, get_total_experience
from engine.behavior_engine import get_behavior_score
from engine.metadata_engine import metadata_score
from engine.reason_engine import generate_reason

class CandidateRanker:
    def __init__(self, job_description):
        self.job_description = job_description
        print("Initializing Ranker and creating JD embedding...")
        self.jd_embedding = create_embedding(job_description)

    def skill_score(self, candidate):
        jd = self.job_description.lower()
        score = 0
        matched = []
        for skill in candidate.get("skills", []):
            name = skill.get("name", "")
            if not name:
                continue
            if name.lower() in jd:
                matched.append(name)
                score += 8
            
            proficiency = skill.get("proficiency", "").lower()
            if proficiency == "advanced":
                score += 3
            elif proficiency == "intermediate":
                score += 2
            else:
                score += 1
            
            score += min(skill.get("duration_months", 0) / 12, 3)
            score += min(skill.get("endorsements", 0) / 20, 3)
        
        return round(min(score, 100), 2), matched

    def experience_score(self, candidate):
        exp = get_total_experience(candidate)
        if exp >= 12: return 100
        elif exp >= 10: return 90
        elif exp >= 8: return 80
        elif exp >= 6: return 70
        elif exp >= 4: return 60
        elif exp >= 2: return 45
        return 25

    def semantic_score(self, candidate):
        embedding = candidate.get("embedding")
        # FIX 1: NumPy array check fix
        if embedding is None:
            return 0
        similarity = similarity_from_embeddings(self.jd_embedding,embedding)
        return round(similarity * 100, 2)

    @staticmethod
    def normalize(score):
        return max(0, min(score, 100))

    def hybrid_score(self, candidate):
        semantic = self.normalize(self.semantic_score(candidate))
        career = self.normalize(career_score(candidate))
        behavior = self.normalize(get_behavior_score(candidate))
        metadata = self.normalize(metadata_score(candidate))
        experience = self.normalize(self.experience_score(candidate))
        skill, matched_skills = self.skill_score(candidate)
        skill = self.normalize(skill)

        final_score = (
            semantic * 0.40 +
            career * 0.25 +
            skill * 0.15 +
            behavior * 0.10 +
            metadata * 0.05 +
            experience * 0.05
        )

        scores = {
            "semantic": round(semantic, 2),
            "career": round(career, 2),
            "behavior": round(behavior, 2),
            "metadata": round(metadata, 2),
            "skill": round(skill, 2),
            "experience": round(experience, 2),
            "final": round(final_score, 2)
        }
        return scores, matched_skills

    def rank_candidate(self, candidate):
        scores, matched_skills = self.hybrid_score(candidate)
        reasons = generate_reason(candidate, scores, self.job_description)
        profile = candidate.get("profile", {})
        
        return {
            "candidate_id": candidate.get("candidate_id"),
            "candidate": candidate,
            "name": profile.get("anonymized_name", ""),
            "headline": profile.get("headline", ""),
            "title": profile.get("current_title", ""),
            "company": profile.get("current_company", ""),
            "location": profile.get("location", ""),
            "country": profile.get("country", ""),
            "matched_skills": matched_skills,
            "score": scores["final"],
            "semantic_score": scores["semantic"],
            "career_score": scores["career"],
            "behavior_score": scores["behavior"],
            "metadata_score": scores["metadata"],
            "skill_score": scores["skill"],
            "experience_score": scores["experience"],
            "reasons": reasons
        }

    def rank_candidates(self, candidates):
        print("\nRanking candidates...\n")
        ranked = []
        total = len(candidates)
        # FIX 3: Progress tracking loop
        for idx, candidate in enumerate(candidates):
            ranked.append(self.rank_candidate(candidate))
            if (idx + 1) % 1000 == 0:
                print(f"Processed {idx + 1}/{total} candidates")
                
        ranked.sort(key=lambda x: x["score"], reverse=True)
        return ranked

def export_submission(ranked_candidates, output_file="submission.csv", top_k=None):
    # FIX 2: Correct top_k check
    if top_k is not None:
        ranked_candidates = ranked_candidates[:top_k]
    
    with open(output_file, "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["rank", "candidate_id", "candidate_name", "headline", "current_title", "company", "location", "country", "final_score", "semantic_score", "career_score", "behavior_score", "metadata_score", "skill_score", "experience_score", "matched_skills", "reasons"])
        for rank, c in enumerate(ranked_candidates, start=1):
            writer.writerow([rank, c["candidate_id"], c["name"], c["headline"], c["title"], c["company"], c["location"], c["country"], c["score"], c["semantic_score"], c["career_score"], c["behavior_score"], c["metadata_score"], c["skill_score"], c["experience_score"], ", ".join(c["matched_skills"]), " | ".join(c["reasons"])])
    print(f"\n{output_file} generated successfully.")

def print_top_candidates(ranked_candidates, k=10):
    print("\n" + "=" * 100 + f"\nTOP {k} CANDIDATES\n" + "=" * 100)
    for rank, c in enumerate(ranked_candidates[:k], start=1):
        print(f"\nRank #{rank} | ID: {c['candidate_id']} | Name: {c['name']}")
        print(f"Score: {c['score']:.2f} | Title: {c['title']} @ {c['company']}")
        print(f"Skills: {', '.join(c['matched_skills']) if c['matched_skills'] else 'None'}")
        for r in c['reasons']: print(f"• {r}")
        print("-" * 80)