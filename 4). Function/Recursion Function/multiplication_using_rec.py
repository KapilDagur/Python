def multi(n,i):
    if(i==0):
        return 0
    return n+multi(n,i-1)

#main()
mul = int(input("Enter Multiplicand : "))
mult = int(input("Enter Multiplier : "))
res = multi(mul,mult)
print(f"Multiplication of {mul} and {mult} is {res}")