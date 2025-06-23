def fun(a):
    hashset = set()
    for n in a:
        if n in hashset:
            return True
        hashset.add(n)
    return False

a = [1,2,3,4,2,3,4]
print(fun(a))