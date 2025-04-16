#def main():
#    print_column(3)


#def print_column(height):
#    for _ in range(height):
#        print("#")
#    print("#\n" * height, end="")


#main()



#def main():
#    print_row(4)

#def print_row(width):
#    print("?" * width)

#main()


#the outer loop is related to the rows, the inner loop is related to the columns
def main():
    print_square(3)

#def print_square(size):
#    for i in range(size):
#        for j in range(size):
#            print("#", end="")
#        print()

#def print_square(size):
#    for i in range(size):
#        print("#" * size)

def print_square(size):
    for i in range(size):
        print_row(size)    #abstraction

def print_row(width):
    print("#" * width)

main()

