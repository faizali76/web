# Write a program to generate multiplication tables from 2 to 20 and write it to the different file.Place these file in a folder for a 13 year old.

def generateTable(n):
    table = ""
    for i in range (1, 11):
        table += f"{n} x {i} = {n*i}\n"

    with open(f"table/table_{n}.txt", "w") as f:
        f.write(table)



for i in range(2, 21):
    generateTable(i)