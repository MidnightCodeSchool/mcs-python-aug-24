"""
fizz buzz: while loop
Print numbers from 1 to 100. 
If the number is divisible by 3, print fizz instead of the number.
If the number is divisible by 5, print buzz instead of the number.
If the number is divisible by both 3 and 5, print fizzbuzz instead of the number.
# แปลไทย
fizz buzz: while loop
พิมพ์เลขตั้งแต่ 1 ถึง 100
ถ้าเลขนั้นหารด้วย 3 ลงตัว ให้พิมพ์ fizz แทนเลขนั้น
ถ้าเลขนั้นหารด้วย 5 ลงตัว ให้พิมพ์ buzz แทนเลขนั้น
ถ้าเลขนั้นหารด้วยทั้ง 3 และ 5 ลงตัว ให้พิมพ์ fizzbuzz แทนเลขนั้น
"""

num = 1
max_num = 100

while num <= max_num:
    if num % 3 == 0 and num % 5 == 0:
        print("fizzbuzz")
    elif num % 3 == 0:
        print("fizz")
    elif num % 5 == 0:
        print("buzz")
    else:
        print(num)
    num += 1