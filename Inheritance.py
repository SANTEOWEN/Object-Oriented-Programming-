#Parent Class
class person:
    def __init__(self,Fname,Lname):
        self.first = Fname
        self.last = Lname
    
    def introduce(self):
        print("Hi Im " + self.first + " " + self.last)

#Child Class
class student(person):
    def __init__(self, Fname, Lname,Section):
        #Super function is used to give access to methods and properties of a parent or sibling class.
        super().__init__(Fname, Lname)
        self.section = Section
    
        #You can override a function from a parent class 
    #def introduce(self):
        #print("Hi Im " + self.first + " " + self.last + "From " + self.section)#

        #You Can also use customize overrode function by using the super() function
    def introduce(self):
        super().introduce()
        print("From" +  self.section)


#Child Class
class worker(person):
    def __init__(self, Fname, Lname, IDnum, Position, work):
        super().__init__(Fname, Lname)
        self.id = IDnum
        self.pos = Position
        self.wrk = work

    def introduce(self):
        super().introduce()
        print("With an ID# of " + self.id+ " and my position is a " + self.pos)

    #we can also add a new function for this class just rename the function so it doesnt override other functions
    def workspace(self):
        print("My worksite is on " + self.wrk)

#You can use all of the functions from the parents class because of the inheritance
pOne = person("Owen", "Sante")
pOne.introduce()

#This is the example of the overide version of the function from the parent
sTwo = student("Sante", "Owen", "1-E")
sTwo.introduce()

#This is the example of the individual function of the worker class
wTwo = worker("Owen", "Sante", "1212412", "Mechanic", "Engine Room")
wTwo.introduce()
wTwo.workspace()
