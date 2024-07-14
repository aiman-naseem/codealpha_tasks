#code_alpha task # 01
#fibonacci generator
def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    
    fib_series = [0, 1]
    for i in range(2, n):
        next_term = fib_series[-1] + fib_series[-2]
        fib_series.append(next_term)
    
    return fib_series
# Take input from the user
n = int(input("Enter the number of terms for the Fibonacci series: "))

# Generate and print the Fibonacci series
print(fibonacci(n))
