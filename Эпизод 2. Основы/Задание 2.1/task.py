def task_1(N):
    f = 1
    if N < 0:
        return
    elif N == 0:
        return 1
    else:
        for i in range(1, N + 1):
            f *= i
    return f


def task_2(N):
    a = 0
    b = 1
    for i in range(3, N + 1):
        c = a + b
        a = b
        b = c
    return b


def task_3(N):
    result = []
    for i in range(1, N + 1):
        if N % i == 0:
            result.append(i)
    return result
