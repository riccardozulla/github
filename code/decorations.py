import functools
from time import perf_counter

def decorate(func):
    @functools.wraps(func)
    def inner(*args, **kargs):
        t0=perf_counter()
        res=func(*args, **kargs)
        t1=perf_counter()
        print(f"Elapsed time: {t1-t0}")
        return res

    return inner

@decorate
def complicated_things():
    return [i*2 for i in range(10)]

for i in complicated_things():
    print(i)

    