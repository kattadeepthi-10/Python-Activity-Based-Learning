
data = {
    "Monday":    {"prepared": 500, "served": 420, "leftovers": 80},
    "Tuesday":   {"prepared": 480, "served": 450, "leftovers": 30},
    "Wednesday": {"prepared": 550, "served": 410, "leftovers": 140},
    "Thursday":  {"prepared": 600, "served": 560, "leftovers": 40},
    "Friday":    {"prepared": 520, "served": 400, "leftovers": 100}
}

ACCEPTABLE_LIMIT = 15.0

print(f"{'DAY':<12} | {'WASTAGE %':<10} | {'STATUS'}")

for day, data_info in data.items():
    prepared = data_info["prepared"]
    leftovers = data_info["leftovers"]

    # Calculate percentage out of total prepared food
    waste_percentage = (leftovers / prepared) * 100

    if waste_percentage > ACCEPTABLE_LIMIT:
        status = "EXCEEDS LIMIT"
    else:
        status = "ACCEPTABLE"

    print(f"{day:<12} | {waste_percentage:>8.1f}% | {status}")
