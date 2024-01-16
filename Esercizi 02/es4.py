import random
import time
import functools

def dummydecorator(fun):
    @functools.wraps(fun)
    def wrapper(*args):
        print("dummydecorator is running")
        return fun(*args)
    return wrapper

def calctime(fun):
    @functools.wraps(fun)
    @dummydecorator
    def wrapper(*args):
        start = time.time()
        ret = fun(*args)
        end = time.time()
        print(f"La funzione {fun.__name__} ha impiegato {end - start} s")
        return ret
    return wrapper

# O(n^2)
@calctime
def nodup_v1(a : list):
    ret = []
    for e in a:
        if e not in ret:
            ret.append(e)

    return ret

# O(n + n*log n)
def nodup_v2(a : list):
    a = a[:]
    a.sort()
    ret = a[:1]
    
    for i in range(1, len(a)):
        if a[i] != ret[-1]:
            ret.append(a[i])
            
    return ret

# O(n)
def nodup_v3(a : list):
    return list(set(a))




def donothing():
    for i in range(1, 10000):
        pass

# a = []
# for i in range(1, 10000):
#     a.append(random.randint(1, 10000))

# a = [4, 1, 1, 4, 7, 9, 7] 
a = range(1, 10000)
a = list(a)

nodup_v1(a)

help(nodup_v2)
help(nodup_v1)

# calctime(nodup_v2, a)
# calctime(nodup_v3, a)
# calctime(donothing)