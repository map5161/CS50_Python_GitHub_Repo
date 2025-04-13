#x = int(input("What is x? "))
#y = int(input("What is y? "))

#x = float(input("What is x? "))
#y = float(input("What is y? "))

#z = round(x + y)

#print(z)

#print(f"{z:,}") #formatting to 1,000 with the comma
#print(f"{z:.2f}") formatting to round to 2 decimal places

#z = round(x / y, 2)

#print(z)


####defining a function and return value###
def main():
    x = int(input("What is x? "))
    print("x squared is", square(x))

def square(n):
    #return n * n
    return n ** 2

main()