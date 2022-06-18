new_iter = []

def flatten_decorator(func):
    def flatten_iter(obj):
        for num in obj:
            if isinstance(num, list):
                flatten_iter(num)
            elif isinstance(num, tuple):
                flatten_iter(num)
            elif isinstance(num, dict):
                flatten_iter(num.values())
            else:
                new_iter.append(num)

        return func(new_iter)
    return flatten_iter

def sum_decorator(func):
    def inner(args):
        addr = 0
        for i in args:
            addr = addr + i
        return func(addr)
    return inner

@flatten_decorator
@sum_decorator
def adder(obj):
    return obj


x = [1, (2, 3), [4, 5], [6], [[7], [8, 9]]]
print(flatten_decorator(x))

print(adder(x))
