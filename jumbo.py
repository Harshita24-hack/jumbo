
import random

words = {
    3: ["cat", "dog", "sun","Map","Box","Pen","Sky","Ice","Fun"],
    4: ["bird", "code", "game","Love", "Tree", "Book", "Star", "Home", "Fire", "Wind", "Rain", "Hope"],
    5: ["apple", "basic", "cloud","Smile", "Dream", "Light", "Peace", "Heart", "Bread", "Laugh", "Music", "Plant"],
    6: ["banana", "coffee", "fables","Friend", "Nature", "Beauty", "Castle", "Spirit", "Animal", "Bright", "Silver", "Flower", "Future"]
}

def jumble_word(word):
    return ''.join(random.sample(word, len(word)))

n = int(input("Enter word length (3-6): "))
word = random.choice(words[n])
jumbled = jumble_word(word)

print(f"Unscramble: {jumbled}")
answer = input("Enter answer: ")

if answer.lower() == word:
    print("Correct!")
else:
    print(f"Sorry, correct answer was {word}.")

