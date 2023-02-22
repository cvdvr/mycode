#!/usr/bin/env python3
# final project for python and TLG NDE Class
import time

Geoff = 0
Carl = 0

print("Hello, who should the 22.11 CM NDE mascot be, Geoff the Ghost of AWS or Carl the Wiener Dog?")
name = input("First, what should I call you?\n")

# questions to determine if you are more like Carl or Geoff

dog1 = input("If you had a tail, would you wag it?")
if dog1 == "yes":
    Carl += 1

ghost1 = input("Have you ever pulled an Irish Goodbye?")
if ghost1 == "yes":
    Geoff += 1

dog2 = input("Are you more a dog person or cat person?")
if dog2 == "dog":
    Carl += 1
elif dog2 == "cat":
    Geoff += 1

hair = input("Is your hair wild and unkempt?")
if hair == "yes":
    Geoff += 1
elif hair == "no":
    Carl += 1

print(f"""
Final Scores:
Geoff the AWS Ghost: {Geoff}
Carl the Wiener Dog: {Carl}""")

# delay before remembering Geoff

time.sleep(3)
print("In memory of Geoff")

# pretty picture of Geoff

time.sleep(2)
print("Thanks for playing " + name)
