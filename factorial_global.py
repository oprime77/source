def factorial(num):
    global sum
    sum *= num
    if num == 1:
        return sum
    else:
        num -= 1
        return factorial(num)
sum=1
print(factorial(5))
