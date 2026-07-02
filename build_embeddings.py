import numpy as np

from parser.candidate_loader import load_candidates
from embeddings.semantic_engine import (
    candidate_text,
    create_embedding
)

print("Loading candidates...")

candidates = load_candidates("data/candidates.jsonl")

embeddings = []

print("Generating embeddings...")

for i, candidate in enumerate(candidates):

    text = candidate_text(candidate)

    emb = create_embedding(text)

    embeddings.append(emb)

    if (i + 1) % 1000 == 0:
        print(f"{i+1} completed")

embeddings = np.array(embeddings)

np.save("data/candidate_embeddings.npy", embeddings)

print("Done")
print(embeddings.shape)