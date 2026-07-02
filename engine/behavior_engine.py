def get_behavior_score(candidate):
    """
    Returns a normalized behavior score (0-100).
    """

    signals = candidate.get("redrob_signals", {})

    score = 0.0

    ####################################################
    # Open to Work
    ####################################################

    if signals.get("open_to_work_flag", False):
        score += 20

    ####################################################
    # Recruiter Response Rate (0-1)
    ####################################################

    score += min(
        signals.get("recruiter_response_rate", 0) * 25,
        25
    )

    ####################################################
    # Interview Completion (0-1)
    ####################################################

    score += min(
        signals.get("interview_completion_rate", 0) * 20,
        20
    )

    ####################################################
    # Offer Acceptance (0-1)
    ####################################################

    score += min(
        signals.get("offer_acceptance_rate", 0) * 10,
        10
    )

    ####################################################
    # GitHub Activity (0-100)
    ####################################################

    score += min(
        signals.get("github_activity_score", 0) * 0.5,
        10
    )

    ####################################################
    # Profile Completeness
    ####################################################

    score += min(
        signals.get("profile_completeness_score", 0) * 0.10,
        10
    )

    ####################################################
    # Recruiter Interest
    ####################################################

    score += min(
        signals.get("saved_by_recruiters_30d", 0),
        5
    )

    ####################################################
    # Search Appearance
    ####################################################

    score += min(
        signals.get("search_appearance_30d", 0) / 100,
        5
    )

    ####################################################
    # Fast Response Bonus
    ####################################################

    response_hours = signals.get(
        "avg_response_time_hours",
        9999
    )

    if response_hours <= 24:
        score += 5

    elif response_hours <= 72:
        score += 3

    ####################################################
    # Final Clamp
    ####################################################

    score = max(score, 0)
    score = min(score, 100)

    return round(score, 2)