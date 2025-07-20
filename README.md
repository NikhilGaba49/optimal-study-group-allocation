# Optimal Study Group Allocation

A modular Python system that simulates and optimizes study group formation among fictional characters called **Zoomerbinis**. Each Zoomerbini is defined by a set of unique attributes and academic subjects. The system identifies valid groupings based on shared or diverse traits and common subjects, scoring and ranking them to prioritize the most effective study groups.

---

## Overview

This project creates and evaluates study groups of Zoomerbinis using combinatorics, set operations, and modular arithmetic. The focus is on ensuring group diversity, shared interests, and optimal group sizes to simulate ideal collaborative learning environments.

---

## Features

### Attribute Decoding Logic
- Each Zoomerbini is assigned a unique type ID.
- Traits such as hairstyle, color, accessory, and social media platform are decoded using:
  - Dictionary-based classification
  - Modular arithmetic

### Validation Engine
- Ensures all generated groups meet the following criteria:
  - Group size is either **3** or **4**
  - All members are unique
  - For each trait, values are **either all the same or all different**
  - Group members share **at least one academic subject**

### Optimization Algorithm
- Generates all valid group combinations using `itertools`
- Scores each group based on:
  - **Number of shared subjects**
  - **Preferred group size** (more points for ideal sizes)
- Ranks all groups in descending order of effectiveness

### Modular Design
- Clean, reusable, and well-organized functions
- Promotes scalability and ease of maintenance

---

## Tools & Skills Used

- **Language:** Python  
- **Techniques & Concepts:**
  - Combinatorics (`itertools`)
  - Set Operations
  - Modular Arithmetic
  - Data Structures (Lists, Dictionaries, Sets)
  - Functional Decomposition
  - Clean Coding Practices

---

## Folder Structure 
> optimal-study-group-allocation/
> │
> ├── data/
> │ └── zoomerbinis.json # Sample input data defining Zoomerbinis and their subjects> │
> ├── modules/
> │ ├── zoomerbinis.py # Attribute decoding and Zoomerbini object logic
> │ ├── validator.py # Validation logic for group eligibility
> │ └── optimizer.py # Group scoring and optimization functions
> │
> ├── main.py # Main script to run the simulation
> ├── requirements.txt # Dependencies (if any)
> ├── README.md # Project documentation
