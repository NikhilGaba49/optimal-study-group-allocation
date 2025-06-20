# optimal-study-group-allocation
Overview:
Developed a modular system in Python to simulate and optimize study group formation among fictional characters called Zoomerbinis, each defined by unique attributes and academic subjects. The program identifies valid groupings based on shared traits and common subjects, and scores them to prioritize the most effective study groups.
Key Features:
•	Attribute Decoding Logic: Mapped Zoomerbini traits (hairstyle, color, accessory, social media) from a unique type ID using dictionary-based classification and modular arithmetic.
•	Validation Engine: Ensured group validity by enforcing group size constraints, uniqueness of members, and consistency of attributes (either all same or all different) while checking for shared academic subjects.
•	Optimization Algorithm: Generated all possible group combinations (size 3 or 4), validated them, scored each based on number of shared subjects and group size, and sorted them in descending order of effectiveness.
•	Modular Design: Divided the project into clearly defined and reusable functions, promoting clean code structure and scalability.
Tools & Skills Used:
Python, Combinatorics (itertools), Set Operations, Modular Arithmetic, Data Structures (Lists, Dictionaries, Sets), Functional Decomposition, Clean Coding Practices
