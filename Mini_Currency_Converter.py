def convertor():
    print('''.... Currency Convertor ...
    1) Indian Rupee to American Dollar
    2) American Dollar to Indian Rupee''')
    user_choice=int(input("Enter your choice : "))
    
    if user_choice==1:
        user_Amount=float(input("Enter the amount : "))
        Amount=round(user_Amount/82.3,2)
        print(f"{user_Amount} Rupee is equal to {Amount} Dollar")
    elif user_choice==2:
        user_Amount=float(input("Enter the amount : "))
        Amount=round(user_Amount*82.3,2)
        print(f"{user_Amount} Dollar is equal to {Amount} Rupees")
    else:
        print("please enter a valid choice")
convertor()