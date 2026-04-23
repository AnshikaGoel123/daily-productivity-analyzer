def calculate_productivity(sleep, work, focus):
    # Sleep Score (ideal around 8 hrs)
    sleep_score = max(0, 100 - abs(8 - sleep) * 12)

    # Work Score (ideal 6 to 8 hrs)
    if work <= 8:
        work_score = work * 12.5
    else:
        work_score = max(0, 100 - (work - 8) * 10)

    # Focus Score (1 to 10 converted to 10 to 100)
    focus_score = focus * 10

    # Weighted Final Score
    final_score = (
        sleep_score * 0.35 +
        work_score * 0.40 +
        focus_score * 0.25
    )

    final_score = max(0, min(final_score, 100))

    return round(final_score, 2)