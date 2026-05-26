
items = {
    "technology": [
        {"name": "Python Programming", "rating": 4.8},
        {"name": "Artificial Intelligence", "rating": 4.9},
        {"name": "Web Development", "rating": 4.7}
    ],

    "sports": [
        {"name": "Football Training", "rating": 4.6},
        {"name": "Cricket Academy", "rating": 4.8},
        {"name": "Fitness Coaching", "rating": 4.5}
    ],

    "music": [
        {"name": "Guitar Classes", "rating": 4.7},
        {"name": "Music Production", "rating": 4.8},
        {"name": "Piano Lessons", "rating": 4.6}
    ],

    "movies": [
        {"name": "Sci-Fi Collection", "rating": 4.9},
        {"name": "Action Movies", "rating": 4.8},
        {"name": "Comedy Shows", "rating": 4.5}
    ],

    "books": [
        {"name": "Atomic Habits", "rating": 4.9},
        {"name": "Deep Work", "rating": 4.8},
        {"name": "Think and Grow Rich", "rating": 4.7}
    ]
}


# Function → Similarity Matching
def calculate_score(category, user_choices):

    score = 0

    for choice in user_choices:

        if choice == category:
            score += 3

        elif choice[0] == category[0]:
            score += 1

    return score


print("\n=================================")
print(" AI RECOMMENDATION SYSTEM ")
print("=================================\n")

print("Available Interests:")
for category in items:
    print("-", category)

# User Input
user_input = input(
    "\nEnter interests (comma separated): "
).lower()

preferences = [
    x.strip()
    for x in user_input.split(",")
]


# User Rating
importance = int(
    input(
        "\nRate preference importance (1–5): "
    )
)


# Calculate Similarity
scores = {}

for category in items:

    scores[category] = (
        calculate_score(
            category,
            preferences
        ) * importance
    )


# Sort Categories
recommended = sorted(
    scores.items(),
    key=lambda x: x[1],
    reverse=True
)


print("\n========== RESULTS ==========")

found = False

for category, score in recommended:

    if score > 0:

        found = True

        print("\nCategory:", category)
        print("Similarity Score:", score)

        category_items = sorted(
            items[category],
            key=lambda x: x["rating"],
            reverse=True
        )

        print("Recommended Items:")

        for item in category_items:

            print(
                "-",
                item["name"],
                "| Rating:",
                item["rating"]
            )


if not found:

    print(
        "No recommendation found."
    )


print("\n========== END ==========")