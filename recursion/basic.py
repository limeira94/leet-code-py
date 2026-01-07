def sum_numbers_recursive(numbers):
    if len(numbers) == 0:
        return 0
    print(numbers)
    return numbers[0] + sum_numbers_recursive(numbers[1:])


def sum_numbers(numbers):
    summ = 0
    for num in numbers:
        summ += num

    return summ


def factorial_recursive(n):
    if n < 0:
        return "no factorial negative"
    elif n == 0:
        return 1
    else:
        return n * factorial_recursive(n - 1)


print(factorial_recursive(5))
