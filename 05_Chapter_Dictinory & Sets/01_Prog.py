# This programme shows the different views of creating a dictionaryand most used functions of dictionary or methods


# Different ways to create a dictionary
dict1 = {'a': 1, 'b': 2}
dict2 = dict([('x', 10), ('y', 20)])
dict3 = dict(name='Alice', age=25)
dict4 = {k: k**2 for k in range(3)}  # Using dictionary comprehension
dict5 = {}  # Empty dictionary
dict6 = dict(zip(['p', 'q'], [100, 200]))  # Using zip

print("Different dictionaries created:")
print("dict1:", dict1)
print("dict2:", dict2)
print("dict3:", dict3)
print("dict4:", dict4)
print("dict5:", dict5)
print("dict6:", dict6)

# Now applying different dictionary methods

# 1. get()
print("\nValue for key 'a' in dict1:", dict1.get('a'))

# 2. keys()
print("Keys in dict2:", list(dict2.keys()))

# 3. values()
print("Values in dict3:", list(dict3.values()))

# 4. items()
print("Items in dict4:", list(dict4.items()))

# 5. update()
dict1.update({'c': 3})
print("dict1 after update:", dict1)

# 6. pop()
removed = dict2.pop('x')
print("Removed value from dict2:", removed)
print("dict2 after pop:", dict2)

# 7. popitem()
removed_item = dict3.popitem()
print("Removed item from dict3:", removed_item)
print("dict3 after popitem:", dict3)

# 8. setdefault()
result = dict1.setdefault('d', 4)
print("Result of setdefault on dict1:", result)
print("dict1 after setdefault:", dict1)

# 9. clear()
dict5.clear()
print("dict5 after clear:", dict5)

# 10. copy()
dict7 = dict1.copy()
print("Copy of dict1 (dict7):", dict7)

# 11. fromkeys()
dict8 = dict.fromkeys(['m', 'n', 'o'], 0)
print("Dictionary from keys with default value:", dict8)

# 12. in keyword (not a method but very useful)
print("Is 'b' a key in dict1?", 'b' in dict1)
