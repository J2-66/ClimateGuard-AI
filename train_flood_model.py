import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score


# =========================================================
# 1. Create a small educational flood-risk dataset
# =========================================================

data = {

    "rainfall_mm": [
        20, 35, 45, 60, 75,
        90, 110, 130, 150, 180,
        200, 220, 250, 280, 300,
        320, 350, 380, 400, 450
    ],

    "river_level": [
        1, 1, 1, 1, 2,
        2, 2, 3, 3, 3,
        3, 4, 4, 4, 4,
        4, 5, 5, 5, 5
    ],

    "waterlogging": [
        0, 0, 0, 1, 1,
        1, 1, 1, 2, 2,
        2, 2, 3, 3, 3,
        3, 3, 3, 3, 3
    ],

    "previous_flooding": [
        0, 0, 0, 0, 0,
        0, 1, 1, 1, 1,
        1, 1, 1, 1, 1,
        1, 1, 1, 1, 1
    ],

    "temperature": [
        25, 25, 26, 26, 27,
        27, 28, 28, 29, 29,
        29, 30, 30, 30, 31,
        31, 31, 32, 32, 32
    ],

    "humidity": [
        55, 58, 60, 62, 65,
        68, 70, 72, 75, 78,
        80, 82, 84, 86, 88,
        90, 91, 92, 94, 95
    ],

    "risk": [
        "Low", "Low", "Low", "Low", "Low",
        "Moderate", "Moderate", "Moderate",
        "Moderate", "Moderate",
        "High", "High", "High", "High", "High",
        "High", "High", "High", "High", "High"
    ]
}


df = pd.DataFrame(data)


print("=" * 60)
print("CLIMATEGUARD AI - FLOOD MODEL TRAINING")
print("=" * 60)

print("\nDataset:")
print(df)


# =========================================================
# 2. Separate features and target
# =========================================================

X = df[
    [
        "rainfall_mm",
        "river_level",
        "waterlogging",
        "previous_flooding",
        "temperature",
        "humidity"
    ]
]

y = df["risk"]


# =========================================================
# 3. Split dataset
# =========================================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.25,
    random_state=42,
    stratify=y
)


# =========================================================
# 4. Train Random Forest
# =========================================================

model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)


# =========================================================
# 5. Evaluate model
# =========================================================

predictions = model.predict(X_test)

accuracy = accuracy_score(
    y_test,
    predictions
)

print("\nModel Accuracy:")
print(f"{accuracy * 100:.2f}%")

print("\nClassification Report:")
print(
    classification_report(
        y_test,
        predictions
    )
)


# =========================================================
# 6. Save model
# =========================================================

joblib.dump(
    model,
    "flood_model.pkl"
)

print("\nModel saved successfully:")
print("flood_model.pkl")

print("\n" + "=" * 60)
print("FLOOD MODEL TRAINING COMPLETE")
print("=" * 60)