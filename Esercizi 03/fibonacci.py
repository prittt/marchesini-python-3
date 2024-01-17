# # Fibonacci
#       0, se n = 0
# F(n)  1, se n = 1
#       F(n - 1) + F(n - 2), altrimenti

# F(0) = 0
# F(1) = 1
# F(2) = F(0) + F(1) = 1 
# F(3) = 2
# F(4) = 3

def fib_decorator(fun):
    results = [None] * 51
    def wrapper(n):
        if results[n] is None:
            results[n] = fun(n)
        return results[n]
    return wrapper

# def decorator(fun):
#     def wrapper(*args):
#         n = args[0]
#         pass

def fib(n):
    ncall = 0
    @fib_decorator
    def fib_rec(n):
        nonlocal ncall
        ncall += 1
        if n <= 1: 
            return n

        return fib_rec(n - 1) + fib_rec(n - 2)

    res = None
    if 0 <= n <= 50 : 
        res = fib_rec(n)
    
    print(f"La funzione fib_rec per {n=} è stata invocata {ncall} volte. Il risultato è {res}.")

fib(-1)
fib(0)
fib(1)
fib(2)
fib(5)

