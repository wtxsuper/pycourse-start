def task_1(str):
    histogram = {}
    for letter in str:
        if letter.lower() in "abcdefghijklmnopqrstuvwxyz":
            if letter.lower() in histogram:
                histogram[letter.lower()] += 1
            else:
                histogram[letter.lower()] = 1
    return histogram

def task_2(list):

    list_unique = set(list)
    return sum(list_unique)


def task_3(cities):

    return ", ".join(cities) + '.'


def task_4(a, b):
    a = set(a)
    b = set(b)
    c = list(a & b)
    return c
