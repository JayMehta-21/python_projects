def checker():
    print(".... Palindrome Checker ....")
    user=input("Enter a String you want to check :").lower().strip()
    rev=user[::-1]
    if user==rev:
        print("Its a Palindrome")
    else:
        print("Its Not a Palindrome")
checker()