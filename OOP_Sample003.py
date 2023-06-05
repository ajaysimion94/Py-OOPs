class Sample:
    num=0
    def __init__(self,var) -> None:
        Sample.num+=1
        self.var=var
        print("The object value is : ",var)
        print("The value of the class variable is : ",Sample.num)
    def __del__(self):
        Sample.num-=1
        print("Object with value %d is exit from the scope"%self.var)
S=Sample(15)
S=Sample(34)
S=Sample(67)