def calculate_match_score(
    candidate_skills: str,
    job_skills: str
):
    candidate_set = set(
        skill.strip().lower()
        for skill in candidate_skills.split(",")
        if skill.strip()
    )

    job_set = set(
        skill.strip().lower()
        for skill in job_skills.split(",")
        if skill.strip()
    )

    if not job_set:
        return 0

    matched = (
        candidate_set.intersection(
            job_set
        )
    )

    score = (
        len(matched)
        / len(job_set)
    ) * 100

    return {
        "match_score": round(score, 2),
        "matched_skills": list(matched),
        "missing_skills": list(
            job_set - matched
        )
    }