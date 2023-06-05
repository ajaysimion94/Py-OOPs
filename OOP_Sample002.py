class Odd_Even:
    def check(self,num):
        if num%2==0:
            print("It is a Even Number")
        else:
            print("It is a Odd Number")
n=Odd_Even()
x=int(input("Enter a number : "))
n.check(x)