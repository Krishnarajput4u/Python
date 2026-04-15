def avg(marks):
    average=sum(marks)/len(marks)
    return average

#second part
def grade(average):
    if average>=90:
        grade='A'
    elif average<=89 and average>=75:
        grade='B'
    elif average<=74 and average>=50:
        grade='C'
    else:
        grade='F'

    return grade

#third part
def maximum(marks):
    max=max(marks)
    return max

#fourth part
def minimum(marks):
    min=min(marks)
    return min