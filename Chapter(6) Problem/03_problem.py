# A spam comment is definded as a text containsinsing following keyword: "make of lot of money", "buy now", "subscribe this", "click this". Write a program to delect these spams.
p1 = "make of lot of money"
p2 = "buy now"
p3 = "subscribe this"
p4 = "click this"

massage = input("Enter your comment: ")

if((p1 in massage) or (p2 in massage) or (p3 in massage) or (p4 in massage)):
    print("This comment is a spam")

else:
    print("This comment is not a spam")