class Sample:
    def __init__(self,n1,n2):
        self.n1=n1
        self.n2=n2
    def Display(self):
        print("Class Variable 1 : ",self.n1)
        print("Class Variable 2 : ",self.n2)
S=Sample(15,25)
S.Display()
print("External Call : ",S.n1)
print("External Call :",S.n2)