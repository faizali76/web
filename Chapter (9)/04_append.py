# Jitne bar ham code ko run karenge utna bar add hota jaye ga

st = "hay Faiz you are amazing "

f = open("myfile.txt", "a")

f.write(st)

f.close()

f = open("myfile.txt", "r")
content = f.read()  # File ka content read karna
print("Faiz is bignner for pyrhon programming :")
print(content)
f.close()