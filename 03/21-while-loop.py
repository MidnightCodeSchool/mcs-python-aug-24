"""
while <statement true/false>:
    <body>
"""

cur_num = 0
max_num = 5

while cur_num <= max_num:
    print(f"{cur_num=}")
    print(f"{max_num=}")
    print("-"*20)
    cur_num += 1

print("done")