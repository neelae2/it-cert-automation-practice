#!/usr/bin/env python3


import re



def validate_user(username, minlen):

    """Checks if the received username matches the required conditions."""

    if minlen < 3:

        return False

    if len(username) < minlen:

        return False

    if not username.isalnum():

        return False

    if username[0].isdigit():  # Check if first character is a digit

        return False

    return True



# Test cases

print(validate_user("blue.kale", 3)) # True

print(validate_user(".blue.kale", 3)) # False

print(validate_user("red_quinoa", 4)) # True

print(validate_user("_red_quinoa", 4)) # False


