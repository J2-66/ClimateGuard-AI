def calculate_flood_risk(
    rainfall,
    river_level,
    waterlogging,
    previous_flooding
):

    score = 0

    # Rainfall
    if rainfall >= 200:
        score += 3
    elif rainfall >= 100:
        score += 2
    elif rainfall >= 50:
        score += 1

    # River level
    if river_level == "Very High":
        score += 3
    elif river_level == "High":
        score += 2
    elif river_level == "Moderate":
        score += 1

    # Waterlogging
    if waterlogging == "Severe":
        score += 3
    elif waterlogging == "Moderate":
        score += 2
    elif waterlogging == "Minor":
        score += 1

    # Previous flooding
    if previous_flooding == "Yes":
        score += 2

    # Risk classification
    if score >= 8:
        risk = "Critical"
    elif score >= 6:
        risk = "High"
    elif score >= 3:
        risk = "Moderate"
    else:
        risk = "Low"

    return risk, score