camel_case = input("camelCase: ")

for c in camel_case:
    if c.isupper():
        c = "_" + c.lower()
    print(c, end="")

    