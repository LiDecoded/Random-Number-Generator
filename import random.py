import random

Name = input("Enter your name : ")

GameNumber = random.randrange(0, 10)



print ("Hello ", Name , " Welcome to the game, enter a number to guess  ")

GuessNumber = int(input())

while GuessNumber != GameNumber: 

    if GuessNumber > GameNumber: 
            print ("Guess lower :")
            GuessNumber = int(input())
    
    if GuessNumber < GameNumber:
            print("Guess higher : ")
            GuessNumber = int(input()) 

while GuessNumber == GameNumber:  
        print("Congradulations you guessed Number")
        Stop = input()
       

