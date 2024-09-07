pokemon1 = {
    "name": "Pikachu",
    "type": "Electric",
    "hp": 35,
    "attack": 55,
    "defense": 40,
}
print(pokemon1)
print("name", pokemon1["name"])
print("type", pokemon1["type"])

pokemon1["speed"] = 90
print(pokemon1)
pokemon1["speed"] = 95
print(pokemon1)
del pokemon1["speed"]
print(pokemon1)

print(pokemon1.keys())
print(pokemon1.values())