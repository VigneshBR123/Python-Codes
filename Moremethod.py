class Human:
    total=0
    data=[]
    def __init__(self,name,age,alive=True):
        self.name=name
        self.age=age
        self.alive=alive
        Human.total+=1
        Human.data.append(self.name)
br=Human("Vignesh",21)
abi=Human("Abina",19)
def dead(self):
    if self.alive:
        print(self.name,"is no more row")
        Human.total-=1
        self.alive=False
    else:
        print("The person is already dead")
d=Human.data
print(d)
a=Human.total
print(a)
dead(br)
dead(br)
b=Human.total
print(b)
print("Methods in Python")