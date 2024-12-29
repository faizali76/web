st = "hay Faiz you are amazing "

f = open("myfile.txt", "w")

f.write(st)

f.close()

f = open("myfile.txt", "r")
content = f.read()  # File ka content read karna
print("Faiz is bignner for pyrhon programming :")
print(content)
f.close()