# -*- coding: utf-8 -*-
"""
Created on Fri Oct 20 05:50:24 2023

@author: kavit
"""

import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Get the desired password length from the user
password_length = int(input("Enter the desired password length: "))

# Generate and print the random password
if password_length > 0:
    password = generate_password(password_length)
    print("Generated Password:", password)
else:
    print("Password length should be greater than 0")