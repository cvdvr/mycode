#!/usr/bin/python3

# parse keystone.common.wsgi and return number of successful login attempts
loginsuccess = 0 # counter for success

# open the file for reading
with open("/home/student/mycode/attemptlogin/keystone.common.wsgi") as kfile:

    # loop over the file
    for line in kfile:
        # if this 'success pattern' appears in the line...
        if "- - - - -] GET" in line:
            loginsuccess += 1 
        elif "- - - - -] POST" in line:
            loginsuccess+= 1

print("The number of successful log in attempts is", loginsuccess)

