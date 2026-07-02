def extract_skills(candidate):
    return [skill["name"].lower() for skill in candidate["skills"]]
