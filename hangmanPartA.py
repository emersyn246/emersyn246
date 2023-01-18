"""
File: Project 2 Part A
Author: Emersyn McGrath
Description: Plays a game of hangman.
"""
import random, os, sys

def getWords():
    """
    This function rads the words from the file and creats a dictionary where
    the keys is the length of the words and the items are the words.
    """
    words = {}
    with open(os.path.join(sys.path[0], 'dictionary.txt'), 'r') as file:
        for line in file:
            word = line.strip()
            if len(word) not in words:
                words[len(words)] = [word]
            else:
                words[len(word)].append(word)
    return words

def allowedLength(words):
    """
    This function will return a set of the allowed word lengths
    """
    allowedWords = set()
    for key in words:
        allowedWords.add(key)
    return allowedWords

def getUserInput(allowedWords):
    """
    This function will get the user input and check if it is valid
    """
    while True:
        try:
            length = int(input("Please enter the length of a word: "))
            if length in allowedWords:
                return length
            else:
                print("Sorry, but our dictionary doesn't have words the length of 26 or 27")
        except ValueError:
            print("Please enter a number between 1 and 29.")

def getRandomWord(words, length):
    """
    This function will return a random word from the dictionary
    """
    answer = random.choice(words[length])
    return answer

def playHangman(words):
    """
    This function with play the game
    """
    allowedWords = allowedLength(words)
    length = getUserInput(allowedWords)
    answer = getRandomWord(words, length)
    guessWord = ["-"]*len(answer)
    alreadyGuessed = []
    allowedGuesses = int(input("How many guesses would you like? "))

    while allowedGuesses > 0:
        if guessWord == list(answer):
            print("Congrats! You Win!")
            break
        guess = input("Enter a letter to see if it's in the word: ")
        alreadyGuessed.append(guess)
        print(alreadyGuessed)
        print("\n")
        if guess in answer:
            for idx, char in enumerate(answer):
                if char == guess:
                    guessWord[idx] = char
            print(' '.join(guessWord)+"\n")
        else:
            print(' '.join(guessWord)+"\n")
        allowedGuesses -= 1
        print("Guesses left: ", allowedGuesses)
        print("\n")
    else:
        print("Sorry, you lose. The answer was ", answer)

def main():
    print("Hello! Are you ready to play hangman?")
    words = getWords()
    print("The computer will pick a word for you.")
    playHangman(words)
    
main()
