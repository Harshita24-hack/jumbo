import random

words = {
    3: ["cat", "dog", "sun", "Map", "Box", "Pen", "Sky", "Ice", "Fun"],
    4: ["bird", "code", "game", "Love", "Tree", "Book", "Star", "Home", "Fire", "Wind", "Rain", "Hope"],
    5: ["apple", "basic", "cloud", "Smile", "Dream", "Light", "Peace", "Heart", "Bread", "Laugh", "Music", "Plant"],
    6: ["banana", "coffee", "fables", "Friend", "Nature", "Beauty", "Castle", "Spirit", "Animal", "Bright", "Silver", "Flower", "Future"]
}

def jumble_word(word):
    return ''.join(random.sample(word, len(word)))

while True:
    try:
        n = int(input("Enter word length (3-6) or 0 to quit: "))
        if n == 0:
            print("Thanks for playing! Goodbye.")
            break
        if n not in words:
            print("Please enter a valid number between 3 and 6.")
            continue

        word = random.choice(words[n])
        jumbled = jumble_word(word)

        print(f"Unscramble: {jumbled}")
        answer = input("Enter answer (or type 'exit' to quit): ").strip()

        if answer.lower() == 'exit':
            print("Thanks for playing! Goodbye.")
            break

        if answer.lower() == word.lower():
            print("Correct!\n")
        else:
            print(f"Sorry, correct answer was {word}.\n")

    except ValueError:
        print("Please enter a valid integer.\n")
