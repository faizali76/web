# Write a progarm using functions to find greatests of three numbers.
def greatest(a,b,c):
    if(a>b and a>c):
        return a
    elif(b>a and b>c):
        return b
    elif(c>b and c>a):
        return c
    
a = 1
b = 89
c = 5
print(greatest(a,b,c))