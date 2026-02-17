def Volume():
    pi=3.142
    radius=int(input("Enter the radius:"))
    height=int(input("Enter the height:"))
    volume=(pi* radius * radius * height)
    return volume

result=Volume()
print("Volume of cylinder:",result)


def Grade():
    score=int(input("Enter your score:"))
    if(score>=90 and score<100):
         grade="A"
    elif(score>=89 and score<=80):
        grade="B"
    elif(score>=79 and score<=70):
        grade="C"
    elif(score>=69 and score<=60):
        grade="D"
    else:
        grade="FAIL"
    return grade

f_grade=Grade()
print("YOUR FINAL GRADE IS:",f_grade)
    
