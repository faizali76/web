# Write a python function to print multiplication table of a given number.
def multiply(n):
    for i in range(1, n+1):
        print(f"{n} x {i} = {n*i}")


multiply(10)