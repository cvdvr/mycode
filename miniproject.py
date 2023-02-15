#!/usr/bin/env python3

#Name game for mini project 1.

Carl=0
CarltheDog=0
CarlTheWeinerDog=0
print ("What should your name be?")
name=input("Hello, what is your name?\n")

   # because .title() will force "name" to be capitalized, you must have Trent and Carl's name capitalized... otherwise it will never match
if name.title() == "Trent": 
    CarlTheWeinerDog += 10

elif name.title() == "Carl":
    CarltheDog += 10

dog= input("Are you a weiner dog?")
if dog == "yes":
    CarlTheWeinerDog += 10
    Carl -= 5
    CarltheDog -= 5 # if you say "yes" to this question, carltheweinerdog goes up and everything else goes down

naps=input("Do you enjoy naps?\n")
if naps == "yes":
     CarlTheWeinerDog +=1

print(f"""
FINAL SCORES:
Carl: {Carl}
Carl the Dog: {CarltheDog}
Carl the Weiner Dog: {CarlTheWeinerDog}""")













