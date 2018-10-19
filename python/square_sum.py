from functools import reduce


def square_sum(numbers):
    if numbers is None or len(numbers) == 0:
        return 0
    else:
        return reduce(lambda x, y: x + y, [z ** 2 for z in numbers])
