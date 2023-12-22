def factorial(number: int) -> int:
    """
    Gives the factorial of `number`

    :param number: Number to calculate factorial
    :return: the product of all the values from 1 to the number,
        inclusive.
    """
    if number == 0:
        return 1
    value1 = 1
    for i in range(1, number + 1):
        total = value1 * i
        value1 = total
    return total


for x, index in enumerate(range(36)):
    print(index, factorial(x))
