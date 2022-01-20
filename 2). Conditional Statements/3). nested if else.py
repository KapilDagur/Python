#Here we see nested if-else statment
#Nested mean a stament whose is in side a conditional and that conditional statment also in a comditional 
#Means Double conditional statment
val = int(input("Enter Integer value : "))
if val < 100 :
    if val < 50 :
        print("Value is less then fifty : ",val)
    else:
        print("Value is greater then fifty ya fifty and less then hundred : ",val )
else:
    if val < 500 :
        print("Value is greater than hundred ya hundred and less then five hundred : ",val)
    else:
        print("Value is greater than five hundred ya five hundred : ")