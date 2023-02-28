def task_1(list, search):
    result = str(list.index(search))
    return result

def task_2(x):
    is_prime = True
    for i in range(2, x):
        if x % i == 0:
            is_prime = False
            break
    return is_prime