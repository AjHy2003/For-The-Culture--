import json
import os


print("====================================")
print("          VIBEMATE V3")
print("====================================")
print("Your personal vibe assistant.")
print()

PROFILE_FILE = "vibemate_profile.json"

MOODS = (
    "happy",
    "sad",
    "stressed",
    "hype",
    "chill",
    "curious",
    "lonely",
    "romantic",
    "spooky",
    "motivated"
)

VIBE_MESSAGES = {
    "happy": "You sound bright today. Let's keep that energy going.",
    "sad": "Let's find something comforting for your day.",
    "stressed": "You deserve something calming and easy.",
    "hype": "Big energy. Time to match it.",
    "chill": "Let's keep things smooth and peaceful.",
    "curious": "You want something interesting today.",
    "lonely": "Let's find something that feels like good company.",
    "romantic": "Soft, sweet, and thoughtful fits today.",
    "spooky": "A darker vibe sounds perfect right now.",
    "motivated": "You're locked in today. Let's feed that drive."
}

ADVICE = {
    "happy": (
        "Share the good mood with somebody.",
        "Use today's energy to start something fun.",
        "Take a picture of one good moment today."
    ),
    "sad": (
        "Be gentle with yourself today.",
        "Pick one comforting thing and enjoy it slowly.",
        "Rest is still progress."
    ),
    "stressed": (
        "Take a few deep breaths before your next task.",
        "Do one thing at a time today.",
        "A short break can help more than forcing it."
    ),
    "hype": (
        "Use that energy on something exciting.",
        "Turn your hype into momentum.",
        "This is a good day to do something bold."
    ),
    "chill": (
        "Protect your peace today.",
        "Keep your schedule simple if you can.",
        "A quiet moment can reset a lot."
    ),
    "curious": (
        "Follow a question that interests you today.",
        "Try one new thing, even if it's small.",
        "Let yourself explore something different."
    ),
    "lonely": (
        "Do something kind for yourself today.",
        "Reach out if you want connection.",
        "Good company can also come from a favorite story."
    ),
    "romantic": (
        "Lean into softness today.",
        "Do something thoughtful for yourself or someone else.",
        "Small sweet moments count."
    ),
    "spooky": (
        "Set the mood and enjoy the atmosphere.",
        "A dark vibe can still be fun and cozy.",
        "Let today feel cinematic."
    ),
    "motivated": (
        "Use today's focus on one real goal.",
        "Start before you feel fully ready.",
        "Momentum grows when you keep moving."
    )
}

SCIENCE_FACTS = (
    "Octopuses have three hearts.",
    "Bananas are berries, but strawberries are not.",
    "Honey can last for years without spoiling.",
    "Sharks existed before trees.",
    "Your brain uses electricity to send messages through your body."
)

RECOMMENDATIONS = {
    "happy": {
        "music": ("Pharrell - Happy", "Bruno Mars - Treasure", "Earth, Wind & Fire - September"),
        "movie": ("Spider-Man: Into the Spider-Verse", "The Super Mario Bros. Movie", "Paddington 2"),
        "game": ("Mario Kart 8 Deluxe", "Animal Crossing: New Horizons", "Fall Guys"),
        "food": ("pizza", "ice cream", "fruit smoothie")
    },
    "sad": {
        "music": ("Adele - Easy On Me", "Joji - Glimpse of Us", "Billie Eilish - What Was I Made For?"),
        "movie": ("A Silent Voice", "The Fault in Our Stars", "Inside Out"),
        "game": ("GRIS", "Journey", "Spiritfarer"),
        "food": ("mac and cheese", "hot chocolate", "tomato soup")
    },
    "stressed": {
        "music": ("lofi hip hop radio", "SZA - Good Days", "Frank Ocean - Pink + White"),
        "movie": ("My Neighbor Totoro", "Chef", "Kiki's Delivery Service"),
        "game": ("Unpacking", "Stardew Valley", "Tetris Effect"),
        "food": ("ramen", "green tea", "grilled cheese")
    },
    "hype": {
        "music": ("Eminem - Till I Collapse", "DMX - X Gon' Give It To Ya", "Kendrick Lamar - HUMBLE."),
        "movie": ("Mad Max: Fury Road", "Creed", "John Wick"),
        "game": ("DOOM Eternal", "Tekken 8", "Call of Duty"),
        "food": ("buffalo wings", "loaded fries", "spicy tacos")
    },
    "chill": {
        "music": ("Daniel Caesar - Japanese Denim", "Snoh Aalegra - I Want You Around", "Sade - By Your Side"),
        "movie": ("The Secret Life of Walter Mitty", "Before Sunrise", "School of Rock"),
        "game": ("Minecraft", "The Sims 4", "Stardew Valley"),
        "food": ("sushi", "boba tea", "pasta")
    },
    "curious": {
        "music": ("Gorillaz - Feel Good Inc.", "Childish Gambino - Redbone", "Tyler, The Creator - See You Again"),
        "movie": ("Interstellar", "Knives Out", "Everything Everywhere All at Once"),
        "game": ("Portal 2", "Outer Wilds", "The Witness"),
        "food": ("dumplings", "bibimbap", "street tacos")
    },
    "lonely": {
        "music": ("Drake - Marvin's Room", "Sam Smith - Stay With Me", "Joji - Slow Dancing in the Dark"),
        "movie": ("Her", "The Perks of Being a Wallflower", "Soul"),
        "game": ("Coffee Talk", "Spiritfarer", "A Short Hike"),
        "food": ("instant ramen", "toast", "tea and cookies")
    },
    "romantic": {
        "music": ("Daniel Caesar - Best Part", "John Legend - All of Me", "Sade - No Ordinary Love"),
        "movie": ("La La Land", "Pride and Prejudice", "Crazy Rich Asians"),
        "game": ("It Takes Two", "Florence", "Life is Strange"),
        "food": ("cheesecake", "strawberries", "alfredo pasta")
    },
    "spooky": {
        "music": ("Michael Jackson - Thriller", "The Weeknd - The Hills", "Billie Eilish - bury a friend"),
        "movie": ("Get Out", "A Quiet Place", "Train to Busan"),
        "game": ("Resident Evil 4", "Little Nightmares", "Dead by Daylight"),
        "food": ("blackberry pie", "dark chocolate", "spicy noodles")
    },
    "motivated": {
        "music": ("Fort Minor - Remember the Name", "Kanye West - Stronger", "Meek Mill - Dreams and Nightmares"),
        "movie": ("Rocky", "The Pursuit of Happyness", "Whiplash"),
        "game": ("Hades", "Celeste", "Street Fighter 6"),
        "food": ("protein bowl", "grilled chicken wrap", "banana and peanut butter")
    }
}

SOLO_ACTIVITIES = (
    "go on a walk with headphones",
    "watch a movie and make your favorite snack",
    "journal for 10 minutes"
)

SOCIAL_ACTIVITIES = (
    "text a friend to hang out",
    "play a game with someone",
    "go get food with a friend"
)

SPOOKY_ACTIVITIES = (
    "watch a horror movie with the lights low",
    "play a spooky game",
    "make a creepy playlist for a night drive"
)

CALM_ACTIVITIES = (
    "read for 20 minutes",
    "take a quiet walk",
    "stretch and listen to soft music"
)

ENERGY_ACTIVITIES = (
    "hit the gym",
    "dance to a playlist",
    "start a challenge in a game"
)


def get_next_item(items, index):
    item = items[index]
    index = index + 1
    if index >= len(items):
        index = 0
    return item, index


def load_profile():
    if os.path.exists(PROFILE_FILE):
        file = open(PROFILE_FILE, "r")
        profile = json.load(file)
        file.close()
        return profile
    return None


def save_profile(profile):
    file = open(PROFILE_FILE, "w")
    json.dump(profile, file, indent=2)
    file.close()


def build_profile():
    print("Let's build your profile first.")
    profile = {}
    profile["name"] = input("What is your name? ").strip()
    profile["favorite_food"] = input("What is one of your favorite foods? ").strip()
    profile["favorite_movie_genre"] = input("What movie genre do you love most? ").strip()
    profile["favorite_game_genre"] = input("What game genre do you love most? ").strip()
    profile["favorite_music"] = input("What kind of music do you love? ").strip()
    profile["favorite_activity"] = input("What is one activity you enjoy? ").strip()
    profile["social_style"] = input("Do you prefer solo or social activities? ").strip().lower()
    return profile


def edit_profile(profile):
    print()
    print("Edit profile")
    print("1. Name")
    print("2. Favorite food")
    print("3. Favorite movie genre")
    print("4. Favorite game genre")
    print("5. Favorite music")
    print("6. Favorite activity")
    print("7. Social style")
    print("8. Back")
    choice = input("Choose what to edit: ").strip()

    if choice == "1":
        profile["name"] = input("New name: ").strip()
    elif choice == "2":
        profile["favorite_food"] = input("New favorite food: ").strip()
    elif choice == "3":
        profile["favorite_movie_genre"] = input("New favorite movie genre: ").strip()
    elif choice == "4":
        profile["favorite_game_genre"] = input("New favorite game genre: ").strip()
    elif choice == "5":
        profile["favorite_music"] = input("New favorite music: ").strip()
    elif choice == "6":
        profile["favorite_activity"] = input("New favorite activity: ").strip()
    elif choice == "7":
        profile["social_style"] = input("New social style: ").strip().lower()
    return profile


def show_profile(profile):
    print()
    print("Your VibeMate profile:")
    print("------------------------------------")
    print("Name:", profile["name"])
    print("Favorite food:", profile["favorite_food"])
    print("Favorite movie genre:", profile["favorite_movie_genre"])
    print("Favorite game genre:", profile["favorite_game_genre"])
    print("Favorite music:", profile["favorite_music"])
    print("Favorite activity:", profile["favorite_activity"])
    print("Activity style:", profile["social_style"])
    print("------------------------------------")


def get_activity_group(mood, social_style):
    if mood == "spooky":
        return SPOOKY_ACTIVITIES, "spooky"
    if mood == "stressed" or mood == "chill":
        return CALM_ACTIVITIES, "calm"
    if mood == "hype" or mood == "motivated":
        return ENERGY_ACTIVITIES, "energy"
    if social_style == "social":
        return SOCIAL_ACTIVITIES, "social"
    return SOLO_ACTIVITIES, "solo"


def run_check_in(profile, counters):
    print()
    print("Moods:", ", ".join(MOODS))
    print("Type surprise if you want VibeMate to choose for you.")
    mood = input("How are you feeling today? ").strip().lower()

    if mood == "surprise":
        mood, counters["mood_index"] = get_next_item(MOODS, counters["mood_index"])
        print("VibeMate picked:", mood)
    elif mood not in MOODS:
        print()
        print("I don't know that mood yet.")
        return counters

    print()
    print(VIBE_MESSAGES[mood])
    print("------------------------------------")

    music_pick, counters[mood + "_music"] = get_next_item(RECOMMENDATIONS[mood]["music"], counters[mood + "_music"])
    movie_pick, counters[mood + "_movie"] = get_next_item(RECOMMENDATIONS[mood]["movie"], counters[mood + "_movie"])
    game_pick, counters[mood + "_game"] = get_next_item(RECOMMENDATIONS[mood]["game"], counters[mood + "_game"])
    food_pick, counters[mood + "_food"] = get_next_item(RECOMMENDATIONS[mood]["food"], counters[mood + "_food"])
    advice_pick, counters[mood + "_advice"] = get_next_item(ADVICE[mood], counters[mood + "_advice"])
    fact_pick, counters["fact_index"] = get_next_item(SCIENCE_FACTS, counters["fact_index"])

    activity_group, activity_key = get_activity_group(mood, profile["social_style"])
    activity_pick, counters[activity_key + "_activity"] = get_next_item(activity_group, counters[activity_key + "_activity"])

    print("Today's vibe for", profile["name"] + ":")
    print("Music:", music_pick, "| based on your love for", profile["favorite_music"])
    print("Movie:", movie_pick, "| favorite genre:", profile["favorite_movie_genre"])
    print("Game:", game_pick, "| favorite genre:", profile["favorite_game_genre"])
    print("Food:", profile["favorite_food"] + " or " + food_pick)
    print("Activity:", profile["favorite_activity"] + " or " + activity_pick)
    print("Advice:", advice_pick)
    print("Fun fact:", fact_pick)
    print("------------------------------------")
    return counters


def build_counters():
    counters = {"fact_index": 0, "mood_index": 0}
    for mood in MOODS:
        counters[mood + "_music"] = 0
        counters[mood + "_movie"] = 0
        counters[mood + "_game"] = 0
        counters[mood + "_food"] = 0
        counters[mood + "_advice"] = 0
    counters["solo_activity"] = 0
    counters["social_activity"] = 0
    counters["spooky_activity"] = 0
    counters["calm_activity"] = 0
    counters["energy_activity"] = 0
    return counters


profile = load_profile()

if profile is None:
    profile = build_profile()
    save_profile(profile)
    print()
    print("Profile saved.")
else:
    print("Welcome back,", profile["name"] + ".")

counters = build_counters()
running = True

while running:
    print()
    print("Main menu")
    print("1. Daily check-in")
    print("2. View profile")
    print("3. Edit profile")
    print("4. Quit")
    choice = input("Choose 1, 2, 3, or 4: ").strip()

    if choice == "1":
        counters = run_check_in(profile, counters)
    elif choice == "2":
        show_profile(profile)
    elif choice == "3":
        profile = edit_profile(profile)
        save_profile(profile)
        print()
        print("Profile updated.")
    elif choice == "4":
        running = False
        print()
        print("Thanks for using VibeMate V3.")
        print("See you next check-in.")
    else:
        print()
        print("Please choose 1, 2, 3, or 4.")
