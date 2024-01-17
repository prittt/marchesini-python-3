

# def print_decorator(func):
#     def wrapper():
#         # cose (opzionale)
#         ret = func()
#         # cose (opzionale)
#         return ret
#     return wrapper


# # Fibonacci
#       0, se n = 0
# F(n)  1, se n = 1
#       F(n - 1) + F(n - 2), altrimenti


# a = 12
# def myfun():
#     a = 32
#     def myfun2():
#         nonlocal a
#         a += 12
    
#     myfun2()
#     print(a)

# myfun()
# print(a)

def decorator(fun):
    def wrapper(*args,**kwargs):
        global print
        tmp = print
        def print(*args,**kwargs):
            tmp('-- Marchesini -- ', end='')
            tmp(*args, **kwargs)
        ret = fun(*args, **kwargs)
        print = tmp
        return ret
    return wrapper
        

@decorator
def myfun1():
    print('myfun1-a')
    print('myfun1-b')


def myfun2():
    print('myfun2-a')
    print('myfun2-b')


myfun1()
myfun2()
myfun1()
myfun2()