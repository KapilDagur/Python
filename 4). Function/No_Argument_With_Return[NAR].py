def func():     #Function Definition/prototype
    while True:
        print("Press 1 For 'Hii' ")
        print("Press 2 For 'Hello' ")
        print("Press 3 For 'Bye' ")
        print("Press 4 For 'Exit' ")
        num = int(input("Enter Your Choice : "))
        return num


#main
while True:
    num = func()      #Function Calling
    if(num ==1):
        print("Hii !!!")
    elif(num == 2):
        print("Hello !!!")
    elif(num == 3):
        print("Bye !!!")
    elif(num == 4):
        break
    else:
        print("Invalid Choice !!! ")