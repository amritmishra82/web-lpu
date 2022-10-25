#Rock Paper & Scissors
import random
print("Welcome to the game")
uC = input("Enter either rock or paper or scissors")
cC = ["rock", "paper","scissors"]
cS = random.choice(cC)
print(f"\n user choice is {uC} and computer choice is {cS} \n")
if uC == "rock" and cS == "paper":
   print("you lost")
if uC == ""