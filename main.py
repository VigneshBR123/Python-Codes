class Human:
    def __init__(self, name, age, hobby):
        self.name = name
        self.age = age
        self.hobby = hobby
br = Human("Vignesh",22,"Progamming")
andin=Human("Abina",19,"Sleeping")
class Student(Human):
    def __init__(self,name,age,hobby,company,post):
        super().__init__(name,age,hobby)
        self.company=company
        self.post=post
abin = Student("Abin",15,"playing","skv","tl")
a=abin. post
print(a)