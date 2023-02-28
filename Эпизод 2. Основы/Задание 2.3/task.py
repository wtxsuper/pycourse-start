# todo: replace this with an actual task
def task_1(str):
    words = str.split()
    length_last = len(words[-1])
    return length_last


def task_2(str):
    words = str.split()
    for i in range(0, len(words) - 1, 2):
        words[i], words[i+1] = words[i + 1], words[i]
    print(' '.join(words))
    return ' '.join(words)


def task_3(str):
    words = str.split()
    counter = 0
    for i in range(1,  len(words)):
        if words[i][0] == words[i-1][-1]:
            counter += 1
    return counter
