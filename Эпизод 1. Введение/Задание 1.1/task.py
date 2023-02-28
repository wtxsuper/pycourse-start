import math

# Пример 1
def task_1(a, d, c):
    result = (c - d/5 + 321 ** 0.5) / (1 + a * 3)
    return result


# Пример 2
def task_2(a, d, c):
    result = (math.log10(c/3)-d+25)/(a*5-1)
    return result


# Пример 3
def task_3(a, d, c):
    result = (c/2+math.log(d)-35)/(a*5+1)
    return result


# Пример 4
def task_4(a, d, c):
    result = (math.tan(c)+d/32)/(a/3+1)
    return result


# Пример 5
def task_5(a, d, c):
    result = (c/5-d+1)/(c+math.tan(2*a))
    return result


# Пример 6
def task_6(a, d, c):
    result = (math.sqrt(25*c)+d-3)/(d-a*a+1)
    return result


# Пример 7
def task_7(a, d, c):
    result = (5*math.log10(c)+3*d-32)/(a*a+1)
    return result


# Пример 8
def task_8(a, d, c):
    result = (c*d-math.log(4*3*a))/(c+a-1)
    return result
