def fun(n):
    stack = []
    res = []
    
    def backtrack(o,c):
        if o == c == n:
            res.append("".join(stack))
            return
        if o < n:
            stack.append("(")
            backtrack(o+1,c)
            stack.pop()
        if c < o:
            stack.append(")")
            backtrack(o,c+1)
            stack.pop()
    backtrack(0,0)
    return res
n = int(input())
print(fun(n))
            