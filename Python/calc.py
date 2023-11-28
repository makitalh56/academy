def add(x, y):
    return x + y

def multiply(x, y):
    return x * y

def power(x, y):
    """Calculate x raised to the power y without using math.pow."""
    result = 1
    for _ in range(int(y)):
        result *= x
    return result

print(add(5,4))       # --> 9
print(multiply(3,4))  # --> 12
print(power(2,8))     # --> 256