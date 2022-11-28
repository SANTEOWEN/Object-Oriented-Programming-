class user:
    def __init__(self, Fname, Lname, LikesCount, Friendsname):
        self.fname = Fname
        self.lname = Lname
        self.likes = LikesCount
        self.friends = Friendsname
        print("User Created Name: " + self.fname)

    def introduce(self):
        print ("Hi Iam " + self.lname + " " + self.fname)
    
    def Profile(self):
        print ("Full Name: " + self.fname + " " + self.lname)
        print ("Likes: " + str(self.likes))
        print("Friends: ")
        for friends in self.friends:
            print("  - " + friends)

Uone = user("Owen", "Sante", 10, ["Eve", "Yoasobi"])
Uone.Profile()