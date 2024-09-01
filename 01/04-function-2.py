# Function (user-defined)
# def function_name(argument):
#     """
#     docstring
#     """
#     return result

def hello():
    """
    Print "Hello, World!".
    """
    print("Hello, World!")

def add_one(number: int) -> int:
    """
    Add one to the input number.
    """
    print("user put in:")
    print(number)
    print("-----")
    return number + 1

def sum_two_nums(a: int, b: int) -> int:
    """
    Sum two numbers.
    """
    return a + b

def sum_two_nums_say_hello_then_print(a: int, b: int) -> int:
    """
    Sum two numbers and print "Hello, World!".
    print the sum.
    return the sum.
    """
    result = a + b
    hello()
    print(result)
    return result




# hello()
# print(add_one(5))
# print(sum_two_nums(5, 6))
print(sum_two_nums_say_hello_then_print(5, 6))