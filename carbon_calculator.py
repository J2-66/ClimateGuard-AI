def calculate_carbon_footprint(
    electricity_kwh,
    car_km,
    public_transport_km,
    flights
):

    # Approximate electricity factor
    electricity_factor = 0.7

    # Approximate petrol car factor
    car_factor = 0.17

    # Approximate public transport factor
    public_transport_factor = 0.05

    # Approximate flight factor per flight
    flight_factor = 250

    electricity_emission = (
        electricity_kwh * electricity_factor
    )

    car_emission = (
        car_km * car_factor
    )

    public_transport_emission = (
        public_transport_km *
        public_transport_factor
    )

    flight_emission = (
        flights * flight_factor
    )

    total = (
        electricity_emission
        + car_emission
        + public_transport_emission
        + flight_emission
    )

    return {
        "electricity": electricity_emission,
        "car": car_emission,
        "public_transport": public_transport_emission,
        "flights": flight_emission,
        "total": total
    }