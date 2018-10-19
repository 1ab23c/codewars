from functools import reduce

def digital_root(x):
    if x > 9:
        x_list = list(str(x))
        sum = reduce(lambda x, y: int(x) + int(y), x_list)
        return digital_root(sum)
    else:
        return x
