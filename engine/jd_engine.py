import re


def extract_jd_features(job_description):

    jd = job_description.lower()

    features = {}

    # Experience
    exp = re.search(r'(\d+)\s*[-–]\s*(\d+)\s*years', jd)

    if exp:
        features["min_experience"] = int(exp.group(1))
        features["max_experience"] = int(exp.group(2))
    else:
        features["min_experience"] = 0
        features["max_experience"] = 100

    # Required Skills
    features["required_skills"] = [
        "python",
        "embeddings",
        "retrieval",
        "ranking",
        "llm",
        "vector databases",
        "faiss",
        "evaluation",
    ]

    # Preferred Locations
    features["locations"] = [
        "noida",
        "pune",
        "hyderabad",
        "delhi",
        "mumbai"
    ]

    return features