# Write a program to read the text from a given file 'poems.text' and find out whether it contains the word 'twinkle'.

# f = open("poems.txt")
# content = f.read()
# if("twinkle" in content):
#     print("The word twinkle is present in the content")

# else:
#     print("The word twinkla is present in the ")

# f.close()


f = open("poems.txt")
content = f.read()

if("twinkle" in content):
    print("twinkle is present in the content")
else:
    print("twinkle is not present in the content")
f.close()


f = open("poems.txt")

content = f.read()

if("twinkle" in content):
    print("twinkle is present in the content")

else:
    print("twinkle is not present in the content")

f.close()