#!/usr/bin/env python3

#printing peoples names

tlgfolks= ["Aaron", "Adrian", "Alex", "Tony", "Chris", "Derek", "Javier", "John", "Jonathan", "Justin", "Levi", "Rohalio", "Steven", "Taje", "Trent", "Walt"]


for eachperson in tlgfolks:
    while eachperson[0] not in "aeiou":
        eachperson= eachperson[1:]
    print(f"j{eachperson.lower()}")


