

#recursion:a function calls itself repletly

def sum (n):
    if n==0: #base condition
        return 0
    return n+sum(n-1)
print(sum(10))

#factorial

def fact(n):
    if n==1:
        return 1
    return n* fact(n-1)
print(fact(5))