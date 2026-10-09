name = " kushal sai "
print(f"Welcome,\n {name.strip().capitalize()}")

########################################################

EmpName = 'John'
Empid = 'EMP1025'
Dept = 'Finance'
Salary = '55000'

print('Employee Details\n')
print('------------')
print(f'Name = {EmpName}\nID = {Empid}\nDepartment = {Dept}\nSalary = {Salary} ')

########################################################

user  = 'admin'
password_1 = 'pass123'

username = input('Enter username: ')
password = input('Enter password: ')

if username.lower() == user and password == password_1:
    print('login successful')
else:
    print('invalid credentials')
print(f'Login request recieved for the <{username}>')

########################################################

inv_amt = input('enter invoice amount: ')
gst_percent = input('enter GST percentage: ')

for i in range(3):
    if not inv_amt.replace('.', '', 1).isdigit() or not gst_percent.replace('.', '', 1).isdigit():
        print('Invalid input. Please enter valid numbers.')
        inv_amt = input('enter invoice amount: ')
        gst_percent = input('enter GST percentage: ')

    else:
        break
try:
    
    if inv_amt < 0 or gst_percent < 0 or gst_percent > 100:
        raise ValueError('Invoice amount and GST percentage must be non-negative.')
    gst_amount = (inv_amt * gst_percent) / 100
    total_amount = inv_amt + gst_amount
    print(f'Invoice Amount: {inv_amt}\nGST Amount: {gst_amount}\nTotal Amount: {total_amount}')
except ValueError:
    print('Invalid input. Please enter valid numbers.')