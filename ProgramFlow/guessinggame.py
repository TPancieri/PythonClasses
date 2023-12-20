import random

highest = 1000
answer = random.randint(1, highest)

guess = 0

print("Please guess a number between 1 and {}: ".format(highest))
while guess != answer:
    guess = int(input())

    if guess == answer:
        print("Well done, you guessed it")
        break
    elif guess == 0:
        print("Exited game")
        break
    else:
        if guess < answer:
            print("Please guess higher")
        else:
            print("Please guess lower")

# if guess == answer:
#     print("You got it first time")
# else:
#     if guess < answer:
#         print("Please guess higher")
#     else:
#         print("Please guess lower")
#     guess = int(input())
#     if guess != answer:
#         print("Sorry, you have not guessed correctly")
#     else:
#         print("Well done, you have guessed it")
