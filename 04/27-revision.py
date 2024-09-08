# print() function is used to print the output to the console.
print("Print->This is a cat. Meaow!")
print(5)
print(5.0)
print("string")
print([1, 2, 3])
print({"name": "John", "age": 30})

# type
print(type("string"))
print(type(5))

# string
"this is a string"
'this is also a string'
"""this is a 
multiline string"""
'''
this is also a
multiline string
'''
"this is a\ntwo line string"
a = 5
b = 6
f"this is a string with {a} and {b}"
f"{a=}, {b=}"
f"a={a}, b={b}"
c = 5678.123
f"{c=:.2f}"

# integer
-234523452345234
0
5

# float
5.0
42.1
500.0

# list
[1, 2, 3]
["a", "b", "c"]
[1, "a", 5.0]
[1, [2, 3], 4]
[1, {"name": "John", "age": 30}, 4]
[
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# dictionary
{"name": "John", "age": 30}
{"name": "John", "age": 30, "address": {"city": "New York", "state": "NY"}}
{1: "a", 2: "b", 3: "c"}

# variable
this_is_an_int = 1
print(this_is_an_int)
this_is_an_int = 2
print(this_is_an_int)

# function
def func_name(a, b):
    return a + b

def func_name2(a, b=5):
    return a + b

print(func_name2(1, 2))
print(func_name2(1))

# input
my_input = input("Enter a number: ")

# math operators
#+, -, *, /, //, %, **

# comparison operators -> boolean
# >, <, >=, <=, ==, !=
print(5 > 3)  # True

# conditionals if, elif, else
condition = 5 > 3
if condition:
    print("5 is greater than 3")
elif condition is False:
    print("5 is not greater than 3")
else:
    print("all checks not met")

# import
import random  # <- เอาไว้บนสุดของไฟล์
print(random.randint(1, 10))

# for loop
for i in range(5):
    print(i)

# while loop
i = 0
while i < 5:
    print(i)
    i += 1