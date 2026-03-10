with open("numbers.txt", "w") as file:
    file.write("120\n50\n200\n30\n150")

with open("numbers.txt", "r") as file:
    nums = [int(num) for num in file]

print("Maximum:", max(nums))

#average 

avg = sum(nums) / len(nums)
print("Average:", avg)

count = 0

#Number greater than 100

for num in nums:
    if num > 100:
        count += 1

print("Numbers > 100:", count)