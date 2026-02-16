# Lab Exercise 
# Student Performance Analytics System
# Problem Statement:
# A university wants to analyze student performance data for a class of N students.
# For each student, the following inputs are given:
# Roll Number (integer)
# Name (string)
# Marks in 5 subjects (each out of 100)
# You must write a Python program using only loops and if-else statements (no built-in functions like max(), min(), sum(), sort(), etc.).
 
# Your program must perform the following tasks:
# Input Section
# Accept N students.
# For each student:
# Read roll number
# Read name
# Read 5 subject marks
 
# For Each Student Calculate:
# Total marks
# Percentage
# Grade using conditions:
# >= 90 → Grade O
# >= 80 → Grade A+
# >= 70 → Grade A
# >= 60 → Grade B
# >= 50 → Grade C
# >= 40 → Grade D
# < 40 → Fail
 
# Additional Conditions:
# If a student fails in any subject (<40) → overall result = "Fail"
# Otherwise → "Pass"
 
# Find and Display:
# Class Topper (highest total)
# Lowest Scorer
# Number of students passed
# Number of students failed
# Average class percentage (calculated manually)
 
# Advanced Logic Requirement:
# Display students who scored:
# Above class average
# Below class average
# Display distinction holders (percentage ≥ 75 AND no subject < 60)
 
# Constraint:
#  Do NOT use:
# sum()
# max()
# min()
# sort()
# Lists methods like .append() in advanced ways
# Functions
# Dictionary
# Only:
# for loop
# while loop
# if-elif-else
# Basic variables
x=int(input("Enter the number of students : "))
failure=0
passed=0
total_sum=0
max_marks=0,max_name=""
min_marks=0,min_name=""
class_average=0
for i in range(x):
    roll_number=int(input("Enter the roll number of student : "))
    name=input("Enter the name of student : ")
    sum=0
    for j in range(5):
        marks=int(input(f"Enter the marks of subject {j+1} : "))
        sum+=marks
    if marks>=90:
        grade='O'
    elif marks>=80:
        grade='A+'
    elif marks>=70:
        grade='A'
    elif marks>=60:
        grade='B'
    elif marks>=50:
        grade='C'
    elif marks>=40:
        grade='D'
    else:
        grade='F'
    
    if grade=='F':
        failure+=1
    else:
        passed+=1
    
    total_sum+=sum
    percentage=sum/5
    if sum>max_marks:
        max_marks=sum
        max_name=name
    
    if sum<min_marks:
        min_marks=sum
        min_name=name
    
    class_average=total_sum/(i+1)


