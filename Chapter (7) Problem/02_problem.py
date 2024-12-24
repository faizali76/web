# Write a program to great all the person names stored in a list L1 and which starts with S.
l = ["faiz", "ali", "faiyaz", "faizan"]

for name in l:
    if(name.startswith("f")):
        print(f"hello {name}")