d = {
    "name": "Sprigatito",
    "type": "wood",
    "species": "feline"
}

# Advanced error handling
# try:
#     divided_by_zero = 1 / 0 # ZeroDivisionError
#     print(d["hp"]) # KeyError
# except KeyError:
#     print("Key hp does not exist")
# except ZeroDivisionError:
#     print("Cannot divide by zero")

try:
    print(d["hp"]) # KeyError
except Exception:
    print("An error occurred: hp does not exist")
