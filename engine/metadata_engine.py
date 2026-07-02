def metadata_score(candidate):
    """
    Returns a normalized metadata score (0-100).
    """

    signals = candidate.get("redrob_signals", {})

    score = 0.0

    ####################################################
    # Open to Work
    ####################################################

    if signals.get("open_to_work_flag", False):
        score += 20

    ####################################################
    # Relocation
    ####################################################

    if signals.get("willing_to_relocate", False):
        score += 10

    ####################################################
    # Preferred Work Mode
    ####################################################

    work_mode = signals.get(
        "preferred_work_mode",
        ""
    ).lower()

    if work_mode == "hybrid":
        score += 10

    elif work_mode == "flexible":
        score += 10

    elif work_mode == "remote":
        score += 8

    elif work_mode == "onsite":
        score += 5

    ####################################################
    # Notice Period
    ####################################################

    notice = signals.get(
        "notice_period_days",
        90
    )

    if notice <= 15:
        score += 20

    elif notice <= 30:
        score += 15

    elif notice <= 60:
        score += 10

    elif notice <= 90:
        score += 5

    ####################################################
    # Contact Verification
    ####################################################

    if signals.get("verified_email", False):
        score += 10

    if signals.get("verified_phone", False):
        score += 10

    ####################################################
    # LinkedIn Connected
    ####################################################

    if signals.get("linkedin_connected", False):
        score += 5

    ####################################################
    # Final Clamp
    ####################################################

    score = min(score, 100)

    return round(score, 2)