import math
# Пример 1
def task_1(A):
    sum = 0
    for element in A:
        if element >= 0:
            sum += element
    return sum


# Пример 2
def task_2(A):
    result = sum(A) / len(A)
    return result


# Пример 3
def task_3(A):
    deviation = 0
    average = sum(A) / len(A)
    for element in A:
        deviation += (element - average) ** 2
    deviation = math.sqrt(deviation / len(A))
    return deviation
