#i = 0
#while i < 3:
#    print("meow1")
#    i += 1

#for i in [0, 1, 2]:
#    print("meow")

#for i in range(3):    #range is a list
#    print("meow2")

#for _ in range(3):    #use _ since we never use the variable again.. it's just a signal to others.. more pythonic
#    print("meow3")

#print("meow4\n" * 3, end="")   this is a cool one line way to do it

#while True:
#    n = int(input("What's n? "))
#    if n < 0:
#        continue
#    else:
#        break

#while True:
#    n = int(input("What's n? "))
#    if n > 0:
#        break

#for _ in range(n):
#    print("meow")


def main ():
        number = get_number()
        meow(number)


def get_number():
    while True:
            n = int(input("What's n? "))
            if n > 0:
                   return n
            

def meow(n):
       for _ in range(n):
              print("meow")


main ()