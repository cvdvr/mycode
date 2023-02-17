#!/usr/bin/env python3

# challenge to make me smarter

challenge= ["science", "turbo", ["goggles", "eyes"], "nothing"]


trial= ["science", "turbo", {"eyes": "goggles", "goggles": "eyes"}, "nothing"]


nightmare= [{"slappy": "a", "text": "b", "kumquat": "goggles", "user":{"awesome": "c", "name": {"first": "eyes", "last": "toes"}},"banana": 15, "d": "nothing"}]

e= challenge[2][1]
g= challenge[2][0]
n=challenge[3]

print(f"My {e}! The {g} do {n}!")

e= trial[2]['goggles']
g= trial[2]['eyes']
n= trial[3][3]

e= challenge[2][1]
g= challenge[2][0]
n= challenge[3]

e= nightmare[4]['name']['first']
g= nightmare[0]['kumquat']
n= nightmare[2]['d']
