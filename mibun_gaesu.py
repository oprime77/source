def numerical_diff(f, x):
    delta = 0.0001  # 1e-4로 해도된다
    return (f(x + delta) - f(x - delta)) / (2 * delta)

def function_1(x):
    return 2 * pow(x, 2) + 1


print(numerical_diff(function_1, -2))