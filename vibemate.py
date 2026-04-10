print("====================================")
print("            VIBEMATE")
print("====================================")
print("Your personal vibe assistant.")
print()

# Mood messages
happy_message = "You sound bright today. Let's keep that energy going."
sad_message = "Let's find something comforting for your day."
stressed_message = "You deserve something calming and easy."
hype_message = "Big energy. Time to match it."
chill_message = "Let's keep things smooth and peaceful."
curious_message = "You want something interesting today."
lonely_message = "Let's find something that feels like good company."
romantic_message = "Soft, sweet, and thoughtful fits today."
spooky_message = "A darker vibe sounds perfect right now."
motivated_message = "You're locked in today. Let's feed that drive."

# Advice tuples
happy_advice = ("Share the good mood with somebody.", "Use today's energy to start something fun.", "Take a picture of one good moment today.")
sad_advice = ("Be gentle with yourself today.", "Pick one comforting thing and enjoy it slowly.", "Rest is still progress.")
stressed_advice = ("Take a few deep breaths before your next task.", "Do one thing at a time today.", "A short break can help more than forcing it.")
hype_advice = ("Use that energy on something exciting.", "Turn your hype into momentum.", "This is a good day to do something bold.")
chill_advice = ("Protect your peace today.", "Keep your schedule simple if you can.", "A quiet moment can reset a lot.")
curious_advice = ("Follow a question that interests you today.", "Try one new thing, even if it's small.", "Let yourself explore something different.")
lonely_advice = ("Do something kind for yourself today.", "Reach out if you want connection.", "Good company can also come from a favorite story.")
romantic_advice = ("Lean into softness today.", "Do something thoughtful for yourself or someone else.", "Small sweet moments count.")
spooky_advice = ("Set the mood and enjoy the atmosphere.", "A dark vibe can still be fun and cozy.", "Let today feel cinematic.")
motivated_advice = ("Use today's focus on one real goal.", "Start before you feel fully ready.", "Momentum grows when you keep moving.")

# Science facts
science_facts = (
    "Octopuses have three hearts.",
    "Bananas are berries, but strawberries are not.",
    "Honey can last for years without spoiling.",
    "Sharks existed before trees.",
    "Your brain uses electricity to send messages through your body."
)

# Music tuples
happy_music = ("Pharrell - Happy", "Bruno Mars - Treasure", "Earth, Wind & Fire - September")
sad_music = ("Adele - Easy On Me", "Joji - Glimpse of Us", "Billie Eilish - What Was I Made For?")
stressed_music = ("lofi hip hop radio", "SZA - Good Days", "Frank Ocean - Pink + White")
hype_music = ("Eminem - Till I Collapse", "DMX - X Gon' Give It To Ya", "Kendrick Lamar - HUMBLE.")
chill_music = ("Daniel Caesar - Japanese Denim", "Snoh Aalegra - I Want You Around", "Sade - By Your Side")
curious_music = ("Gorillaz - Feel Good Inc.", "Childish Gambino - Redbone", "Tyler, The Creator - See You Again")
lonely_music = ("Drake - Marvin's Room", "Sam Smith - Stay With Me", "Joji - Slow Dancing in the Dark")
romantic_music = ("Daniel Caesar - Best Part", "John Legend - All of Me", "Sade - No Ordinary Love")
spooky_music = ("Michael Jackson - Thriller", "The Weeknd - The Hills", "Billie Eilish - bury a friend")
motivated_music = ("Fort Minor - Remember the Name", "Kanye West - Stronger", "Meek Mill - Dreams and Nightmares")

# Movie tuples
happy_movies = ("Spider-Man: Into the Spider-Verse", "The Super Mario Bros. Movie", "Paddington 2")
sad_movies = ("A Silent Voice", "The Fault in Our Stars", "Inside Out")
stressed_movies = ("My Neighbor Totoro", "Chef", "Kiki's Delivery Service")
hype_movies = ("Mad Max: Fury Road", "Creed", "John Wick")
chill_movies = ("The Secret Life of Walter Mitty", "Before Sunrise", "School of Rock")
curious_movies = ("Interstellar", "Knives Out", "Everything Everywhere All at Once")
lonely_movies = ("Her", "Perks of Being a Wallflower", "Soul")
romantic_movies = ("La La Land", "Pride and Prejudice", "Crazy Rich Asians")
spooky_movies = ("Get Out", "A Quiet Place", "Train to Busan")
motivated_movies = ("Rocky", "The Pursuit of Happyness", "Whiplash")

# Game tuples
happy_games = ("Mario Kart 8 Deluxe", "Animal Crossing: New Horizons", "Fall Guys")
sad_games = ("GRIS", "Journey", "Spiritfarer")
stressed_games = ("Unpacking", "Stardew Valley", "Tetris Effect")
hype_games = ("DOOM Eternal", "Tekken 8", "Call of Duty")
chill_games = ("Minecraft", "The Sims 4", "Stardew Valley")
curious_games = ("Portal 2", "Outer Wilds", "The Witness")
lonely_games = ("Coffee Talk", "Spiritfarer", "A Short Hike")
romantic_games = ("It Takes Two", "Florence", "Life is Strange")
spooky_games = ("Resident Evil 4", "Little Nightmares", "Dead by Daylight")
motivated_games = ("Hades", "Celeste", "Street Fighter 6")

# Food tuples
happy_food = ("pizza", "ice cream", "fruit smoothie")
sad_food = ("mac and cheese", "hot chocolate", "tomato soup")
stressed_food = ("ramen", "green tea", "grilled cheese")
hype_food = ("buffalo wings", "loaded fries", "spicy tacos")
chill_food = ("sushi", "boba tea", "pasta")
curious_food = ("dumplings", "bibimbap", "street tacos")
lonely_food = ("instant ramen", "toast", "tea and cookies")
romantic_food = ("cheesecake", "strawberries", "alfredo pasta")
spooky_food = ("blackberry pie", "dark chocolate", "spicy noodles")
motivated_food = ("protein bowl", "grilled chicken wrap", "banana and peanut butter")

# Activity tuples
solo_activities = ("go on a walk with headphones", "watch a movie and make your favorite snack", "journal for 10 minutes")
social_activities = ("text a friend to hang out", "play a game with someone", "go get food with a friend")
spooky_activities = ("watch a horror movie with the lights low", "play a spooky game", "make a creepy playlist for a night drive")
calm_activities = ("read for 20 minutes", "take a quiet walk", "stretch and listen to soft music")
energy_activities = ("hit the gym", "dance to a playlist", "start a challenge in a game")


def get_message(mood):
    if mood == "happy":
        return happy_message
    elif mood == "sad":
        return sad_message
    elif mood == "stressed":
        return stressed_message
    elif mood == "hype":
        return hype_message
    elif mood == "chill":
        return chill_message
    elif mood == "curious":
        return curious_message
    elif mood == "lonely":
        return lonely_message
    elif mood == "romantic":
        return romantic_message
    elif mood == "spooky":
        return spooky_message
    elif mood == "motivated":
        return motivated_message
    return "Let's find your vibe."


def get_advice(mood):
    if mood == "happy":
        return happy_advice[0]
    elif mood == "sad":
        return sad_advice[0]
    elif mood == "stressed":
        return stressed_advice[0]
    elif mood == "hype":
        return hype_advice[0]
    elif mood == "chill":
        return chill_advice[0]
    elif mood == "curious":
        return curious_advice[0]
    elif mood == "lonely":
        return lonely_advice[0]
    elif mood == "romantic":
        return romantic_advice[0]
    elif mood == "spooky":
        return spooky_advice[0]
    elif mood == "motivated":
        return motivated_advice[0]
    return "Take care of yourself today."


def get_music_pick(mood, favorite_music):
    if mood == "happy":
        return happy_music[0]
    elif mood == "sad":
        return sad_music[0]
    elif mood == "stressed":
        return stressed_music[0]
    elif mood == "hype":
        return hype_music[0]
    elif mood == "chill":
        return chill_music[0]
    elif mood == "curious":
        return curious_music[0]
    elif mood == "lonely":
        return lonely_music[0]
    elif mood == "romantic":
        return romantic_music[0]
    elif mood == "spooky":
        return spooky_music[0]
    elif mood == "motivated":
        return motivated_music[0]
    return favorite_music


def get_movie_pick(mood, favorite_movie_genre):
    if mood == "happy":
        return happy_movies[0]
    elif mood == "sad":
        return sad_movies[0]
    elif mood == "stressed":
        return stressed_movies[0]
    elif mood == "hype":
        return hype_movies[0]
    elif mood == "chill":
        return chill_movies[0]
    elif mood == "curious":
        return curious_movies[0]
    elif mood == "lonely":
        return lonely_movies[0]
    elif mood == "romantic":
        return romantic_movies[0]
    elif mood == "spooky":
        return spooky_movies[0]
    elif mood == "motivated":
        return motivated_movies[0]
    return favorite_movie_genre


def get_game_pick(mood, favorite_game_genre):
    if mood == "happy":
        return happy_games[0]
    elif mood == "sad":
        return sad_games[0]
    elif mood == "stressed":
        return stressed_games[0]
    elif mood == "hype":
        return hype_games[0]
    elif mood == "chill":
        return chill_games[0]
    elif mood == "curious":
        return curious_games[0]
    elif mood == "lonely":
        return lonely_games[0]
    elif mood == "romantic":
        return romantic_games[0]
    elif mood == "spooky":
        return spooky_games[0]
    elif mood == "motivated":
        return motivated_games[0]
    return favorite_game_genre


def get_food_pick(mood, favorite_food):
    if mood == "happy":
        return favorite_food + " or " + happy_food[0]
    elif mood == "sad":
        return favorite_food + " or " + sad_food[0]
    elif mood == "stressed":
        return favorite_food + " or " + stressed_food[0]
    elif mood == "hype":
        return favorite_food + " or " + hype_food[0]
    elif mood == "chill":
        return favorite_food + " or " + chill_food[0]
    elif mood == "curious":
        return favorite_food + " or " + curious_food[0]
    elif mood == "lonely":
        return favorite_food + " or " + lonely_food[0]
    elif mood == "romantic":
        return favorite_food + " or " + romantic_food[0]
    elif mood == "spooky":
        return favorite_food + " or " + spooky_food[0]
    elif mood == "motivated":
        return favorite_food + " or " + motivated_food[0]
    return favorite_food


def get_activity_pick(mood, favorite_activity, social_style):
    if mood == "spooky":
        return spooky_activities[0]
    elif mood == "stressed" or mood == "chill":
        return calm_activities[0]
    elif mood == "hype" or mood == "motivated":
        return energy_activities[0]
    elif social_style == "social":
        return favorite_activity + " or " + social_activities[0]
    return favorite_activity + " or " + solo_activities[0]


def show_profile(name, favorite_food, favorite_movie_genre, favorite_game_genre, favorite_music, favorite_activity, social_style):
    print()
    print("Your VibeMate profile:")
    print("------------------------------------")
    print("Name:", name)
    print("Favorite food:", favorite_food)
    print("Favorite movie genre:", favorite_movie_genre)
    print("Favorite game genre:", favorite_game_genre)
    print("Favorite music:", favorite_music)
    print("Favorite activity:", favorite_activity)
    print("Activity style:", social_style)
    print("------------------------------------")


print("Let's build your profile first.")
name = input("What is your name? ").strip()
favorite_food = input("What is one of your favorite foods? ").strip()
favorite_movie_genre = input("What movie genre do you love most? ").strip()
favorite_game_genre = input("What game genre do you love most? ").strip()
favorite_music = input("What kind of music do you love? ").strip()
favorite_activity = input("What is one activity you enjoy? ").strip()
social_style = input("Do you prefer solo or social activities? ").strip().lower()

running = True

while running:
    print()
    print("Main menu")
    print("1. Daily check-in")
    print("2. View profile")
    print("3. Quit")
    choice = input("Choose 1, 2, or 3: ").strip()

    if choice == "1":
        print()
        print("Moods: happy, sad, stressed, hype, chill, curious, lonely, romantic, spooky, motivated")
        mood = input("How are you feeling today? ").strip().lower()
        print()
        print(get_message(mood))
        print("------------------------------------")
        print("Today's vibe for", name + ":")
        print("Music:", get_music_pick(mood, favorite_music))
        print("Movie:", get_movie_pick(mood, favorite_movie_genre))
        print("Game:", get_game_pick(mood, favorite_game_genre))
        print("Food:", get_food_pick(mood, favorite_food))
        print("Activity:", get_activity_pick(mood, favorite_activity, social_style))
        print("Advice:", get_advice(mood))
        print("Fun fact:", science_facts[0])
        print("------------------------------------")
    elif choice == "2":
        show_profile(name, favorite_food, favorite_movie_genre, favorite_game_genre, favorite_music, favorite_activity, social_style)
    elif choice == "3":
        running = False
        print()
        print("Thanks for using VibeMate.")
        print("See you next check-in.")
    else:
        print()
        print("Please choose 1, 2, or 3.")
