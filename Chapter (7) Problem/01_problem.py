# write a program to orint multiplication table of a given number using for loop.
n = int(input("Enter a numbner: "))

for i in range(1, 11):
    print(f"{n} x {i} = {n*i}")