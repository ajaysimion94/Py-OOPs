class Student:
    mark1,mark2,mark3=90,80,99
    def process(self):
        sum=Student.mark1+Student.mark2+Student.mark3
        avg=sum/3
        print("The total mark is : ",sum)
        print("The Average mark is : ",avg)
        return
S=Student()
S.process()