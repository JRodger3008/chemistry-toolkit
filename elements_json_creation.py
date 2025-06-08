"""
Automatically generates a JSON file (elements.json) containing data on all known chemical elements.

This dataset serves as a foundational, static reference for various chemistry-related calculations, 
including relative atomic mass, pH, pKa, and other formulae.

Each element object includes:
    - Name - Full name of the element (e.g., Hydrogen)
    - Symbol - Standardised IUPAC chemical symbol (e.g., H, He, Li)
    - Atomic number - inferred from list position using `enumerate(...)`
    - Atomic mass - Quantity of matter contained in an atom (units: Daltons)
    - Group classification - Element family (e.g., Halogen, Noble Gas)
    - Data source - PubChem or Royal Society of Chemistry (RSC)

Note on Data Source:
Some atomic mass values (see `ALTERNATE_SOURCE_ELEMENTS`) in the elements_data are sourced 
from the RSC website (`RSC_URL`), while others are primarily sourced from PubChem (`PUBCHEM_URL`).

Note: While fetching data directly from an API can be more efficient, this script 
generates a static, hardcoded JSON dataset useful for offline use and demonstration purposes.

Author: Jordan Rodger
Created: 14/05/2025 | Last Modified: 31/05/2025
"""

import json


# ====== CONSTANTS ======
OUTPUT_FILE = "elements.json"

# PubChem - Default URL
PUBCHEM_URL = "https://pubchem.ncbi.nlm.nih.gov/ptable/atomic-mass/"
# Royal Society of Chemistry - Secondary URL
RSC_URL = "https://periodic-table.rsc.org/?gad_source=1&gad_campaignid=116934383&gbraid=0AAAAADs4yQFnMI3HEftlCZXwrgIx-nE-U&gclid=CjwKCAjw_pDBBhBMEiwAmY02NjNlc40_jQymbG-K31Rcv6QFF5ta-90Ff5ptaHfqarkn8X7msW32WRoCCsoQAvD_BwE"

# Set of elemental symbols whose atomic mass has been sourced from RSC_URL
ALTERNATE_SOURCE_ELEMENTS = {
    "Li", "Ar", "Zn", "Se", "Br", "Kr", "Ru", "Cd", "Ba", "Nd", "Sm",
    "Er", "Yb", "Hf", "Os", "Ir", "Pt", "Hg", "Pb"
}

# Sulfur was taken as an average between PubChems 32.07, and RSCs 32.06
# Thus Sulfur's atomic_mass = 32.065 in `elements.json` file

# Define element data as tuples: (name, symbol, atomic_mass, group)
elements_data = [
    ("Hydrogen", "H", 1.008, "Nonmetal"),
    ("Helium", "He", 4.0026, "Noble Gas"),
    ("Lithium", "Li", 6.941, "Alkali Metal"),
    ("Beryllium", "Be", 9.012183, "Alkaline Earth Metal"),
    ("Boron", "B", 10.81, "Metalloid"),
    ("Carbon", "C", 12.011, "Nonmetal"),
    ("Nitrogen", "N", 14.007, "Nonmetal"),
    ("Oxygen", "O", 15.999, "Nonmetal"),
    ("Fluorine", "F", 18.99840316, "Halogen"),
    ("Neon", "Ne", 20.18, "Noble Gas"),
    ("Sodium", "Na", 22.9897693, "Alkali Metal"),
    ("Magnesium", "Mg", 24.305, "Alkaline Earth Metal"),
    ("Aluminium", "Al", 26.981538, "Post-transition Metal"),
    ("Silicon", "Si", 28.085, "Metalloid"),
    ("Phosphorus", "P", 30.97376200, "Nonmetal"),
    ("Sulfur", "S", 32.07, "Nonmetal"),
    ("Chlorine", "Cl", 35.45, "Halogen"),
    ("Argon", "Ar", 39.95, "Noble Gas"),
    ("Potassium", "K", 39.0983, "Alkali Metal"),
    ("Calcium", "Ca", 40.08, "Alkaline Earth Metal"),
    ("Scandium", "Sc", 44.95591, "Transition Metal"),
    ("Titanium", "Ti", 47.867, "Transition Metal"),
    ("Vanadium", "V", 50.9415, "Transition Metal"),
    ("Chromium", "Cr", 51.996, "Transition Metal"),
    ("Manganese", "Mn", 54.93804, "Transition Metal"),
    ("Iron", "Fe", 55.84, "Transition Metal"),
    ("Cobalt", "Co", 58.93319, "Transition Metal"),
    ("Nickel", "Ni", 58.693, "Transition Metal"),
    ("Copper", "Cu", 63.55, "Transition Metal"),
    ("Zinc", "Zn", 65.38, "Transition Metal"),
    ("Gallium", "Ga", 69.723, "Post-transition Metal"),
    ("Germanium", "Ge", 72.63, "Metalloid"),
    ("Arsenic", "As", 74.92159, "Metalloid"),
    ("Selenium", "Se", 78.971, "Nonmetal"),
    ("Bromine", "Br", 79.904, "Halogen"),
    ("Krypton", "Kr", 83.798, "Noble Gas"),
    ("Rubidium", "Rb", 85.468, "Alkali Metal"),
    ("Strontium", "Sr", 87.62, "Alkaline Earth Metal"),
    ("Yttrium", "Y", 88.90584, "Transition Metal"),
    ("Zirconium", "Zr", 91.22, "Transition Metal"),
    ("Niobium", "Nb", 92.90637, "Transition Metal"),
    ("Molybdenum", "Mo", 95.95, "Transition Metal"),
    ("Technetium", "Tc", 96.90636, "Transition Metal"),
    ("Ruthenium", "Ru", 101.07, "Transition Metal"),
    ("Rhodium", "Rh", 102.9055, "Transition Metal"),
    ("Palladium", "Pd", 106.42, "Transition Metal"),
    ("Silver", "Ag", 107.868, "Transition Metal"),
    ("Cadmium", "Cd", 112.414, "Transition Metal"),
    ("Indium", "In", 114.818, "Post-transition Metal"),
    ("Tin", "Sn", 118.71, "Post-transition Metal"),
    ("Antimony", "Sb", 121.760, "Metalloid"),
    ("Tellurium", "Te", 127.6, "Metalloid"),
    ("Iodine", "I", 126.9045, "Halogen"),
    ("Xenon", "Xe", 131.29, "Noble Gas"),
    ("Cesium", "Cs", 132.9054520, "Alkali Metal"),
    ("Barium", "Ba", 137.327, "Alkaline Earth Metal"),
    ("Lanthanum", "La", 138.9055, "Lanthanide"),
    ("Cerium", "Ce", 140.116, "Lanthanide"),
    ("Praseodymium", "Pr", 140.90766, "Lanthanide"),
    ("Neodymium", "Nd", 144.242, "Lanthanide"),
    ("Promethium", "Pm", 144.91276, "Lanthanide"),
    ("Samarium", "Sm", 150.36, "Lanthanide"),
    ("Europium", "Eu", 151.964, "Lanthanide"),
    ("Gadolinium", "Gd", 157.25, "Lanthanide"),
    ("Terbium", "Tb", 158.92535, "Lanthanide"),
    ("Dysprosium", "Dy", 162.500, "Lanthanide"),
    ("Holmium", "Ho", 164.93033, "Lanthanide"),
    ("Erbium", "Er", 167.259, "Lanthanide"),
    ("Thulium", "Tm", 168.93422, "Lanthanide"),
    ("Ytterbium", "Yb", 173.045, "Lanthanide"),
    ("Lutetium", "Lu", 174.9667, "Lanthanide"),
    ("Hafnium", "Hf", 178.486, "Transition Metal"),
    ("Tantalum", "Ta", 180.9479, "Transition Metal"),
    ("Tungsten", "W", 183.84, "Transition Metal"),
    ("Rhenium", "Re", 186.207, "Transition Metal"),
    ("Osmium", "Os", 190.23, "Transition Metal"),
    ("Iridium", "Ir", 192.217, "Transition Metal"),
    ("Platinum", "Pt", 195.084, "Transition Metal"),
    ("Gold", "Au", 196.96657, "Transition Metal"),
    ("Mercury", "Hg", 200.592, "Transition Metal"),
    ("Thallium", "Tl", 204.383, "Post-transition Metal"),
    ("Lead", "Pb", 207.2, "Post-transition Metal"),
    ("Bismuth", "Bi", 208.98040, "Post-transition Metal"),
    ("Polonium", "Po", 208.98243, "Metalloid"),
    ("Astatine", "At", 209.98715, "Halogen"),
    ("Radon", "Rn", 222.01758, "Noble Gas"),
    ("Francium", "Fr", 223.01973, "Alkali Metal"),
    ("Radium", "Ra", 226.02541, "Alkaline Earth Metal"),
    ("Actinium", "Ac", 227.02775, "Actinide"),
    ("Thorium", "Th", 232.038, "Actinide"),
    ("Protactinium", "Pa", 231.03588, "Actinide"),
    ("Uranium", "U", 238.0289, "Actinide"),
    ("Neptunium", "Np", 237.048172, "Actinide"),
    ("Plutonium", "Pu", 244.06420, "Actinide"),
    ("Americium", "Am", 243.061380, "Actinide"),
    ("Curium", "Cm", 247.07035, "Actinide"),
    ("Berkelium", "Bk", 247.07031, "Actinide"),
    ("Californium", "Cf", 251.07959, "Actinide"),
    ("Einsteinium", "Es", 252.0830, "Actinide"),
    ("Fermium", "Fm", 257.09511, "Actinide"),
    ("Mendelevium", "Md", 258.09843, "Actinide"),
    ("Nobelium", "No", 259.10100, "Actinide"),
    ("Lawrencium", "Lr", 266.120, "Actinide"),
    ("Rutherfordium", "Rf", 267.122, "Transition Metal"),
    ("Dubnium", "Db", 268.126, "Transition Metal"),
    ("Seaborgium", "Sg", 269.128, "Transition Metal"),
    ("Bohrium", "Bh", 270.133, "Transition Metal"),
    ("Hassium", "Hs", 269.1336, "Transition Metal"),
    ("Meitnerium", "Mt", 277.154, "Unknown"),
    ("Darmstadtium", "Ds", 282.166, "Unknown"),
    ("Roentgenium", "Rg", 282.169, "Unknown"),
    ("Copernicium", "Cn", 286.179, "Transition Metal"),
    ("Nihonium", "Nh", 286.182, "Post-transition Metal"),
    ("Flerovium", "Fl", 290.192, "Post-transition Metal"),
    ("Moscovium", "Mc", 290.196, "Post-transition Metal"),
    ("Livermorium", "Lv", 293.205, "Post-transition Metal"),
    ("Tennessine", "Ts", 294.211, "Halogen"),
    ("Oganesson", "Og", 295.216, "Noble Gas")
]


# Build JSON structure with atomic numbers inferred from list positions (1-based).
# I used enumerate(iterable, start) to get both the index (atomic number),
# and the element tuple from the list.
elements_json = []
for i, (name, symbol, mass, group) in enumerate(elements_data, start = 1):
    # Determines which source URL to use for atomic mass
    source = RSC_URL if symbol in ALTERNATE_SOURCE_ELEMENTS else PUBCHEM_URL

    element = {
        "name": name,
        "symbol": symbol,
        "atomic_number": i,
        "atomic_mass": mass,
        "group": group,
        "source": source
    }
    # Append the element dictionary to the list
    elements_json.append(element)


# Used if __name__ == "__main__" to make the script safe for reuse.
if __name__ == "__main__":
    # Write the list of elements to elements.json in write mode (overwrites if exists).
    # UTF-8 encoding specified for compatibility across different operating systems.
    # Output is formatted with an indentation of 4 spaces for readability.
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(elements_json, f, indent=4)

    # Confirm successful creation of elements.json file
    print(f"JSON file '{OUTPUT_FILE}' created successfully with {len(elements_json)} elements.")