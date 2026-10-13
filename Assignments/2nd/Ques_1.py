def odd_even(num):
    
    rem=num%2
    return rem
    
    # if num%2==0:
    #     print("Entered number is even")
    # else:
    #     print("Entered number is odd")

a=int(input("Enter a number to check for odd or even : "))

ans=odd_even(a)

if ans==0:
    print("entered number is even")
else:
    print("entered number is odd")