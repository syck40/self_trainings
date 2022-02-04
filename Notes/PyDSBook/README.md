# Primer

- identifier
temp = 98
identifier = expression

- mutable parameter
- positional arg
- type checking at runtime
```
def sqrt(x):
    if not isinstance(x, (int, float)):
        raise TypeError('x must be numeric')
    elif x <0:
        raise ValueError('x must be positive')
```
- error handling
"look before you leap" vs "easier to ask for forgiveness than it is to get permission(try/except)" 
use try to skip loop iteration
```
while a < b:
    try:
        do_something()
    except ValueError:
        pass
    except EOFError:
        raise
    finally:
        clean_up()
```
- iterator is an object let next(i) produce the next element, with stop-iteration exception raised
- iterable is an object that produces iterator from iter(obj)
- data = [1,2,3,4], data is not an iterator because can't call next(data), but data is iterable because we can do i = iter(data) then we can call next(i)

- eager vs lazy with generator
```
def factors(n):
    ret = []
    for i in range(1,n+1):
        if n % i == 0
            ret.append(i)
    return n
```
```
def factors(n):
    for i in range(1, n+1):
        if n % i == 0
            yield i
```

- multiple returns packs into a tuple
- a,b,c,d = range(0,4) unpacking
- algorithm Design Patterns:
recursion
amortization
divide and conquer
prune and search
brute force
dynamic programming
greety method
- software engineering Design Patterns
iterator
adapter
position
composition
template    
locator
factory
- Design
phase 1:
responsibilities: actors
independence: define work fo each class
behaviors: will become methods
CRC cards

LEFT | CENTER | RIGHT
responsibility | name | collaborators

- Fib
0, 1, 1, 2, 3, 5, 8, 13
can be generated from 2 values, 4, 6, 10, 16
