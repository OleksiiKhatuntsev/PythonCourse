# LESSER OF TWO EVENS: Write a function that returns the lesser of two given numbers if both numbers are even,
# but returns the greater if one or both numbers are odd

def get_a_number_from_number_set(a, b):
    if a % 2 == 0 and b % 2 == 0:
        return max(a, b)
    else:
        return min(a, b)

# ANIMAL CRACKERS: Write a function takes a two-word string and returns True if both words begin with same letter

def check_for_same_letter(my_string):
    if my_string.split()[0][0] == my_string.split()[1][0]:
        return True
    else:
        return False

# MAKES TWENTY: Given two integers, return True if the sum of the integers is 20 or if one of the integers is 20.
# If not, return False

def makes_twenty(num1, num2):
    if num1 == 20 or num2 == 20 or num1 + num2 == 20:
        return True
    else:
        return False

# OLD MACDONALD: Write a function that capitalizes the first and fourth letters of a name

def old_macDonald(name):
    converted_name = ''
    count = 0
    for letter, in name:
        if count == 0 or count == 3:
            converted_name += letter.upper()
        else:
            converted_name += letter
        count += 1
    return converted_name

# MASTER YODA: Given a sentence, return a sentence with the words reversed

def master_yoda(test):
    test_array = [word for word in test.split()]
    test_array.reverse()
    result = ' '
    return result.join(test_array)

#ALMOST THERE: Given an integer n, return True if n is within 10 of either 100 or 200

def almost_there(num):
    return num in range(10, 101) or num == 200

# FIND 33: Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.

def has_33(nums):
    count = 0
    while count < len(nums) - 1:
        if nums[count] == 3 and nums[count + 1] == 3:
            return True
        else:
            count += 1
    return False

# PAPER DOLL: Given a string, return a string where for every character in the original there are three characters

def paper_doll(text):
    result = ''
    for letter in text:
        result += letter*3
    return result

# BLACKJACK: Given three integers between 1 and 11, if their sum is less than or equal to 21, return their sum.
# If their sum exceeds 21 and there's an eleven, reduce the total sum by 10.
# Finally, if the sum (even after adjustment) exceeds 21, return 'BUST'

def blackjack(a, b, c):
    sum = a + b + c
    if sum <= 21:
        return sum
    elif 11 in (a, b, c):
        return sum - 10
    else:
        return 'BUST'

# SUMMER OF '69: Return the sum of the numbers in the array, except ignore sections of numbers starting with a 6
# and extending to the next 9 (every 6 will be followed by at least one 9). Return 0 for no numbers.

def summer_69(nums):
    result = 0
    flag = True
    for num in nums:
        if num == 6:
            flag = False
        if flag:
            result += num
        if num == 9:
            flag = True
    return result

# SPY GAME: Write a function that takes in a list of integers and returns True if it contains 007 in order

def spy_game(nums):
    count = 0
    while count < len(nums) - 2:
        if nums[count] == 0 and nums[count + 1] == 0 and nums[count + 2] == 7:
            return True
        else:
            count += 1
    return False

# COUNT PRIMES: Write a function that returns the number of prime numbers that exist up to and including a given number

def count_primes(num):
    result = 0
    for count in range(2, num + 1):
        flag = True
        for checknum in range(2, count):
            if count % checknum == 0:
                flag = False
        if flag:
            result += 1
        flag = True
    return result

# PRINT BIG: Write a function that takes in a single letter, and returns a 5x5 representation of that letter

def print_big(letter):
    a = '  *\n * *\n*****\n*   *\n*   *'
    b = '****\n*   *\n****\n*   *\n****'
    c = ' ***\n*   *\n*\n*   *\n ***'
    d = '****\n*   *\n*   *\n*   *\n****'
    e = '*****\n*\n*****\n*\n*****'
    if letter == 'a':
        return a
    elif letter == 'b':
        return b
    elif letter == 'c':
        return c
    elif letter == 'd':
        return d
    elif letter == 'e':
        return e

print(get_a_number_from_number_set(2, 4))
print(get_a_number_from_number_set(2, 5))

print(check_for_same_letter("test takitest"))
print(check_for_same_letter("test netest"))

print(makes_twenty(10, 20))
print(makes_twenty(20, 1))
print(makes_twenty(18, 2))

print(old_macDonald("macdonald"))

print(master_yoda("my string here"))

print(almost_there(35))
print(almost_there(10))
print(almost_there(9))
print(almost_there(100))
print(almost_there(200))

print(has_33([3,3,2,1]))
print(has_33([2,3,2,3]))

print(paper_doll('Mississippi'))
print(paper_doll('Hello'))

print(blackjack(5,6,7))
print(blackjack(9,9,9))
print(blackjack(9,9,11))

print(summer_69([1, 3, 5]))
print(summer_69([4, 5, 6, 7, 8, 9]))
print(summer_69([2, 1, 6, 9, 11]))

print(spy_game([1,2,4,0,0,7,5]))
print(spy_game([1,0,2,4,0,5,7]))
print(spy_game([1,7,2,0,4,5,0]))

print(count_primes(100))

print(print_big('a'))
print(print_big('b'))
print(print_big('c'))
print(print_big('d'))
print(print_big('e'))