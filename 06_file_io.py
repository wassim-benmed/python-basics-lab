f = open("text.txt", 'w')
Str = input("Please enter the content to be written: ")
f.write(Str)
f.close()

f = open("text.txt", 'r')
print(f.read(6))
print(f.read())
f.close()

with open("text1.txt", 'w') as f:
    f.write("python file operation")
with open("text1.txt", 'r') as f:
    print(f.read())