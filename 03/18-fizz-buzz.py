"""
fizz buzz: for loop
Print numbers from 1 to 100. 
If the number is divisible by 3, print fizz instead of the number.
If the number is divisible by 5, print buzz instead of the number.
If the number is divisible by both 3 and 5, print fizzbuzz instead of the number.
"""
# range(start, stop) เหมือนกับ function ที่สร้าง list ที่มีเลข start ไปถึง stop - 1, แต่จะค่อยๆคืนเลขมาทีละตัว

for num in range(1, 100 + 1):
    if num % 3 == 0 and num % 5 == 0:
        print("fizzbuzz")
    elif num % 3 == 0:
        print("fizz")
    elif num % 5 == 0:
        print("buzz")
    else:
        print(num)