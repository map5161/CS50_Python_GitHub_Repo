omit_list = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]

input = input("Input: ")

for i in input:
    if i in omit_list:
        i = ""
    print(i, end="")