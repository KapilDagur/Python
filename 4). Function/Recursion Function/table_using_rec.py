import re


def table(n,i):
    if(i > 10):
        return 
    print(n,"*",i,"=",n*i)
    return table(n,i+1)

#main
num = int(input("Enter A Number\n"))
table(num,1)