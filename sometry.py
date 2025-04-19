import json

with open("character_sample_20.json") as f:
    database = json.load(f)

questions = [
    ("Is your character human?", "human"),
    ("Is your character a YouTuber?", "youtuber"),
    ("Has your character appeared in a movie?", "movie"),
    ("Is your character an original (real-life) person?", "original"),
    ("Is your character an inventor?", "inventor"),
    ("Is your character Indian?", "indian"),
    ("Is your character a superhero?", "superhero"),
    ("Is your character real?", "real"),
    ("Is your character a musician?", "musician"),
    ("Is your character from a cartoon?", "cartoon"),
    ("Is your character an athlete?", "sports"),
    ("Is your character animated?", "animated")
]

def play_game():
    print(" Welcome to Shruti's Mini Akinator Game!")
    print("Think of one of these characters:")
    for idx, char in enumerate(database, 1):
        print(f"{idx}. {char['name']}")
    print("\nAnswer the following questions with 0 (No) or 1 (Yes):")

    candidates = database.copy()

    for question_text, key in questions:
        while True:
            try:
                ans = int(input(f"{question_text} (0/1): "))
                if ans not in [0, 1]:
                    raise ValueError
                break
            except ValueError:
                print("Invalid input. Please enter 0 or 1.")
        ans = bool(ans)
        candidates = [c for c in candidates if c[key] == ans]

        if len(candidates) == 1:
            print(f"\n I got it! You're thinking of **{candidates[0]['name']}**!")
            return
        elif len(candidates) == 0:
            print("\n No matching character found. Maybe try again or add more characters!")
            return

    if len(candidates) > 1:
        print("\n I couldn’t narrow it down to one. Here are some possible matches:")
        for c in candidates:
            print(f" - {c['name']}")

# Run the game
play_game()
