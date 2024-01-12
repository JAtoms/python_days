import os.path
import random

# Generate random numbers
x = random.randint(1, 6)

# Generate random items from a list
rock = ["rock", "paper", "scissors"]
choice = random.choice(rock)
print(choice)

# Shuffle
rock = ["rock", "paper", "scissors"]
random.shuffle(rock)
print(rock)
