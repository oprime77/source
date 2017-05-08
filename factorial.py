def factorial(count):
    if count == 0:
        return 1
    elif count > 0:
        return factorial(count - 1) * count

print(factorial(10))