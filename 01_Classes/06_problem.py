# write a program to get 5 subject marks of a student  and print  
# total and average only the student has passed in all the subject 
# maximum marks is 100 and passing marks is 50.

phy = float(input("Enter the marks of physics: "))
chem = float(input("Enter the marks of chemistry: "))
bio = float(input("Enter the marks of Biology: "))
eng = float(input("Enter the marks of english: "))
math = float(input("Enter the marks of maths: "))


if (phy >=50 and chem >= 50 and bio >= 50 and eng > 50 and math >= 50):
    avg_marks = (phy + chem + bio + eng + math) / 5
    total_marks = phy + chem + bio + eng + math
    print("Total marks: ", total_marks)
    print("Total percentage: ",avg_marks)

else:
    print("you are not pass")