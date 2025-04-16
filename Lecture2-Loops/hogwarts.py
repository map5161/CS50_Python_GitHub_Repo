#students = ["Hermione", "Harry", "Ron"]

#for student in students:
#    print(student)

#for i in range(len(students)):
#    print(i + 1, students[i])


#dictionaries use curly braces
#students = {
#    "Hermione": "Gryffindor",
#    "Harry" : "Gryffindor",
#    "Ron" : "Gryffindor",
#    "Draco" : "Slytherin",
#}

#print(students["Hermione"])

#for s in students:
#    print(s, students[s], sep=",")

#a list of dictionaries
students = [
    {"name": "Hermione", "house": "Gryffindor", "patronus": "Otter"},
    {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
    {"name": "Ron", "house": "Gryffindor", "patronus": "Jack Russell terrier"},
    {"name": "Draco", "house": "Slytherin", "patronus": None},
]

for s in students:
    print(s["name"], s["house"], s["patronus"], sep=",")