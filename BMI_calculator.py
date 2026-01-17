print("... welcome to BMI calculator...")
Height=float(input("Enter Your Height(cm) : "))/100
Weight=float(input("Enter Your Weight(kg) : "))

Final_value= Weight/(Height*Height)
print(f"Your BMI Value is {Final_value}")

if Final_value<18.5 :
    print("You are in Underweight Category")
elif(Final_value>=18.5 and Final_value<24.9):
    print("You are in Normal Category")
elif(Final_value>=25 and Final_value<29.9):
    print("You are in Overweight Category")
elif(Final_value>=30 and Final_value<34.9):
    print("You are in Obesity(class_1) Category")
elif(Final_value>=35 and Final_value<39.9):
    print("You are in Obesity(class_2) Category")
else:
    print("You are in Obesity(class_3) Category")
