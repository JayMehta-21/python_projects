a=int(input("enter 1st number : "))
i=0
while i in range(100000):


    print(''' select your operator :
        1)addition 
        2)subtraction
        3)multiple
        4)divition
        5)exit
      ''')

    user= int(input("enter your choice(number) : "))
    b=int(input("enter 2nd number : "))

    if user==1:
        print(f"Your Anser is : {a+b}" )
        a=a+b
        
    elif user==2:
        print(f"Your Anser is : {a-b}" )
        a=a-b
    elif user==3:
        print(f"Your Anser is : {a*b}" )
        a=a*b
    elif user==4:
        print(f"Your Anser is : {a/b}" )
        a=a/b
    elif user==5:
        break 
    else:
        print("enter a valid choice ")
