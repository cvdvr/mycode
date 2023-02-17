#!/usr/bin/env python3

#dracula.txt

with open("dracula.txt","r") as foo:
    for line in foo:
        if "vampire"in line.lower():
            print(line)
            
#adding a count for vampire

with open("dracula.txt", "r") as foo:
    count= 0
    for line in foo:
        if "vampire" in line.lower():
            count += 1

    print(count)

#new file
with open("dracula.txt", "r") as foo:
    with open("vampytimes.txt", "w") as fang:
        for line in foo:
            if "vampire" in line.lower():
                fang.write(line)
