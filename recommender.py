import pandas as pd
import random

# Load Dataset
df = pd.read_csv("tourism.csv")

def recommend_places(
    trip_type,
    budget,
    weather,
    days,
    group_type
):

    recommendations = []

    # Collect activities for fallback
    all_activities = []

    # Loop through dataset
    for index, row in df.iterrows():

        score = 0

        # ---------------- HARD FILTER (IMPORTANT FIX) ---------------- #
        # Remove completely irrelevant duration results
        if abs(row["days"] - days) > 3:
            continue

        # ---------------- TRIP TYPE MATCH ---------------- #
        if row["type"] == trip_type:
            score += 30
            all_activities.append(row["activities"])

        # ---------------- BUDGET MATCH ---------------- #
        budget_difference = abs(row["budget"] - budget)

        if budget_difference <= 10000:
            score += 20
        elif budget_difference <= 20000:
            score += 10

        # ---------------- WEATHER MATCH ---------------- #
        if row["weather"] == weather:
            score += 20

        # ---------------- DAYS MATCH (IMPROVED LOGIC) ---------------- #
        day_difference = abs(row["days"] - days)

        if day_difference == 0:
            score += 25  # perfect match
        elif day_difference == 1:
            score += 15
        elif day_difference == 2:
            score += 8
        else:
            score += 0

        # Extra boost for exact match
        if row["days"] == days:
            score += 10

        # ---------------- GROUP TYPE MATCH ---------------- #
        if row["group_type"] == group_type:
            score += 15

        # ---------------- RANDOM BONUS ---------------- #
        score += random.randint(1, 5)

        # Cap score
        if score > 100:
            score = 100

        # Save recommendation
        recommendations.append((score, row))

    # ---------------- SORT RECOMMENDATIONS ---------------- #
    recommendations.sort(key=lambda x: x[0], reverse=True)

    # ---------------- TOP RESULTS ---------------- #
    top_places = []

    for score, row in recommendations[:4]:

        row = row.copy()

        row["match_score"] = score

        # ---------------- SAFE ACTIVITIES GENERATION ---------------- #
        unique_activities = list(set(all_activities))

        if len(unique_activities) == 0:
            random_activities = [
                "Sightseeing",
                "Photography",
                "Local Food"
            ]
        else:
            random_activities = random.sample(
                unique_activities,
                min(3, len(unique_activities))
            )

        activities_text = ", ".join(random_activities)

        row["generated_activities"] = activities_text

        # ---------------- AI DESCRIPTION ---------------- #
        descriptions = [
            f"Perfect for {trip_type.lower()} lovers.",
            f"Ideal for {group_type.lower()} trips.",
            f"Suitable for {days}-day vacations.",
            "Offers memorable tourist experiences.",
            f"Includes activities like {activities_text}.",
            "One of the most recommended destinations."
        ]

        row["generated_description"] = " ".join(
            random.sample(descriptions, 4)
        )

        # ---------------- TAGS ---------------- #
        tags = []

        if trip_type == "Adventure":
            tags.extend(["Hiking", "Camping", "Exploration"])

        elif trip_type == "Nature":
            tags.extend(["Mountains", "Scenery", "Relaxation"])

        elif trip_type == "Historical":
            tags.extend(["Culture", "Museums", "History"])

        row["generated_tags"] = ", ".join(tags)

        top_places.append(row)

    # Convert to DataFrame
    result_df = pd.DataFrame(top_places)

    return result_df