people = [
    {"name": "harry", "house":"griddindor"},
    {"name": "cho", "house":"ravenclaw"},
    {"name": "draco", "house":"slytherin"}
]

# def f(person):
#     return person["house"]

# people.sort(key=f)

# the above using lamdas

people.sort(key=lambda person: person["name"])

# takes in person and returns person[name]

print(people)