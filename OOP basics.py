class item:
    def __init__(self,Name,Cost,Quantity=0):
        #validation to the received arguments
        assert Cost>=0, (f"The value of Cost '{Cost}' cannot be less than or equal to zero")
        assert Quantity>=0, (f"The value of Quantity '{Quantity}' cannot be less than or equal to zero")
        
        self.name=Name
        self.cost=Cost
        self.quantity=Quantity
        #print("constructor ran")
    def total_cost (self):
        return self.cost*self.quantity
    pay_rate=0.8
    def apply_discount(self):
        self.cost = (self.pay_rate*self.cost)
   
    
item1=item('mobile',100,3)
item2=item('laptop',1000,4)
item1.boss='nimesh'
item1.pay_rate=0.7

#print(item1.boss)
#print(item1.total_cost())
#print(item2.total_cost())
#print(item1.pay_rate)

#print(item1.__dict__)
item1.apply_discount()
print(item1.cost)
item2.apply_discount()
print(item2.cost)

