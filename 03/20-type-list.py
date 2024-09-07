list1 = [1,2,3,4]
list2 = [5,6,7,"eight"]
list3 = [5,6,7,"eight", 1.1, {"a": 5}]

for item in list1:
    print(item)
print("-"*20)
print(list1[0])
print(list1[-1])
print(list1[1:-1])
print(list1[1:])
print(len(list3))
print(len("hello"))