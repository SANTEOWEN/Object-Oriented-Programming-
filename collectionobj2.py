class person:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        print("lamaw " + self.name)

#We can also use a loop to read a collection under the list
pOne = person("Owen")
pTwo = person("Dave")
pThree = person("Joshua")

listofpeps = [pOne, pTwo, pThree]

for person in listofpeps:
    print(person.name)
