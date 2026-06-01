# AI Recommendation System

print("AI Recommendation System")

# Item database with tags
items = {
    "Python Programming Course": ["python", "coding", "programming", "ai"],
    "Artificial Intelligence Course": ["ai", "machine learning", "python"],
    "Cricket Highlights": ["cricket", "sports", "game"],
    "Football Match": ["football", "sports", "game"],
    "Action Movie": ["action", "movie", "entertainment"],
    "Comedy Movie": ["comedy", "movie", "fun"],
    "Pop Music Playlist": ["music", "pop", "songs"],
    "Classical Music Collection": ["music", "classical", "songs"],
    "Data Science Course": ["data science", "python", "analytics"]
}

# User input
user_input = input("Enter your interests separated by commas: ")

# Convert input into a list
user_preferences = [interest.strip().lower() for interest in user_input.split(",")]

recommendations = []

# Calculate similarity score
for item, tags in items.items():
    score = 0

    for preference in user_preferences:
        if preference in tags:
            score += 1

    if score > 0:
        recommendations.append((item, score))

# Sort by score (highest first)
recommendations.sort(key=lambda x: x[1], reverse=True)

# Display results
print("\nRecommended Items:")

if recommendations:
    for item, score in recommendations:
        print(f"{item} --> Match Score: {score}")
else:
    print("No matching recommendations found.")