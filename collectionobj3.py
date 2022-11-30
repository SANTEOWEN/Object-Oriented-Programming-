#we can also use a loop to write in collection of objects
class Person_one:
    def __init__(self, names):
        self.names = names 

    def introduce_one(self):
        print("I am " + self.names)

listof_peps = []

#here we use a loop to write or input a collection of objects for our list
for i in range(5):
    name = input("Enter a name for the list: ")
    persona = Person_one(name)
    listof_peps.append(persona)

# and here we use a loop to read all of those inputs coming from the first loops that have been inputed on the list
for person_one in listof_peps:
    person_one.introduce_one()