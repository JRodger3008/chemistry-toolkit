![Badge](https://img.shields.io/badge/Python-3.13-blue)
![MIT: LICENSE](https://img.shields.io/badge/License-MIT-yellow.svg)
![Status](https://img.shields.io/badge/status-in--progress-yellow)

# 🔬 Chemistry Calculation Toolkit
*In progress* Python project for chemistry calculations, using a JSON database of chemical elements.

---

## ✅ Features Implemented

### 📁 [`elements_json_creation.py`](./elements_json_creation.py) - Element Dataset Generator
- Automatically generates and populates a JSON file (`elements.json`)

### 📁 [`elements.json`](./elements.json) - Element Dataset
- Contains data on all known elements: name, symbol, atomic number, atomic mass, group, and source

### 📁 [`molar_mass.py`](./molar_mass.py) - Molar Mass/Relative Atomic Mass Calculator
- Parses complex chemical formulas, including parenthetical groupings and repeated elements (e.g., `Al₂(SO₄)₃`, `CH₃COOH`)
- Calculates molar mass using data from `elements.json`
- Gracefully handles unknown elements and malformed formulas
- Includes test cases and interactive user input

## ⌛ Planned Features

This JSON dataset is intended for use in upcoming chemistry-related Python projects, such as:
- 🧮 Support for calculating molar masses of hydrate compounds (e.g., `CuSO₄·5H₂O`)
- ⚗️ pH and pKa calculations (including Henderson-Hasselbalch equation)
- 🧪 Stoichiometry, Mole calculations, and related tools
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
