mystr = "fu"
def fun():
    mystr = "fun"
    print(mystr)
fun()
print(mystr)

del mystr

fun()