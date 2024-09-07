count = 0
count2 = 0

while True:
    count += 1
    if count == 2:
        continue
    count2 += 1
    print(f"{count=}")
    print(f"{count2=}")
    if count >= 5:
        break

print("done")