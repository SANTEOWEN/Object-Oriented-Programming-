class person:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        print("lamaw " + self.name)


#We use the input syntax to get attributes from the users
name = input("Enter a name: ")
pOne = person(name)
print(pOne)