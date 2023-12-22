# fizz buzz
# if the number is divisible by 3 say fizz
# if the number is divisible by 5 say buzz
# if is divisible by both say FizzBuzz

def fizz_buzz(number: int) -> str:
    """
    Prints Fizz when `number` is divisible by 3, Fuzz when
    `number` is divisible by 5, and FizzBuzz when it's divisible by both

    :param number: Number to check for FizzBuzz
    :return: `fizz` if `number` % 3 == 0
        `buzz` if `number % 5 ==0
        `fizzbuzz` if both fizz and buzz apply
        otherwise returns the number as a string
    """
    if number % 15 == 0:
        return "FizzBuzz"
    elif number % 3 == 0:
        return "Fizz"
    elif number % 5 == 0:
        return "Buzz"
    return str(number)


for i in range(1,101):
    print(fizz_buzz(i))
