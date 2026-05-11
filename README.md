Chapter 5 – Dictionaries and Sets

Overview
This folder contains programs that practice dictionaries and sets: how to create them, common methods, and typical set operations like union/intersection. It also includes small exercises using dicts/sets for simple lookup and uniqueness handling.

Concepts Covered
- Creating dictionaries using literals, dict(), zip(), and comprehensions
- Dictionary methods: get, keys, values, items, update, pop, popitem, setdefault, clear, copy, fromkeys
- Creating sets and understanding uniqueness (duplicates removed automatically)
- Set methods: add, update, remove, discard, pop, copy, clear
- Set operations: union, intersection, difference, symmetric difference
- Subset/superset checks and disjoint checks
- Difference between {} (empty dict) and set()

Code Highlights
- A dictionary “methods” script that creates multiple dicts and demonstrates common operations
- A set “methods” script showing several creation patterns and in-place update methods
- A set o.perations demo using |, &, -, ^ and relationship checks
- Practice exercises:
  - Simple Hindi-to-English word lookup using a dictionary
  - Taking 8 numbers from the user and storing them in a set to keep unique values
  - Demonstrating that 18 and "18" are different set elements
  - Demonstrating that 20 and 20.0 are considered equal keys/values in a set
  - Building a “favorite language” dictionary from user input (and showing that keys must be unique)

Learning Outcome
I learned how dictionaries store key/value pairs and how sets help when I need unique items. I also practiced common operations used in scripting, like quick lookups and removing duplicates.

Notes
- The word-meaning script uses direct indexing (w[a]); if the key is missing it will raise an error. Using w.get(a) with a fallback message would be safer.
- The “dictionary duplicate keys” examples show that later updates overwrite earlier entries when the same name/key is entered again.
