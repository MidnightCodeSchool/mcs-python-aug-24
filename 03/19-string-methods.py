my_string = "hello world"
print(my_string[0])
print(my_string[1])
print(my_string[-1])
for char in my_string:
    print(char)
print(my_string[3:])
print(my_string[:-1])
print(my_string[1:3])

print("hello" in my_string)
print("hellox" in my_string)

my_string2 = "hello" + " " + "world"
print(my_string2)

my_string3 = "hello wORLD, i am a string."
print(my_string3.upper())
print(my_string3.lower())

print(my_string3.isalnum())  # False
print("123abc".isalnum())  # True
print("123".isalpha())  # False
print("abc".isalpha())  # True
print("123".isdigit())  # True
print("abc".isdigit())  # False

my_string4 = "hello world"
print(my_string4.split(" ")) 

my_string5 = "1,2,3,4,5"
print(my_string5.split(","))

my_list = ["1", "2", "3", "4", "5"]
print(",".join(my_list))