class Human:
    data=[]
    total=0
    def __init__(self,name,age):
        self.name=name
        self.age=age
        Human.total+=1
        Human.data.append(self.name)
br=Human("Vignesh",21)
abi=Human("SAbina",19)
appa=Human("Babu",50)
amma=Human("Rajam",45)
a=Human.data
print(a)
for i in a:
    print(i)