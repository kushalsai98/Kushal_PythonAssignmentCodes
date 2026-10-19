from Ques_1 import odd_even
from Ques_2 import factorial
from Ques_5 import mul_table
from Ques_3 import full_pyramid

print("Please select items from the below menu to execute the task:")
print("1. Odd or Even task")
print("2. Factorial task")
print("3. Multiplication table task")
print("4. Star pyramid pattern task")
item=int(input("Enter which Item you want to select from the menu :"))

if item==1:
    odd_even()
elif item==2:
    factorial()
elif item==3:
    mul_table()
elif item==4:
    full_pyramid()
else:
    pass