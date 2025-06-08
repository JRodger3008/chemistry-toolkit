"""
Chemical Formula Parser and Molar Mass Calculator.

This module provides functionality to calculate the molar (relative atomic) mass
of a given chemical formula by parsing the molecular structure and summing 
atomic masses retrieved from a JSON-based periodic table dataset ('elements.json').

Features:
    - Parses chemical formulas with support for nested groups, multipliers, and repeated elements.
      Examples: 'CH₃COOH' (Acetic Acid) and 'Al₂(SO₄)₃' (Aluminium Sulfate).
    - Calculates molar mass using atomic masses from a local 'elements.json' file.
    - Raises ValueError for unrecognised element symbols.
    - Includes test cases and user input prompt for interactivity.

Dependencies:
    - Python standard library: `json` and `re` modules.
    - Requires 'elements.json' file with chemical element data in the following format:
        [
            {"symbol": "H", "atomic_mass": 1.008},
            ...
            {"symbol": "O", "atomic_mass": 15.999},
            ...   
        ]
    
Author: Jordan Rodger
Last edited: 08/06/2025
"""

import json
import re # Regular Expression (used for parsing chemical formulas)

# Loads element data from local JSON file
def load_elements(filename="elements.json"):
    try:
        with open(filename, "r") as f: # Opens file in read-only mode, f = file obj
            return json.load(f) # Parses JSON into Python list of dicts
    except (FileNotFoundError, json.JSONDecodeError) as e: # Handles json load errors and decoding errors
        print(f"Error loading elements.json: {e}")
        return []


def parse_formula(formula):
    """
    Parses formula using RegEx and stack data structure (list of dicts).
    This is valid for chemical formulas with repeated elements or parenthetical grouping, 
    such as CH₃COOH and Al₂(SO₄)₃.
    
    Args:
        formula (str): The formula to be parsed.
    Returns:
        stack[0] (dict): A flat dictionary with element symbols (key) and atom counts (value).
    """

    # RegEx pattern to match:
    # - Element symbol (e.g., H, He, Li)
    # - Atom count (e.g., '2' in H₂)
    # - Parentheses for grouping
    pattern = r"([A-Z][a-z]?|\d+|\(|\))"
    matches = re.findall(pattern, formula)

    stack = [{}] # Initializes a stack (list of dicts); supports nested parentheses/groups (LIFO)

    i = 0
    while i < len(matches):
        token = matches[i]

        if token == '(':
            stack.append({}) # Start a new group: push empty dict to stack
            i += 1
        elif token == ')':
            group = stack.pop() # End of group: pop the last group dict off the stack
            i += 1

            multiplier = 1 # Default multiplier after closing parentheses

            # If a number follows the closing parentheses, update multiplier
            if i < len(matches) and matches[i].isdigit():
                multiplier = int(matches[i])
                i += 1
            
            # Merge the group dict into the previous dict on the stack
            for element, count in group.items():
                stack[-1][element] = stack[-1].get(element, 0) + count * multiplier

        elif re.match('[A-Z][a-z]?', token):
            # Found an element symbol
            elem = token
            count = 1

            # If the next token is a number, set count accordingly
            if i + 1 < len(matches) and matches[i + 1].isdigit():
                count = int(matches[i + 1])
                i += 1

            # Add/update the count in the top dict on the stack
            stack[-1][elem] = stack[-1].get(elem, 0) + count
            i += 1
        else:
            # If token is unexpected, skip
            i += 1

    # Final flat dict with all elements and counts
    return stack[0]


def calculate_molar_mass(formula, element_masses):
    """
    Calculates total molar mass, using parse_formula() and element_masses lookup dict.

    Args:
        formula (str): The chemical formula to calculate molar mass from
        element_masses (dict): A dictionary mapping element symbols to atomic masses
    Returns:
        total_mass (float): The molar mass value of the chemical formula (in g/mol)
    """
    composition = parse_formula(formula)
    total_mass = 0
    for element, count in composition.items(): # Dictonary unpacking
        if element not in element_masses:
            raise ValueError(f"Unknown element: {element}")
        total_mass += element_masses[element] * count # e.g., H₂ -> element_masses['H'] = 1.008 -> 1.008 * 2 = 2.016 g/mol
    return total_mass


elements = load_elements()

# Create a lookup dictionary {symbol: atomic_mass}
element_masses = {el['symbol']: el['atomic_mass'] for el in elements}


# ====== TESTS ======
if __name__ == "__main__":
    print(f"elements[18]['name'] = {elements[18]['name']}") # Potassium
    print(f"Lead (Pb) atomic mass = {element_masses['Pb']}") # 207.2

    # Al₂(SO₄)₃ test case (Aluminium Sulfate); formatted using Unicode subscript numbers
    al_sulf = "Al2(SO4)3"
    sb_2 = "\u2082"
    sb_4 = "\u2084"
    sb_3 = "\u2083"
    al_sulf_sb = f"Al{sb_2}(SO{sb_4}){sb_3}" # Al₂(SO₄)₃
    al_sulf_mass = calculate_molar_mass(al_sulf, element_masses) # 342.146076 g/mol
    print(f"{al_sulf_sb} = {parse_formula(al_sulf)} | Molar mass = {al_sulf_mass} g/mol") # {'Al': 2, 'S': 3, 'O': 12}

    # C₆H₁₂O₆ test case (Glucose)
    glucose = "C6H12O6"
    sb_6 = "\u2086"
    sb_1 = "\u2081"
    glucose_sb = f"C{sb_6}H{sb_1}{sb_2}O{sb_6}" # C₆H₁₂O₆
    glucose_mass = calculate_molar_mass(glucose, element_masses) # 180.156 g/mol
    print(f"{glucose_sb} = {parse_formula(glucose)} | Molar mass = {glucose_mass} g/mol") # {'C': 6, 'H': 12, 'O': 6}


# ====== USER INPUT ======
formula = input("Enter a Chemical Formula (e.g., CO2): ").strip()

try:
    mass = calculate_molar_mass(formula, element_masses)
    print(f"The molar mass of {formula} is {mass:.3f} g/mol")
except ValueError as ve:
    print(f"ValueError: {ve}")