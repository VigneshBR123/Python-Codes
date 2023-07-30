class Human:
    def __init__(self, name, age, hobby):
        self.name = name
        self.age = age
        self.hobby = hobby
    def greet(self):
        print(f"My name is {self.name}.And my age is {self.age},My hobby is {self.hobby}.")
br = Human("Vignesh",22,"Progamming")
andin=Human("Abina",19,"Sleeping")
br.greet()