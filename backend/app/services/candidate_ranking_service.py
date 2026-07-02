from app.services.job_matching_service import (
    calculate_match_score
)


def rank_candidates(
    applications,
    job
):
    rankings = []

    for application in applications:
        candidate = application.candidate

        if not candidate:
            continue

        skills = candidate.skills or ""

        result = calculate_match_score(
            skills,
            job.skills_required
        )

        rankings.append(
            {
                "application_id": application.id,
                "candidate_id": candidate.id,
                "match_score":
                    result["match_score"],
                "matched_skills":
                    result["matched_skills"],
                "missing_skills":
                    result["missing_skills"]
            }
        )

    rankings.sort(
        key=lambda x: x["match_score"],
        reverse=True
    )

    return rankings