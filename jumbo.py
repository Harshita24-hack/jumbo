
import random

words = {
    3: ["cat", "dog", "sun"],
    4: ["bird", "code", "game"],
    5: ["apple", "basic", "cloud"],
    6: ["banana", "coffee", "fables"]
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
