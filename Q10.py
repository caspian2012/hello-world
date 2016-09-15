# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


word = list("tiger")
print("import lingo")
guess = []
while True:
    guess = list(input("Please enter your guess: "))
    if guess == word:
        print("You guessed the right word!")
        break
    else:
        cluelst = guess
        for i in range(0, len(word)):
            if guess[i] == word[i]:
                cluelst[i] = "[" + guess[i] + "]" 
        for i in range(0, len(word)):
            for j in range(0, len(word)):
                if guess[i] == word[j]:
                    cluelst[i] = "(" + guess[i] + ")"
        clue = "".join(cluelst)
        print("Clue: " + clue)
        
    