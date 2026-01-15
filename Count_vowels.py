User_input=input("enter a string : ").lower()

print(f"Toatal a in string :  {User_input.count('a')}")
print(f"Toatal e in string :  {User_input.count('e')}")
print(f"Toatal i in string :  {User_input.count('i')}")
print(f"Toatal o in string :  {User_input.count('o')}")
print(f"Toatal u in string :  {User_input.count('u')}")

Total_vowels= ( User_input.count("a") + User_input.count("e") + User_input.count("i")+ User_input.count("o") + User_input.count("u"))

print(f"Total vowels in string : {Total_vowels}")