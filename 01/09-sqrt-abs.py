# """
# Advanced topic for class I, skippable
# """
# from math import sqrt

# print(sqrt(9))
# print(abs(-5))


def hello():
    name = input("What is your name: ")
    if not name:
        print("ENTER YOUR NAME!")
        return

    print("Hello, " + name)

hello()