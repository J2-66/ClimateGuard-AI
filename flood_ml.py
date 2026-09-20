import joblib
import pandas as pd

from granite_service import ask_granite


MODEL_PATH = "flood_model.pkl"

model = joblib.load(MODEL_PATH)


def predict_flood_risk(
    rainfall,
    river_level,
    waterlogging,
    previous_flooding,
    temperature,
    humidity
):

    data = pd.DataFrame([
        {
            "rainfall_mm": rainfall,
            "river_level": river_level,
            "waterlogging": waterlogging,
            "previous_flooding": previous_flooding,
            "temperature": temperature,
            "humidity": humidity
        }
    ])

    prediction = model.predict(data)[0]

    probabilities = model.predict_proba(data)[0]

    classes = model.classes_

    probability_dict = {
        class_name: float(probability)
        for class_name, probability
        in zip(classes, probabilities)
    }

    return prediction, probability_dict


def generate_flood_explanation(
    rainfall,
    river_level,
    waterlogging,
    previous_flooding,
    temperature,
    humidity,
    prediction,
    probabilities
):

    probability_text = "\n".join(
        [
            f"{level}: {probability * 100:.2f}%"
            for level, probability
            in probabilities.items()
        ]
    )

    prompt = f"""
You are ClimateGuard AI, a flood-risk awareness assistant.

A machine-learning model produced the following
educational flood-risk prediction.

INPUT CONDITIONS:

Rainfall: {rainfall} mm
River Level: {river_level}
Waterlogging Level: {waterlogging}
Previous Flooding: {previous_flooding}
Temperature: {temperature} °C
Humidity: {humidity}%

MODEL PREDICTION:
{prediction}

MODEL PROBABILITIES:
{probability_text}

Explain the result in simple English.

Provide:

1. Predicted Risk
2. Main Factors
3. What the Prediction Means
4. Safety Recommendations
5. Important Limitations

IMPORTANT:
- This is an educational ML prediction.
- It is NOT an official flood warning.
- Do not claim certainty.
- Do not invent weather or local emergency information.

Keep the answer concise.
"""

    return ask_granite(
        prompt,
        max_new_tokens=450,
        temperature=0.2
    )