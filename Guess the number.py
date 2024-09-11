import random
import os
minNum = random.randint(1,1000)
maxNum = random.randint(1000,1500)
ans = random.randint(minNum,maxNum)
guess = ""
guessx = 0
while guess != ans:
    if guess != "":
        if guess > ans:
            print("Smaller!")
        elif guess < ans:
            print("Bigger!")
    guess = int(input("What is the number you are guessing? "))
    guessx += 1
print("Correct! It took you",guessx,"guesses to get the number right!")
os.system("pause")