def is_narcissistic(i):
    nums = list(str(i))
    print(nums)
    _sum = reduce(lambda x, y: x + y, [int(q) ** len(nums) for q in nums])
    if _sum == i:
        return True
    else:
        return False
