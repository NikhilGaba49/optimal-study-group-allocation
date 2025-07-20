# Optimal Study Group Allocation

A **modular Python system** that simulates and optimizes study group formation among fictional characters called **Zoomerbinis**.  
Each Zoomerbini has unique attributes and academic subjects, and the system **scores and ranks study groups** based on diversity, shared interests, and group size to identify the most effective study groups.

---

## Overview

This project **creates and evaluates study groups** using **combinatorics, set operations, and modular arithmetic**.  
The focus is on:
- **Group diversity** – balancing similar and distinct traits  
- **Shared academic interests** – ensuring common study goals  
- **Optimal group size** – promoting ideal collaboration  

---

## Features

### Attribute Decoding Logic
- Each Zoomerbini is assigned a **unique type ID**  
- Traits (hairstyle, color, accessory, social media platform) decoded using:
  - Dictionary-based classification  
  - **Modular arithmetic**  

### Validation Engine
Ensures all generated groups meet strict criteria:
- Group size = **3 or 4 members**  
- All members are **unique**  
- For each trait: **all the same OR all different**  
- Group members share **at least one academic subject**  

### Optimization Algorithm
- Generates **all valid combinations** using `itertools`  
- Scores groups based on:
  - Number of **shared subjects**  
  - **Preferred group size** (bonus for ideal sizes)  
- **Ranks groups** in descending order of effectiveness  

### Modular Design
- Clean, reusable, and well-organized functions  
- Promotes **scalability** and **ease of maintenance**

---

##  Tools & Skills

**Language**: Python  
**Techniques & Concepts**:
- Combinatorics (`itertools`)  
- Set Operations  
- Modular Arithmetic  
- Data Structures: Lists, Dictionaries, Sets  
- Functional Decomposition  
- Clean Coding Practices

---

## Getting Started

### 1 Clone the repository
```bash
git clone https://github.com/NikhilGaba49/optimal-study-group-allocation.git
cd optimal-study-group-allocation
