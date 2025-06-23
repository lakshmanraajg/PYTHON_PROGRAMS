a = {
    "name" : "laksh",
    "age" : "20"
    }
print(a.keys())
print(a.values())
print(a.items())
print(a.get("name"))
b = a.copy()
print(b)

for keys,value in a.items():
    print(keys + " : " + value)
for key in a:
    print(key, a[key])