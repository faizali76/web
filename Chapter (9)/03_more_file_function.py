# file readlines


# f = open("file.txt", "r")

# lines = f.readlines()

# print(lines, type(lines))

# f.close()


# File readline


# f = open("file.txt", "r")

# line1 = f.readline()
# print(line1, type(line1))
 
# line2 = f.readline()
# print(line2, type(line2))

# line3 = f.readline()
# print(line3, type(line3))

# line4 = f.readline()
# print(line4, type(line4))

# line5 = f.readline()
# print(line5, type(line5))

# line6 = f.readline()
# print(line6 =="")

# f.close()


# While loop main bhi kar sakte hai

f = open("file.txt", "r")

line = f.readline()
while(line !=""):
    print(line)
    line = f.readline()

f.close()