new_iter = []


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
    return new_iter


def sum_decorator(func):
    def inner(args):
        return func(flatten_iter(args))
    return inner


@sum_decorator
def adder(obj):
    addr = 0
    for i in obj:
        addr = addr + i
    return obj, addr

print((adder([1, 2, 3, ([4, 5]), [6], [[7], [8, 9]]])))
