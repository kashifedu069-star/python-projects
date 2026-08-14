import random

words=["python","computer","program","school","keyboard"]

word=random.choice(words)

display=["_"]*len(word)

wrong_guesses=0

guessed_letters=[]

print("================================")
print("HANGMAN GAME")
print("================================")

print("Guess the word one letter at a time.")
print("You can make a maximum of 6 wrong guesses.\n")

while wrong_guesses<6 and "_" in display:

    print("Word:"," ".join(display))
    print("Wrong guesses:",wrong_guesses,"/ 6")

    guess=input("Enter a letter:").lower()

    if len(guess)!=1 or not guess.isalpha():
        print("Please enter only one letter.\n")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter.\n")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print("Correct guess!")

        for i in range(len(word)):
            if word[i]==guess:
                display[i]=guess
    else:
        wrong_guesses+=1
        print("Wrong guess!")

    print()

if "_" not in display:
    print("================================")
    print("Congratulations! You won!")
    print("The word was:",word)
    print("================================")
else:
    print("================================")
    print("Game Over!")
    print("The word was:",word)
    print("================================")