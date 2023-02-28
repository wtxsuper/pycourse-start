import math

# Пример 1
def task_1(n):
    n = 10
    x = 0
    for i in range(1, n + 1):
        x += 1 / i
    return x


# Пример 2
def task_2(x, n):
    n = 17
    x = 0
    y = 1
    for i in range(1, n + 1, 2):
        x += y / i
    return x


# Пример 3
def task_3(n):
    n = 10
    x = math.factorial(n)
    return x


# Пример 4
def task_4(x, n):
    n = 9
    x = 1
    y = 1
    for i in range(2, n + 1):
        x *= (y + i) / i
    return x


# Пример 5
def task_5(x, n):
    n = 3
    x = 0
    y = 1
    for i in range(1, n + 1):
        x += (y * i) / (2 * i)
    return x


# Пример 6
def task_6(n):
    x = 1
    for i in range(2, 20 + 2, 2):
        x *= i
    return x

