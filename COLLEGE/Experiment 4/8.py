# 8.	Take two sets and apply various set operations on them :
# S1 = {Red ,yellow, orange , blue }
# S2 = {violet, blue , purple}
s1 = {"Red", "yellow", "orange", "blue"}
s2 = {"violet", "blue", "purple"}
# a) Union of S1 and S2
union_set = s1.union(s2)
print("Union of S1 and S2:", union_set)
# b) Intersection of S1 and S2
intersection_set = s1.intersection(s2)
print("Intersection of S1 and S2:", intersection_set)
# c) Difference of S1 and S2 (S1 - S2)
difference_set = s1.difference(s2)
print("Difference of S1 and S2 (S1 - S2):", difference_set)