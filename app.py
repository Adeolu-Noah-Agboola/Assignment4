from flask import Flask
import random

app = Flask(__name__)

@app.route('/')
def say_hi():
    success="The file successfully ran"
    return success

with open('ranwords.txt', 'r') as f:
    words = f.readlines()


word=random.choice(words)[:-1]
allowedErrors=7
guesses=[]
done=False
while not done:
    for letter in word:
        if letter.lower() in guesses:
            print(letter, end=" ")
        else:
            print("_", end=" ")
    print("")

    guess= input(f"Allowed Errors left {allowedErrors}, Next Guess: ")
    guesses.append(guess.lower())
    if guess.lower() not in word.lower():
        allowedErrors-=1
        if allowedErrors == 0:
            break

    done= True
    for letter in word:
        if letter.lower() not in guesses:
            done = False

if done:
    print(f"You found the word! It was {word}!")
else:
    print(f"Game Over! The word was {word}")


