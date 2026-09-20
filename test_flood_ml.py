from flood_ml import predict_flood_risk


print("=" * 60)
print("       CLIMATEGUARD AI - ML FLOOD TEST")
print("=" * 60)


risk, probabilities = predict_flood_risk(
    rainfall=180,
    river_level=4,
    waterlogging=2,
    previous_flooding=1,
    temperature=30,
    humidity=85
)


print("\nPredicted Flood Risk:")
print(risk)


print("\nRisk Probabilities:")

for level, probability in probabilities.items():

    print(
        f"{level}: "
        f"{probability * 100:.2f}%"
    )


print("\n" + "=" * 60)
print("ML FLOOD TEST COMPLETE")
print("=" * 60)