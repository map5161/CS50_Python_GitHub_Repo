exp = input("Expression: ").strip().lower()

x, y, z = exp.split(" ")

x = int(x)
z = int(z)

def interpreter(x, y, z):
    if y == "+":
        return(x + z)
    elif y == "-":
        return(x - z)
    elif y == "*":
        return(x * z)
    else:
        return(x / z)

float_output = float(interpreter(x, y, z))

print(float_output)