response = input("What is the answer to the Great Question of Life, the Universe and Everything? ").strip().lower()

if response == "42" or response == "forty-two" or response == "forty two":
    print("Yes")
else:
    print("No")
