![Badge](https://img.shields.io/badge/Python-3.13-blue)
![MIT: LICENSE](https://img.shields.io/badge/License-MIT-yellow.svg)

# 🔬 Chemistry Calculation Toolkit
*In progress* Python project for chemistry calculations, using a JSON database of chemical elements.

---

## ✅ Features Implemented

📁 [`elements_json_creation.py`](./elements_json_creation.py) - **Element Dataset Generator** <br>
Automatically generates and populates a JSON file (`elements.json`) containing data on all known chemical elements, including: name, symbol, atomic number, atomic mass, group, and source.
<br>


## ⌛ Planned Features

📁 [`molar_mass.py`](./molar_mass.py) - **Molar Mass/Relative Atomic Mass Calculator** (*in progress*)

This JSON dataset is intended for use in upcoming chemistry-related Python projects, such as:
- 🧮 Relative Atomic Mass & Molar Mass Calculations 
- ⚗️ pH and pKa Calculations (including Henderson-Hasselbalch Equation)
- 🧪 Stoichiometry, Mole Calculations, and related tools
- 🧾 Interactive Periodic Table

---

## ❓ Why no API fetching (yet)?
There are two main reasons:
1. **Offline-first Design**:
   - The generator provides a static, reliable reference file that avoids dependency on external APIs. This ensures consistency across tools and allows offline use.
     
2. **Learn API Integration Before Applying**:
   - While I’ve worked with APIs in JavaScript, I’ve yet to implement one in Python. I chose to delay API integration until I fully understand the Pythonic approach to fetching, parsing, and handling API data.
   - I also took this as an opportunity to deepen my understanding of JSON - learning how to generate structured files in Python and use them effectively in data-driven calculations.

---

## License
This repository is licensed under the MIT License - see the [LICENSE](./LICENSE) file for details.
