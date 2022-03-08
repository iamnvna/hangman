import random
import string

from words import words


def valid_word():
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)
    
    return word


def hangman():
    word = valid_word()
    length = len(word)
    word_letters = set(word)
    used_letters = set()
    alphabet = set(string.ascii_uppercase)
    print(f"Your word is {length} characters."
          f"\nStart guessing!")
    
    while len(word_letters) > 0:
        print("You have used these letters: ", ' '.join(used_letters))
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print("Current word: ", ' '.join(word_list))
        user_guess = input("Guess a letter: ").upper()
        if user_guess in alphabet - used_letters:
            used_letters.add(user_guess)
            if user_guess in word_letters:
                word_letters.remove(user_guess)
        
        elif user_guess in used_letters:
            print("You've guessed this letter. Try again!")
        
        else:
            print("Invalid guess. Try again!")

hangman()
