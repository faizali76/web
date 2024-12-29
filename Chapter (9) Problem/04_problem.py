# A file contains a word "Donkey" multiple times.You need to with a program which replaces this word with ###### by updateing the same file.

# word = "donkey"

# Step 1: File ko read mode mein open karke content read karo

# with open("file.txt", "r") as f :
#       content = f.read()

# Step 2: Replace karo variable 'word' ki value with "#####"

# content = content.replace(word,"#####")

# Step 3: File ko write mode mein open karke updated content likho

# with open("file.txt", "w") as f:
#       f.write(content) 

#  STEP BY STEP UPER HAI 👆 ↑ ↓

# word = "donkey"

# with open("file.txt", "r") as f:
#     content = f.read()

# content = content.replace(word,"####")

# with open("file.txt", "w") as f:
#      f.write(content)

word = "Donkey"

with open("file.txt", "r") as f :
    content = f.read()

content = content.replace(word , "#####")

with open("file.txt", "w") as f :
    content = f.write(content)