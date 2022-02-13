def fact(num):
    if(num == 1):
        return 1
    return num*fact(num-1)

#main
num = int(input("Enter A Number : "))
facto = fact(num)
print(f"Factorial of {num} is : {facto}")