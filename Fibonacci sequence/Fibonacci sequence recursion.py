# cache-dictionary declaration,
# as we know the 0th and 1st Fibonacci's number
# this is also the base case of recursion
sequence = {0: 0, 1: 1}


# the function first checks whether the needed number is in the dictionary,
# if so, it retrieves it from the dictionary,
# if not, it calculates it recursively and then saves it to the dictionary for reuse
def recursion_Fibonacci(n):
    if n in sequence:
        return sequence[n]
    sequence[n] = recursion_Fibonacci(n - 1) + recursion_Fibonacci(n - 2)
    return sequence[n]


# getting the value from the user and converting the type from string to int
numbers = int(input("How many Fibonacci numbers you want to display? "))

# calling a function for a value provided by the user
recursion_Fibonacci(numbers)

# displaying the content of the dictionary up to the value provided by the user
# when the value is 0, the entire dictionary is not displayed, but only the 0th number
for i in range(numbers + 1):
    print(sequence[i], end=" ")

# calculating the golden ratio value
# and handling an exception if the sequence is too short
try:
    print("\n\nThe golden ratio of the two largest numbers in the range is", sequence[numbers] / sequence[numbers - 1])
except (ZeroDivisionError, KeyError):
    print("\n\nThe sequence must contain at least 3 numbers to calculate the golden ratio.")

