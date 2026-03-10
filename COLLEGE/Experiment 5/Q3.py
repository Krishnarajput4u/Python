# Find runner-up score

n = int(input("Enter number of students: "))

scores = list(map(int, input("Enter scores: ").split()))

unique_scores = list(set(scores))  # Remove duplicates
unique_scores.remove(max(unique_scores))  # Remove highest

print("Runner-up score:", max(unique_scores))

