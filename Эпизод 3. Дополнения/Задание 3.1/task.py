def task_1(text):
    text += " "
    dict = {}
    sequences = text.split(". ")
    for sequence in sequences:
        if sequence == '':
            continue
        dict[sequence] = len(sequence.split())
    return dict


def task_2(x1, y1, x2, y2):
    result = ((x1-x2)**2 + (y1-y2)**2) ** 0.5
    return result