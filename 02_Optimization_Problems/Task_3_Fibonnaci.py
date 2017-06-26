# RECURSIVE IMPLEMENTATION OF FIBONNACI

def fib(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

# USING MEMO TO COMPUTE FIBONACI

def fastFib(n, memo = {}):
    """Assumes n is an int >= 0, memo used only by recursive calls
    Returns Fibonacci of n"""

    if n == 0 or n == 1:
        return 1

    try:
        return memo[n]
    except KeyError:
        result = fastFib(n - 1, memo) + fastFib(n - 2, memo)
        memo[n] = result
        return result

for i in range(121):
    print('fib(' + str(i) + ') =', fastFib(i))