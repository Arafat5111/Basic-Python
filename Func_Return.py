def get_larger(x, y):
    if x > y:
        return x
    else:
        return y

larger_value = get_larger(23, 32)
print(larger_value)

def add_numbers(x, y):
    total = x + y
    return total
    print("This won't be printed")

print(add_numbers(4, 5))