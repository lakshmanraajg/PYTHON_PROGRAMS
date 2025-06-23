def fun(n,steps):
    if n==0:
        return steps
    
    if n%2 == 0:
        return fun(n//2,steps+1)
    return fun(n-1,steps+1)

print(fun(41,0))