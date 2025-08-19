text = input("Enter any string: ")
a = ""
for i in text:
    if i.isalpha():
        a+=i
b = a.capitalize()
print(b)
print(a)