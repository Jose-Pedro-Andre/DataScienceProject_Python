import sys 

def ft_filter(func, iterable) -> iter:
    if func is None:
        return iterable
    for i in iterable:
        if func(i): 
            yield i
def is_alpha(a):
    if a == 'a' : return True
    return False

# print((ft_filter(is_alpha, "iterableaaa")))
# print((filter(is_alpha, "iterableaaa")))