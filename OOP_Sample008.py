class MyStore:
    __prod_code=[]
    __prod_name=[]
    __cost_price=[]
    __prod_quant=[]
    def getdata(self):
        self.p=int(input("Enter the number of product you need to store: "))
        for x in range(self.p):
            self.__prod_code.append(int(input("Enter the product code: ")))
            self.__prod_name.append(str(input("Enter the name of the product: ")))
            self.__cost_price.append(int(input("Enter the cost of the product: ")))
    def display(self):
        print("Stock in Stores")
        print("-------------------------------------------------------------------------------")
        print("Product Code \t Product Name \t Cost")
        print("-------------------------------------------------------------------------------")
        for x in range(self.p):
            print(self.__prod_code[x],"\t\t",self.__prod_name[x],"\t\t", self.__cost_price[x])
        print("-------------------------------------------------------------------------------")
    def print_bill(self):
        total_price=0
        for x in range(self.p):
            q=int(input("Enter the quantity for the product code %d:"%self.__prod_code[x]))
            self.__prod_quant.append(q)
            total_price=total_price+self.__cost_price[x]*self.__prod_quant[x]
        print("\t\t\t\t Invoice Receipt")
        print("-------------------------------------------------------------------------------")
        print("Product Code\tProduct Name\tCost Price\tQuantity \t Total Amount")
        print("-------------------------------------------------------------------------------")
        for x in range(self.p):
            print(self.__prod_code[x],"\t\t",self.__prod_name[x],"\t\t",self.__cost_price[x],"\t\t",self.__prod_quant[x],"\t\t",self.__cost_price[x]*self.__prod_quant[x])
        print("-------------------------------------------------------------------------------")
        print("\t\t\t\t\t\t\tTotal Amount: ",total_price)
S=MyStore()
S.getdata()
S.display()
S.print_bill()