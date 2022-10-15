# defining a function
def add(a, b):
    print(f"ADDING {a} + {b}")
    return a + b


print(add(55, 1))

# defining a function with default values


def add_default(a, b=10):
    print(f"ADDING {a} + {b}")
    return a + b


print(add_default(55))

# defining a function with a variable number of arguments


def add_many(*args):
    print("Adding many numbers", args)
    return sum(args)


print(add_many(1, 2, 3, 4, 5))

# defining function with multiple return values


def sumDif(x, y):
    sum = x + y
    dif = x - y
    return sum, dif


print(sumDif(10, 5))
