"""
GLAB 386.2.1 – NumPy Random examples
Starter Script for Random Number Generation
Author: Danielle Burgos
"""

import numpy as np
from numpy import random


# ---------------------------------------------------------
# 1. Generate random floats between 0 and 1
# ---------------------------------------------------------
def generate_random_floats():
    print("Random floats (0–1):")
    print(random.rand(10))  # 10 random floats
    print("-" * 50)


# ---------------------------------------------------------
# 2. Generate random numbers from a normal distribution
# ---------------------------------------------------------
def generate_normal_distribution():
    print("Normal distribution (mean=0, std=1):")
    print(random.randn(5))  # 5 normally distributed values
    print("-" * 50)


# ---------------------------------------------------------
# 3. Random choice from a list
# ---------------------------------------------------------
def random_choice_example():
    menu = [
        "Spaghetti Carbonara", "Chicken Alfredo", "Margherita Pizza",
        "Cheeseburger", "Caesar Salad", "Fish and Chips",
        "Pad Thai", "Sushi Platter", "Vegetable Stir-Fry", "Grilled Salmon"
    ]

    print("Random dish suggestion:")
    print(random.choice(menu))
    print("-" * 50)


# ---------------------------------------------------------
# 4. Shuffle a list in place
# ---------------------------------------------------------
def shuffle_example():
    items = ['a', 'b', 'c', 'd', 'e', 'f']
    print("Original list:", items)
    random.shuffle(items)
    print("Shuffled list:", items)
    print("-" * 50)


# ---------------------------------------------------------
# Main runner
# ---------------------------------------------------------
def main():
    generate_random_floats()
    generate_normal_distribution()
    random_choice_example()
    shuffle_example()

