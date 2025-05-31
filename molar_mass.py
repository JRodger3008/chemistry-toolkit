"""
This is an in-progress script for calculating relative atomic/molar mass
from a chemical formula using the generated elements.json dataset.

Author: Jordan Rodger
"""

import json

def load_elements(filename="elements.json"):
    with open(filename, "r") as f: # Opens file in read-mode ("r"), f = file object
        elements = json.load(f) # Parses JSON content into a Python data structure (list of dicts)
    return elements

elements = load_elements()
print(elements[18]["name"]) # Potassium

# Plan:
#   1. Parse the formula (e.g., H2O)
#   2. Count each element in the formula
#   3. Look up each element's atomic mass
#   4. Multiply atomic mass by the number of atoms for each element.
#   5. Sum up values 