z=complex(10,-10)
print(z.real)
print(z.imag)

string = "Hello, World!"
print(string[0])
print(string[7])

greeting = "Hello"
name = "Son"
message = greeting + " , " + name + "!"
print(message)

word = "spam"
repeat = word*3
print(repeat)

string = "Hello, World!"
position = string.find("World")
print(position)

a = True
b = False

print(a and b)
print(a or b)
print(not a)

num = 10
text = "apple"
print(str(num) + text)

num = 10
float_num =float(num)
str_num = str(num)
bool_num = bool(num) 

fruits = ["apple", "banana", "cherry"]
print(fruits)
print(fruits[1])
fruits[1] = "orange"
print(fruits)

fruits = {"apple":3, "banana":2, "cherry":5}
print(fruits)
print(fruits["banana"])
fruits["orange"] = 4
print(fruits)

print("Hello, world!")

firstname = "ByeongHee"
lastname = "Son"
age = 31
print("Myname is {} {} and I am {} years old.".format(firstname, lastname, age))

firstname = "ByeongHee"
lastname = "Son"
age = 31
print("My name is {} {} and I am {} years old.".format(firstname, lastname, age))

name = "Tom"
age = 20
print(f"My name is {name} and I am {age} years old.")