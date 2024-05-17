sub1 = int(input("enter the number 1"))
sub2 = int(input("enter the number 2:"))
sub3 = int(input("enter the number 3:"))
sub4 = int(input("enter the number 4:"))
sub5 = int(input("enter the number 5:"))
if(sub1>= 50 and sub2>=50 and sub3>=50 and sub4>= 50 and sub5>=50):
 total_marks = (sub1 + sub2 + sub3 + sub4 + sub5)
avg_marks = total_marks/5
print("total marks:",total_marks)
print("total parcentage:",avg_marks)
print("you are pass")