# write a program to accept marks of 6 students and display then in a sorts manner

markss = []

f1 = int(input("Enter marks here : "))
markss.append(f1)

f2 = int(input("Enter marks here : "))  
markss.append(f2)

f3 = int(input("Enter marks here : "))
markss.append(f3)

f4 = int(input("Enter marks here : "))
markss.append(f4)

f5 = int(input("Enter marks here : "))
markss.append(f5)

f6 = int(input("Enter marks here : "))
markss.append(f6)
markss.sort()
print(markss)