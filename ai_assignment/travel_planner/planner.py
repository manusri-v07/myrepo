# Advanced AI Travel Planner

places = {
    "Goa": {
        "type": "beach",
        "budget": 5000,
        "food": ["seafood", "continental"]
    },
    "Manali": {
        "type": "mountain",
        "budget": 7000,
        "food": ["north indian"]
    },
    "Jaipur": {
        "type": "historical",
        "budget": 4000,
        "food": ["rajasthani"]
    },
    "Kerala": {
        "type": "beach",
        "budget": 6000,
        "food": ["south indian", "seafood"]
    }
}

# Scoring function (AI logic)
def calculate_score(details, budget, interest, food_pref):
    score = 0

    # Budget match
    if details["budget"] <= budget:
        score += 3

    # Interest match
    if details["type"] == interest:
        score += 4

    # Food match
    if food_pref in details["food"]:
        score += 2

    return score

def recommend_places(budget, interest, food_pref):
    scored_places = []

    for place, details in places.items():
        score = calculate_score(details, budget, interest, food_pref)
        scored_places.append((place, score))

    # Sort by score (highest first)
    scored_places.sort(key=lambda x: x[1], reverse=True)

    return scored_places

def show_details(place):
    details = places[place]
    print(f"\nDetails for {place}:")
    print("Type:", details["type"])
    print("Estimated Cost:", details["budget"])
    print("Food Options:", ", ".join(details["food"]))


# MAIN
if __name__ == "__main__":
    print("=== AI Travel Planner ===")

    budget = int(input("Enter your budget: "))
    interest = input("Enter your interest (beach/mountain/historical): ")
    food_pref = input("Enter food preference: ")

    results = recommend_places(budget, interest, food_pref)

    print("\nRecommended Places (Ranked):")

    for place, score in results:
        if score > 0:
            print(f"- {place} (Score: {score})")
            show_details(place)
