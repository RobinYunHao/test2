"""***row = 7
for i in range(row):
    print(i)
    for _i in range(i + 1):
        print("r", end = '')
    print("u")"""
'''for m in range(1,100):
    for y in range(1,100):
        u = m % y
        print(u)
        i =isinstance(u,int)'''
import math

for num in range(2, 100):
    is_prime = True
    for factor in range(2, int(math.sqrt(num)) + 1):
        if num % factor == 0:
            is_prime = False
            break
    if is_prime:
        print(num, end=' ')