#Ask user for their name
#name = input("What's your name? ")
#Remove whitespace from str
#name = name.strip()
#Capitalize user's name
#name = name.capitalize()
#Capitalize all words.. aka Title Case the string
#name = name.title()
#name = name.strip().title()     .strip() and .title() are methods... functions that are built into the string class.. input makes the input string class

#name = input("What's your name? ").strip().title()

#Split user's name into first name and last name
#first, last = name.split(" ")

#Say hello to user
#print("Hello, " + name + "!")

#print("Hello, ", end="")
#print(name, end="")
#print("!")

#print("Hello,", name)

#print("Hello, ", name, sep="")

#print(f"Hello, {name}!")

#print(f"Hello, {first}")



##### defining our own functions with def#####
#def hello():
    #print("Hello")

#name = input("What's your name? ")
#hello()
#print(name)


#def hello(to="world"):
    #print(f"Hello, {to}!")

#hello()
#name = input("What's your name? ")
#hello(name)

def main():
    name = input("What's your name? ")
    hello(name)

def hello(to="world"):
    print(f"Hello, {to}!")

main()