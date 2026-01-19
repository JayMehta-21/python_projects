import string 
import random 

uppercase=string.ascii_uppercase
lowercase=string.ascii_lowercase
digit=string.digits
symbol=string.punctuation
final_update=uppercase+lowercase+digit+symbol
print("Welcome to Password Generator")
lenght=int(input("Enter the lenght of the password you want to generate : ").strip())
password= ""
for i in range(lenght):
    password+=random.choice(final_update)
print(f"Your Password is : {password}")
print("THANK YOU")