def digsum(n):
    
    if n%10 == n:
        return n
    return (n%10) + digsum(n//10)
n = int(input())
print(digsum(n))


