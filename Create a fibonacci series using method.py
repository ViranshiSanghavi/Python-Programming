#Create a fibonacci series using method

def generate_fibonacci(n):
    fibonacci_series = [0, 1]

    while len(fibonacci_series) < 10:
        next_number = fibonacci_series[-1] + fibonacci_series[-2]
        fibonacci_series.append(next_number)

    return fibonacci_series

n = int(input("Enter the number of terms in the Fibonacci series: "))

fib_series = generate_fibonacci(n)
print("Fibonacci series:", fib_series)
