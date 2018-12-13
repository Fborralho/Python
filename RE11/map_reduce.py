import functools
def map_reduce(n1, n2):
    result = []
    for i in range(n1, n2+1):
        if i % 2 != 0 and i != 1:
            result.append(i ** 2)
    if functools.reduce(lambda x, y: x + y, result) >= 50:
        return functools.reduce(lambda x, y: x + y, result)
    else:
        return functools.reduce(lambda x, y: x * y, result)




