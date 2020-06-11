import math
import string

# Write a function that computes the volume of a sphere given its radius.

def vol(rad):
    return 4 / 3 * rad ** 3 * math.pi

# Write a function that checks whether a number is in a given range (inclusive of high and low)

def ran_check(num, low, high):
    return num in range(low, high + 1)

# Write a Python function that accepts a string and calculates the number of upper case letters and lower case letters.

def up_low(text):
    lower_case_count = 0
    upper_case_count = 0
    symbols_count = 0
    for symbol in text:
        if symbol in string.ascii_lowercase:
            lower_case_count += 1
        elif symbol in string.ascii_uppercase:
            upper_case_count += 1
        else:
            symbols_count += 1
    return f'Original string: {text}\nLower case characters: {lower_case_count}\nUpper case characters: {upper_case_count}\nSymbols: {symbols_count}'

# Write a Python function that takes a list and returns a new list with unique elements of the first list.

def unique_list(my_list):
    return list(set(my_list))

# Write a Python function to multiply all the numbers in a list.

def multiply_list(numbers):
    result = 1
    for number in numbers:
        result *= number
    return result

# Write a Python function that checks whether a word or phrase is palindrome or not.

def palindrome(text):
    text = text.replace(' ', '')
    return text == text[::-1]

# Write a Python function to check whether a string is pangram or not.
# (Assume the string passed in does not have any punctuation)

def is_pangram(text):
    st = "qwe"
    st1 = "qwe"
    print(f'res = {st == st1}')
    text = text.lower()
    text = set(text)
    text = list(text)
    text.sort()
    result = ''
    for symbol in text:
        result += symbol
    return string.ascii_lowercase in result

print(vol(2))

print(ran_check(4, 1, 10))

print(up_low('Hello Mr. Rogers, how are you this fine Tuesday?'))

print(unique_list([1,1,1,1,2,2,3,3,3,3,4,5]))

print(multiply_list([1,2,3,-4]))

print(palindrome('heyy eh'))

print(is_pangram("The quick brown fox jumps over the lazy dog"))