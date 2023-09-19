sequence = {0: 0, 1: 1}

def recursion_Fibonacci(n):
    if n in sequence:
        return sequence[n]
    sequence[n] = recursion_Fibonacci(n - 1) + recursion_Fibonacci(n - 2)
    return sequence[n]


n = int(input("How many Fibonacci numbers you want to display? "))

recursion_Fibonacci(n)

for i in sequence:
    print(sequence[i])

print("The golden ratio of the two largest numbers in the range is", sequence[n] / sequence[n - 1])
