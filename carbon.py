def estimate_carbon(electricity, car_km, bus_km, flights, lpg, diet):
    # Illustrative educational factors; replace with authoritative regional factors.
    factors = {
        "electricity": 0.70,   # kg CO2e/kWh
        "car": 0.18,           # kg CO2e/km
        "bus": 0.08,
        "flight": 250.0,       # kg CO2e/short-haul trip
        "lpg": 42.0,           # kg CO2e/cylinder
        "diet": {"Mixed": 60.0, "Low-meat": 45.0, "Vegetarian": 30.0}
    }
    values = [
        ("Electricity", electricity * factors["electricity"]),
        ("Car travel", car_km * factors["car"]),
        ("Bus travel", bus_km * factors["bus"]),
        ("Flights", flights * factors["flight"]),
        ("LPG", lpg * factors["lpg"]),
        ("Diet", factors["diet"][diet])
    ]
    total = sum(v for _, v in values)
    largest = max(values, key=lambda x: x[1])[0]
    suggestions = {
        "Electricity": "Reduce standby consumption, improve efficiency, and consider renewable electricity where practical.",
        "Car travel": "Combine trips, use public transport, walk/cycle for short journeys, or car-share.",
        "Bus travel": "Prefer public transport over private vehicle travel when feasible.",
        "Flights": "Avoid unnecessary flights and consider rail/virtual alternatives when practical.",
        "LPG": "Improve cooking efficiency and reduce avoidable fuel use.",
        "Diet": "Increase plant-based meals and reduce food waste."
    }
    return {
        "total_kg": total,
        "largest_source": largest,
        "breakdown": [{"Source": k, "kg CO2e/month": round(v,2)} for k,v in values],
        "suggestions": [suggestions[k] for k,_ in sorted(values, key=lambda x:x[1], reverse=True)[:3]]
    }
