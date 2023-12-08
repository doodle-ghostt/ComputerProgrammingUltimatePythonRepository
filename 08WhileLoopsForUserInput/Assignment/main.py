import random
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
    
vending_machine()
        
def hangman():
    word = input("Player 1 please input a word: ")
    guess = ""
    show = " "
    print("".center(len(word), "_"))
    while guess != word:
        print("guess a letter(l) or guess a word(w)?")
        if input() == "l":
            guess = input()
            if guess in word:
