import random
import os
def number_guesser():
    number = random.randint(1, 10)
    guess = ""
    while guess != number:
        print("enter a number between 1 and 10") 
        guess = int(input())
        if guess > number:
            print("Too high")
        elif guess < number:
            print("Too low")
    if guess == number:
        print("you got it :D")



def number_guesser_with_lives():
    number = random.randint(1, 10)
    guess = ""
    lives = 3
    while guess != number and lives > 0:
        print("enter a number between 1 and 10") 
        guess = int(input())
        if guess < 1 or guess > 10:
            print("That is not a valid number >:(")
        elif guess > number:
            print("Too high")
            lives -= 1
            print("you have" , lives, "lives left")
        elif guess < number:
            print("Too low")
            lives -= 1
            print("you have" , lives, "lives left")
    if lives <= 0:
        print("You lose :(")
        print("Correct answer: ", number)
    if guess == number:
        print("you got it :D")



def vending_machine():
    charge = 50
    change = 0
    coin = ""
    while charge > 0:
        print("Amount due:", charge)
        print("Insert coin:")
        coin = int(input())
        if charge < coin and coin in [5, 10, 25]:
            change = abs(charge - coin)
            charge = 0
            print("Change owed:", change)
        elif coin in [5, 10, 25]:
            charge -= coin
    

        
def hangman():
    word = input("Player 1 please input a word: ")
    guess = ""
    board = "_" * len(word)
    board = list(board)
    lives = len(word)
    os.system('cls')
    print(str(board).replace("[", "").replace("]", "").replace("'", "").replace(",", ""))
    while lives > 0 and guess != word:
        g = input("guess a letter (l) or guess the word(w)? ")
        if g == "l":
            i = input("letter: ")
            if i not in word:
                lives -= 1
                print("You have", lives, "lives remaining")
            else:
                for char in range(0, len(word)):
                    if word[char] == i:
                        board[char] = i
            print(str(board).replace("[", "").replace("]", "").replace("'", "").replace(",", ""))
        elif g == "w":
            i = input("word: ")
            if i != word:
                lives -= 1
                print("You have", lives, "lives remaining")
            else:
                guess = word
        if "_" not in board:
                guess = word
    if lives == 0:
        print("YOU :(")
        print(word)
    if guess == word:
        print("YOU :)")
hangman()