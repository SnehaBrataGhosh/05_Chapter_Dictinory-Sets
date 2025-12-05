# This programme shows different ways of creating sets and its different methods

print("==== Set Creation and Common Methods ====")

# Different ways of creating sets

# 1. Empty set
set1 = set()
print("1. Empty set:", set1)

# 2. Set from list
set2 = set([1, 2, 3, 4])
print("2. From list:", set2)

# 3. Set from tuple
set3 = set((4, 5, 6))
print("3. From tuple:", set3)

# 4. Set from string
set4 = set("banana")
print("4. From string 'banana':", set4)

# 5. Set with duplicates
set5 = {1, 2, 2, 3, 4, 4}
print("5. With duplicates:", set5)

# 6. Set comprehension
set6 = {x**2 for x in range(1, 6)}
print("6. Set comprehension (squares):", set6)

# 7. Mixed data types
set7 = {1, "hello", 3.14, True}
print("7. Mixed data:", set7)


print("\n==== Common Set Methods ====")

s = {1, 2, 3}
print("Original set:", s)

s.add(4)
print("1. add(4):", s)

s.update([5, 6])
print("2. update([5, 6]):", s)

s.remove(2)
print("3. remove(2):", s)

s.discard(100)  # No error if 100 not in set
print("4. discard(100):", s)

popped = s.pop()
print("5. pop():", popped, "→ After pop:", s)

copy_set = s.copy()
print("6. copy():", copy_set)

s.clear()
print("7. clear():", s)

# print("\n==== Extra Set Methods (modify sets in-place) ====")

A = {10, 20, 30, 40}
B = {30, 40, 50, 60}
print("Set A:", A)
print("Set B:", B)

A_diff = A.copy()
A_diff.difference_update(B)
print("8. difference_update(B):", A_diff)

A_inter = A.copy()
A_inter.intersection_update(B)
print("9. intersection_update(B):", A_inter)

A_sym = A.copy()
A_sym.symmetric_difference_update(B)
print("10. symmetric_difference_update(B):", A_sym)
