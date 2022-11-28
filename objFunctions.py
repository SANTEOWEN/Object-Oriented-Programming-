#object with constructors
class animals:
    def __init__(self, animal, voice):
        self.animal = animal
        self.voice = voice
#object functions
    def speak(self):
        print(self.voice)
    
    def Introduceself(self):
        print ("Iam a " + self.animal)

#attributes of the object
Aone = animals("Dog", "Arf")
Aone.Introduceself()
Atwo = animals("Cat", "Meow")
Atwo.Introduceself()


