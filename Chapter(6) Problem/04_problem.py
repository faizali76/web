# W eite a program to find whether a given username contains less than 10 character or not.
username = input("Enter username")
if(len(username)<10):
    print("Your username contains less than 10 character")
else:
    print("Your username contains more than or equal to  10 character")