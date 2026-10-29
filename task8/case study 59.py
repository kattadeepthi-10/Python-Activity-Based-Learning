
bus = 40  # Bus capacity

data = {
    'Ibm': {'demand': 60, 'available_fleet': 2},
    'Kondapalli': {'demand': 50, 'available_fleet': 3},
    'Bench circle': {'demand': 70, 'available_fleet': 5},
}

total_unserved = 0

print(f"{'ROUTE NAME':<22} | {'DEMAND':<6} | {'NEEDED':<6} | {'DEPLOYED':<8} | {'UNSERVED'}")

for route, values in data.items():
    demand = values['demand']
    fleet = values['available_fleet']

    buses_needed = demand / bus
    buses_deployed = min(buses_needed, fleet)

    seats_provided = buses_deployed * bus
    unserved_passengers = max(0, demand - seats_provided)

    total_unserved += unserved_passengers

    status_flag = (
        f"{unserved_passengers} left"
        if unserved_passengers > 0
        else "OPTIMAL"
    )

    print(
        f"{route:<22} | {demand:<6} | {buses_needed:<6} | "
        f"{buses_deployed:<8} | {status_flag}"
    )
