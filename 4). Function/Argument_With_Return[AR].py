def func(num):     #Function Definition/prototype

    if(num ==1):
        return "Hii !!!"
    elif(num == 2):
        return "Hello !!!"
    elif(num == 3):
        return "Bye !!!"
    else:
        return "Invalid Choice !!! "

#main
while True:
    print("Press 1 For 'Hii' ")
    print("Press 2 For 'Hello' ")
    print("Press 3 For 'Bye' ")
    print("Press 4 For 'Exit' ")
    num = int(input("Enter Your Choice : "))
    if(num == 4):
        break
    res = func(num)      #Function Calling and Return 
    print(res)