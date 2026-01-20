seconds = int(input("Enter time in seconds: "))
hours = seconds/ 3600
minutes = (seconds % 3600)/ 60
remaining_seconds = seconds % 60

print("Hours:", int(hours))
print("Minutes:", int(minutes))
print("Seconds:", int(remaining_seconds))
