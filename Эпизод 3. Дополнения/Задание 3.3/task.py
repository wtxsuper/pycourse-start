def task_1(list):
    max = [0, 0]
    for item in list:
        if list.count(item) > max[0]:
            max[1] = item
            max[0] = list.count(item)
    return max[1]


def task_2(list_x, list_y):
    for i in range(len(list_x)):
        for j in range(len(list_y)):
            if list_x[i] == list_x[j] or list_y[i] == list_y[j]:
                return "YES"
            if abs(list_x[i] - list_x[j]) == abs(list_y[i] - list_y[j]):
                return "YES"
    return "NO"


def task_3(x, y, xc, yc, r):
    result = ((x - xc) * (x - xc)) + ((y - yc) * (y - yc)) <= r * r  # ур-е окружности
    return result


def task_4(list):
    counter = 0
    for i in range(1, len(list) - 1):
        if list[i] > list[i - 1] and list[i] > list[i + 1]:
            counter += 1
    return counter


def task_5(key):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    result = []
    with open('file.txt', 'r') as f:
        for line in f:
            result_line = ""
            nullified_line = line.strip()
            nullified_line = nullified_line.lower()
            for letter in nullified_line:
                result_index = alphabet.find(letter) + key
                result_line += alphabet[result_index]
            result.append(result_line)
    return result
