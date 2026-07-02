from parser.candidate_loader import load_candidates
from parser.jd_parser import load_job_description

from embeddings.semantic_engine import (
    candidate_text,
    create_embedding
)

from engine.rank import (
    CandidateRanker,
    export_submission,
    print_top_candidates
)


CANDIDATE_FILE = "../data/candidates.jsonl"
JD_FILE = "../data/job_description.docx"


def precompute_embeddings(candidates):
    
    print("\nBuilding candidate embeddings...\n")

    total = len(candidates)

    for idx, candidate in enumerate(candidates):

        text = candidate_text(candidate)

        candidate["embedding"] = create_embedding(text)

        if (idx + 1) % 1000 == 0:
            print(f"Embedded {idx + 1}/{total}")

    return candidates


def main():

    print("=" * 60)
    print("REDROB INTELLIGENT CANDIDATE DISCOVERY")
    print("=" * 60)

    ###########################################
    # Load Candidates
    ###########################################

    print("\nLoading Candidates...")

    candidates = load_candidates(CANDIDATE_FILE)

    print(f"{len(candidates)} candidates loaded.")

    ###########################################
    # Load JD
    ###########################################

    print("\nLoading Job Description...")

    job_description = load_job_description(JD_FILE)

    ###########################################
    # Candidate Embeddings
    ###########################################

    candidates = precompute_embeddings(candidates)

    ###########################################
    # Ranking
    ###########################################

    ranker = CandidateRanker(job_description)

    ranked = ranker.rank_candidates(candidates)

    ###########################################
    # Top Candidates
    ###########################################

    print_top_candidates(ranked, 10)

    ###########################################
    # Export CSV
    ###########################################

    export_submission(ranked)

    print("\nDone.")


if __name__ == "__main__":
    main()