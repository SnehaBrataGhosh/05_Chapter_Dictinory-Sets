# This programme shows different operations of sets

print("==== Set Operations ====")

A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

print("Set A:", A)
print("Set B:", B)

# 1. Union
print("1. Union (A | B):", A | B)

# 2. Intersection
print("2. Intersection (A & B):", A & B)

# 3. Difference
print("3. A - B:", A - B)
print("4. B - A:", B - A)

# 4. Symmetric Difference
print("5. Symmetric Difference (A ^ B):", A ^ B)

# 5. Subset and Superset
print("6. A is subset of B?:", A.issubset(B))
print("7. A is superset of B?:", A.issuperset(B))

# 6. Disjoint
print("8. Are A and B disjoint?:", A.isdisjoint(B))
