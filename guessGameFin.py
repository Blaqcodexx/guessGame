import numpy as np
import random as ran

#This is a number guessing game.
print("""
      ___ ABOUT GAME ___ \n 
      This is a guessing game where you are provided with an option 
      to guess the secret number(0 - 100) the AI randomly chooses. \n
      You only got (3) chances, Make it count! \n
      FYI: The chance of you getting it right is nearly impossible! \n
      ___ GOOD LUCK! ___\n 
      -----------------------------------------------------------""")

def guessGame():
    counter = 0
    tries = 3
    r = [ran.random() for i in range(100)]
    s = sum(r)
    r = [i / s for i in r]
    while counter < tries:
        counter += 1
        a = int(np.random.choice((np.arange(100)), p=(r), size=(1)))
        b = int(input("Guess your number: "))
        if (counter == 1) and (b == a):
            print("Secret number: " + str(a))
            print("Magnificent! You got it right the first time!")
            break
        elif (counter == 2) and (b == a):
            print("Secret number: " + str(a))
            print("Genius, You got it right!")
            break
        elif (counter == 3) and (b == a):
            print("Secret number: " + str(a))
            print("Finally!, You rock!")
            break
        else:
            print("Secret number: " + str(a))
            print("Whoosh!, Try again!")



guessGame()