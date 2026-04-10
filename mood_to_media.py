print("====================================")
print("         MOOD TO MEDIA MIX")
print("====================================")
print("Get recommendations for anime, music, games, books, and food.")
print()

# Mood recommendation tuples
happy_music = ("Pharrell - Happy", "Bruno Mars - Treasure", "Justin Timberlake - Can't Stop the Feeling")
happy_games = ("Mario Kart 8 Deluxe", "Animal Crossing: New Horizons", "Fall Guys")
happy_anime = ("Spy x Family", "Haikyuu!!", "One Punch Man")
happy_books = ("The Little Prince", "Percy Jackson and the Lightning Thief", "The House in the Cerulean Sea")
happy_food = ("ice cream", "pizza", "fruit smoothie")

sad_music = ("Adele - Someone Like You", "Billie Eilish - when the party's over", "Lewis Capaldi - Before You Go")
sad_games = ("GRIS", "Spiritfarer", "Journey")
sad_anime = ("Your Lie in April", "A Silent Voice", "Anohana")
sad_books = ("The Fault in Our Stars", "A Monster Calls", "They Both Die at the End")
sad_food = ("tomato soup", "hot tea", "mac and cheese")

hype_music = ("Kendrick Lamar - HUMBLE.", "Eminem - Till I Collapse", "DMX - X Gon' Give It To Ya")
hype_games = ("DOOM Eternal", "Tekken 8", "Call of Duty")
hype_anime = ("Jujutsu Kaisen", "Blue Lock", "Demon Slayer")
hype_books = ("Red Rising", "The Hunger Games", "Legend")
hype_food = ("buffalo wings", "loaded fries", "energy drink")

chill_music = ("SZA - Snooze", "Frank Ocean - Pink + White", "lofi hip hop radio")
chill_games = ("Stardew Valley", "Minecraft", "Unpacking")
chill_anime = ("Mushishi", "Barakamon", "Natsume's Book of Friends")
chill_books = ("Before the Coffee Gets Cold", "The Alchemist", "The Midnight Library")
chill_food = ("ramen", "green tea", "sushi")

dark_music = ("The Weeknd - The Hills", "Kanye West - Black Skinhead", "Nine Inch Nails - Closer")
dark_games = ("Resident Evil 4", "Bloodborne", "Little Nightmares")
dark_anime = ("Death Note", "Parasyte", "Tokyo Ghoul")
dark_books = ("1984", "No Longer Human", "The Picture of Dorian Gray")
dark_food = ("black coffee", "dark chocolate", "spicy noodles")

romantic_music = ("Daniel Caesar - Best Part", "John Legend - All of Me", "Sade - By Your Side")
romantic_games = ("It Takes Two", "Florence", "Life is Strange")
romantic_anime = ("Kimi ni Todoke", "Horimiya", "Fruits Basket")
romantic_books = ("Pride and Prejudice", "The Sun Is Also a Star", "Book Lovers")
romantic_food = ("strawberries", "pasta", "cheesecake")

motivated_music = ("Kanye West - Stronger", "Meek Mill - Dreams and Nightmares", "Fort Minor - Remember the Name")
motivated_games = ("Hades", "Celeste", "Street Fighter 6")
motivated_anime = ("Naruto", "Black Clover", "My Hero Academia")
motivated_books = ("Atomic Habits", "The 7 Habits of Highly Effective People", "The Mountain Is You")
motivated_food = ("protein bowl", "grilled chicken wrap", "banana and peanut butter")

nostalgic_music = ("OutKast - Hey Ya!", "Usher - U Got It Bad", "Alicia Keys - If I Ain't Got You")
nostalgic_games = ("Pokemon Emerald", "Kingdom Hearts", "Super Smash Bros. Melee")
nostalgic_anime = ("Dragon Ball Z", "Yu Yu Hakusho", "Inuyasha")
nostalgic_books = ("Charlotte's Web", "Harry Potter and the Sorcerer's Stone", "Matilda")
nostalgic_food = ("grilled cheese", "cereal", "chicken nuggets")

lonely_music = ("Drake - Marvin's Room", "Joji - Slow Dancing in the Dark", "Sam Smith - Too Good at Goodbyes")
lonely_games = ("Coffee Talk", "Spiritfarer", "The Sims 4")
lonely_anime = ("Welcome to the N.H.K.", "Orange", "March Comes in Like a Lion")
lonely_books = ("Eleanor Oliphant Is Completely Fine", "The Perks of Being a Wallflower", "Norwegian Wood")
lonely_food = ("instant ramen", "toast", "hot chocolate")

curious_music = ("Childish Gambino - Redbone", "Gorillaz - Feel Good Inc.", "Tyler, The Creator - See You Again")
curious_games = ("Portal 2", "Outer Wilds", "The Witness")
curious_anime = ("Steins;Gate", "Dr. Stone", "Erased")
curious_books = ("The Martian", "Sapiens", "The Hitchhiker's Guide to the Galaxy")
curious_food = ("dumplings", "boba tea", "bibimbap")


def show_moods():
    print()
    print("Available moods:")
    print("happy, sad, hype, chill, dark")
    print("romantic, motivated, nostalgic, lonely, curious")


def show_categories():
    print()
    print("Available categories:")
    print("music, games, anime, books, food, all")


def show_vibe_message(mood):
    print()
    if mood == "happy":
        print("You're giving bright energy today. Let's match that vibe.")
    elif mood == "sad":
        print("Looks like you need something comforting today.")
    elif mood == "hype":
        print("Big energy today. Time for something intense.")
    elif mood == "chill":
        print("You're in a calm lane today. Let's keep it smooth.")
    elif mood == "dark":
        print("You want something intense, moody, or a little dangerous.")
    elif mood == "romantic":
        print("Soft feelings are in the air today.")
    elif mood == "motivated":
        print("You're locked in. Let's feed that drive.")
    elif mood == "nostalgic":
        print("You're in a throwback kind of mood today.")
    elif mood == "lonely":
        print("Let's find something that keeps you company.")
    elif mood == "curious":
        print("You want something interesting and different today.")


def get_recommendations(mood, category):
    if mood == "happy":
        if category == "music":
            return happy_music
        elif category == "games":
            return happy_games
        elif category == "anime":
            return happy_anime
        elif category == "books":
            return happy_books
        elif category == "food":
            return happy_food
        elif category == "all":
            return ()
    elif mood == "sad":
        if category == "music":
            return sad_music
        elif category == "games":
            return sad_games
        elif category == "anime":
            return sad_anime
        elif category == "books":
            return sad_books
        elif category == "food":
            return sad_food
        elif category == "all":
            return ()
    elif mood == "hype":
        if category == "music":
            return hype_music
        elif category == "games":
            return hype_games
        elif category == "anime":
            return hype_anime
        elif category == "books":
            return hype_books
        elif category == "food":
            return hype_food
        elif category == "all":
            return ()
    elif mood == "chill":
        if category == "music":
            return chill_music
        elif category == "games":
            return chill_games
        elif category == "anime":
            return chill_anime
        elif category == "books":
            return chill_books
        elif category == "food":
            return chill_food
        elif category == "all":
            return ()
    elif mood == "dark":
        if category == "music":
            return dark_music
        elif category == "games":
            return dark_games
        elif category == "anime":
            return dark_anime
        elif category == "books":
            return dark_books
        elif category == "food":
            return dark_food
        elif category == "all":
            return ()
    elif mood == "romantic":
        if category == "music":
            return romantic_music
        elif category == "games":
            return romantic_games
        elif category == "anime":
            return romantic_anime
        elif category == "books":
            return romantic_books
        elif category == "food":
            return romantic_food
        elif category == "all":
            return ()
    elif mood == "motivated":
        if category == "music":
            return motivated_music
        elif category == "games":
            return motivated_games
        elif category == "anime":
            return motivated_anime
        elif category == "books":
            return motivated_books
        elif category == "food":
            return motivated_food
        elif category == "all":
            return ()
    elif mood == "nostalgic":
        if category == "music":
            return nostalgic_music
        elif category == "games":
            return nostalgic_games
        elif category == "anime":
            return nostalgic_anime
        elif category == "books":
            return nostalgic_books
        elif category == "food":
            return nostalgic_food
        elif category == "all":
            return ()
    elif mood == "lonely":
        if category == "music":
            return lonely_music
        elif category == "games":
            return lonely_games
        elif category == "anime":
            return lonely_anime
        elif category == "books":
            return lonely_books
        elif category == "food":
            return lonely_food
        elif category == "all":
            return ()
    elif mood == "curious":
        if category == "music":
            return curious_music
        elif category == "games":
            return curious_games
        elif category == "anime":
            return curious_anime
        elif category == "books":
            return curious_books
        elif category == "food":
            return curious_food
        elif category == "all":
            return ()

    return ()


def show_all_categories(mood):
    print("Music pick:", get_recommendations(mood, "music")[0])
    print("Game pick:", get_recommendations(mood, "games")[0])
    print("Anime pick:", get_recommendations(mood, "anime")[0])
    print("Book pick:", get_recommendations(mood, "books")[0])
    print("Food pick:", get_recommendations(mood, "food")[0])


running = True

while running:
    show_moods()
    mood = input("How are you feeling today? ").strip().lower()

    if mood != "happy" and mood != "sad" and mood != "hype" and mood != "chill" and mood != "dark" and mood != "romantic" and mood != "motivated" and mood != "nostalgic" and mood != "lonely" and mood != "curious":
        print()
        print("I don't have that mood yet. Try one from the list.")
    else:
        show_vibe_message(mood)
        show_categories()
        category = input("What do you want recommendations for? ").strip().lower()

        if category != "music" and category != "games" and category != "anime" and category != "books" and category != "food" and category != "all":
            print()
            print("That category is not available yet.")
        elif category == "all":
            print()
            print("Your recommendations:")
            print("------------------------------------")
            show_all_categories(mood)
            print("------------------------------------")
        else:
            picks = get_recommendations(mood, category)
            index = 0
            keep_category = True

            while keep_category:
                print()
                print("Your recommendation:")
                print("------------------------------------")
                print(category.title() + " pick:", picks[index])
                print("------------------------------------")

                if index < len(picks) - 1:
                    next_pick = input("Want another " + mood + " " + category + " pick? yes or no: ").strip().lower()
                    if next_pick == "yes":
                        index = index + 1
                    else:
                        keep_category = False
                else:
                    print("That was the last pick in this category for this mood.")
                    keep_category = False

    print()
    again = input("Would you like to try another mood? yes or no: ").strip().lower()
    if again == "no":
        running = False
        print()
        print("Thanks for using Mood to Media Mix.")
        print("Come back when you need a new vibe.")
