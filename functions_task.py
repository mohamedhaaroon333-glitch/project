"""Build a "marks utility" with functions: average(), highest(), lowest(), grade(score). Use them on a sample list."""
marks=[90,80,35,55,78,60]
def average(marks):
   return sum(marks)/len(marks)
def highest(marks):
    return max(marks)
def lowest(marks):
    return min(marks)
def system(marks):
  for i in marks:
    if i>=90:
        grade="A"
       
    elif i<90 and i>=70:
        grade="B"
        
    elif i<70 and i>=45:
        grade="C"
        
    elif i<45 and i>=35:
        grade="D"
       
    else:
        grade="FAILED"
    print(f"{i} : {grade}")
print("Mark List:", marks)
print("Average Marks:",average(marks))
print(f"Highest marks: {highest(marks)} and Lowest marks: {lowest(marks)}")
print(f"\n The ScoreCard Off The Induviual Is :")
system(marks)


