class character:
    def __init__(self, Name, Hp, Attack, Level, Race): 
        self.name = Name
        self.Hp = Hp
        self.Attack = Attack
        self.Level = Level
        self.race = Race
        print("Created " + self.name)

CharOne = character("Ursa", 275, 66, 1, "Monster" )
CharTwo = character("Invoker", 560, 35, 1, "Elf" )
