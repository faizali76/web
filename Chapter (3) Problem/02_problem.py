# write a program to fill in a letter template given below with name and date.
letter = '''Dear <|Name|>, 
You are selected!
 <|Date|>'''
print(letter.replace("<|Name|>","faiz").replace(" <|Date|>","18 december2024"))

