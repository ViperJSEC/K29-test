'''def F(n):                   # 1-я задача
    if n == 1:
        return 1
    if n % 2 != 0 and n > 1:
        return n + F(n - 2)
    if n % 2 == 0:
        return n * F(n - 1)
print(F(40))
'''
'''def F(n):                   # 2-я задача
    if n == 0:
        return 0
    if n % 3 == 0 and n > 0:
        return n + F(n - 3)
    if n % 3 > 0:
        return n + F(n - n % 3)
print(F(26))
'''
'''def F(n):                   # 3-я задача
    if n == 0:
        return 0
    if n % 2 == 0:
        return F(n // 2)
    if n % 2 != 0:
        return 1 + F(n - 1)

for i in range(1,10000):
    if F(i) == 11:
        print(i)
        break
'''
'''def F(n):                   # 4-я задача
    if n == 0:
        return 0
    if n > 0 and n % 3 == 0:
        return F(n // 3)
    if n % 3 > 0:
        return n % 3 + F(n - n % 3)

for i in range(1,10000):
    if F(i) == 9:
        print(i)
        break
'''
'''def F(n):                   # 5-я задача
    if n == 0:
        return 0
    if n > 0 and n % 2 == 0:
        return F(n // 2)
    if n % 2 != 0:
        return 1 + F(n - 1)

s = 0

for i in range(1,501):
    if F(i) == 8:
        s += 1
print(s)
'''
'''import sys                 # 9-я задача
sys.setrecursionlimit(10**9)
def F(n):
    if n < 11:
        return 10
    if n >= 11:
        return n + F(n - 1)
print(F(2024) - F(2022))
'''
'''import sys                 # 6-я задача
sys.setrecursionlimit(10**9)
def F(n):
    if n < 11:
        return 10
    if n >= 11:
        return n + F(n - 1)
print(F(2021) - F(2019))
'''
'''import sys                 # 8-я задача
sys.setrecursionlimit(10**9)
def F(n):
    if n > 2024:
        return n
    if n <= 2024:
        return n * F(n + 1)
print(F(2022) // F(2024))
'''
'''def F(n):                  # 7-я задача
    if n == 1:
        return 1
    if n > 1:
        return F(n - 1) + 2 ** (n - 1)
print(F(10))
'''