# Use for, .split(), and if to create a Statement that will print out words that start with 's':

st = 'Print only the words that start with s in this sentence'
words = st.split()
for word in words:
    if word[0] == 's' and len(word) > 1:
        print(word)

# Use range() to print all the even numbers from 0 to 10.

range_array = range(1, 11)
for r in range_array:
    if r % 2 == 0:
        print(r)

# Use a List Comprehension to create a list of all numbers between 1 and 50 that are divisible by 3.

comprehension_array = [three_divided for three_divided in range(1, 51) if three_divided % 3 == 0]
print(comprehension_array)

# Go through the string below and if the length of a word is even print "even!"

even_string = 'Print every word in this sentence that has an even number of letters'
for even_word in even_string.split():
    if len(even_word) % 2 == 0:
        print(even_word + " even!")

# Write a program that prints the integers from 1 to 100.
# But for multiples of three print "Fizz" instead of the number, and for the multiples of five print "Buzz".
# For numbers which are multiples of both three and five print "FizzBuzz".

fizz = "Fizz"
buzz = "Buzz"
for int_num in range(1, 101):
    if int_num % 15 == 0:
        print(fizz + buzz)
    elif int_num % 3 == 0:
        print(fizz)
    elif int_num % 5 == 0:
        print(buzz)
    else:
        print(int_num)

# Use List Comprehension to create a list of the first letters of every word in the string below:

comprehension_string = 'Create a list of the first letters of every word in this string'
for letter in [word for word in comprehension_string.split()]:
    print(letter[0])