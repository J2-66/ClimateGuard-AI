def flood_risk(rainfall, river, soil, drainage, elevation, forecast):
    score = 0
    score += min(rainfall / 300 * 30, 30)
    score += min(forecast / 300 * 20, 20)
    score += min(river / 8 * 20, 20)
    score += soil / 100 * 10
    score += (100 - drainage) / 100 * 10
    score += max(0, (30 - min(elevation, 30)) / 30 * 10)
    score = int(round(min(score, 100)))

    if score >= 70:
        level = "HIGH"
        actions = [
            "Monitor official local flood and weather alerts.",
            "Avoid unnecessary travel through flooded roads.",
            "Move important items/equipment to safer elevated locations.",
            "Follow evacuation instructions if issued by authorities."
        ]
    elif score >= 40:
        level = "MEDIUM"
        actions = [
            "Continue monitoring rainfall, river levels and official alerts.",
            "Check drainage routes and prepare essential items.",
            "Avoid low-lying areas if water levels are increasing."
        ]
    else:
        level = "LOW"
        actions = [
            "Maintain normal precautions.",
            "Keep drainage pathways clear.",
            "Continue checking official forecasts during heavy-rain periods."
        ]

    explanation = (
        "The score combines rainfall, forecast rainfall, river level, soil moisture, "
        "drainage quality and elevation. It is a transparent educational model, not a "
        "hydrological forecast or government warning."
    )
    return {"score": score, "level": level, "explanation": explanation, "actions": actions}
