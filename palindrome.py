def palin(newstr):
    if newstr == newstr[::-1]:
        return True
    return False
    
    
run = True
while(run):
    teststr = input("Enter a string: ")
    
    if teststr == "exit":
        run = False
        break
    
    teststr = teststr.lower()
    
    #striping all the unwanted spaces and special characters from the string

    newstr = ""
    for x in teststr:
        if x.isalnum():
            newstr = newstr + x
    print(palin(newstr))