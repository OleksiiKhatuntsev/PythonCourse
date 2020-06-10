import random
guessing_number = random.randint(1, 100)
user_guess = []
while True:
    user_guess.append(int(input("guess a number: ")))
    if user_guess[-1] < 1 or user_guess[-1] > 100:
        print("OUT OF BOUNDS")
    elif user_guess[-1] == guessing_number:
        print("YOU WIN")
        break
    elif len(user_guess) == 1:
        if abs(user_guess[-1] - guessing_number) <= 10:
            print("WARM")
        else:
            print("Cold")
    elif abs(user_guess[-1] - guessing_number) < abs(user_guess[-2] - guessing_number):
        print("WARMER")
    else:
        print("Colder")