a=int(input("Enter first number a: "))
b=int(input("Enter second number b: "))
op=input("Enter operation (+, -, *, /, %): ")

if op=='+':
    result = a + b
elif op=='-':
    result = a - b
elif op=='*':
    result = a * b
elif op=='/':
    if b != 0:
        result = a / b
    else:
        result = "Error: Division by zero"
elif op=='%':
        result = a % b
else:
    result = "Error: Invalid operation"

print(f"Result: {result}")