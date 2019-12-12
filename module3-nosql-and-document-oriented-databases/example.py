# In class example follow along:

def increment(x):
    return x + 1

def double(x):
    return x*2

def run_twice(fun,x):
    return fun(fun(x))

def rec_print(n):
    print(n)
    if n >= 1:
        rec_print(n-1)

def add(x,y):
    return x + y

def identify(X):
    return x
