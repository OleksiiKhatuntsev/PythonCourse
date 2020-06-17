# Problem 1
# Handle the exception thrown by the code below by using try and except blocks.

def problem_one():
    try:
        for i in ['a','b','c']:
            print(i**2)
    except TypeError:
        print("some message")

# Problem 2
# Handle the exception thrown by the code below by using try and except blocks.
# Then use a finally block to print 'All Done.'

def problem_two():
    try:
        x = 5
        y = 0
        z = x/y
    except ZeroDivisionError:
        print("don't divide by zero, bitch")
    finally:
        print("All Done")

# Problem 3
# Write a function that asks for an integer and prints the square of it.
# Use a while loop with a try, except, else block to account for incorrect inputs.

def problem_three():
    result = 0
    while True:
        try:
            result = int(input("Enter a number"))**2
        except ValueError:
            print('Write a number, bitch')
            continue
        else:
            return result

problem_one()
problem_two()
print(problem_three())