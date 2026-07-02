from engine.career_engine import get_total_experience


def generate_reason(candidate, scores, job_description):
    """
    Generate recruiter-friendly reasons for ranking.
    """

    reasons = []

    profile = candidate["profile"]

    ####################################################
    # Semantic Match
    ####################################################

    if scores["semantic"] >= 80:
        reasons.append(
            "Excellent semantic match with the job description."
        )

    elif scores["semantic"] >= 65:
        reasons.append(
            "Strong alignment with the required role."
        )

    elif scores["semantic"] >= 50:
        reasons.append(
            "Reasonable relevance to the job requirements."
        )

    ####################################################
    # Experience
    ####################################################

    exp = get_total_experience(candidate)

    reasons.append(
        f"{exp:.1f} years of professional experience."
    )

    ####################################################
    # Current Role
    ####################################################

    title = profile.get("current_title", "")

    if title:
        reasons.append(
            f"Currently working as {title}."
        )

    ####################################################
    # Skill Match
    ####################################################

    jd = job_description.lower()

    matched_skills = []

    for skill in candidate.get("skills", []):

        skill_name = skill["name"]

        if skill_name.lower() in jd:
            matched_skills.append(skill_name)

    if matched_skills:

        matched_skills = matched_skills[:5]

        reasons.append(

            "Matched skills: "

            + ", ".join(matched_skills)

        )

    ####################################################
    # Behaviour
    ####################################################

    signals = candidate["redrob_signals"]

    if signals.get("open_to_work_flag"):

        reasons.append(
            "Open to new opportunities."
        )

    if signals.get("interview_completion_rate", 0) >= 0.70:

        reasons.append(
            "Strong interview completion rate."
        )

    if signals.get("recruiter_response_rate", 0) >= 0.50:

        reasons.append(
            "Responds well to recruiters."
        )

    ####################################################
    # Metadata
    ####################################################

    if signals.get("verified_email"):

        reasons.append(
            "Verified email."
        )

    if signals.get("verified_phone"):

        reasons.append(
            "Verified phone number."
        )

    if signals.get("notice_period_days", 999) <= 30:

        reasons.append(
            "Short notice period."
        )

    ####################################################
    # Career
    ####################################################

    if scores["career"] >= 75:

        reasons.append(
            "Strong AI/ML career progression."
        )

    elif scores["career"] >= 50:

        reasons.append(
            "Relevant engineering background."
        )

    ####################################################
    # Final Cleanup
    ####################################################

    seen = set()

    final_reasons = []

    for reason in reasons:

        if reason not in seen:

            final_reasons.append(reason)

            seen.add(reason)

    return final_reasons