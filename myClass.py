class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def getName(self):
        return self.name
    def getAge(self):
        return self.age
    
class Customer(Person):
    def __init__(self,nm,ag,ad,tl):
        super().__init__(nm,ag)
        self.address=ad
        self.tel=tl
    def getName(self):
        self.name="顧客："+self.name
        return self.name
    def getAdr(self):
        return self.address
    def getTel(self):
        return self.tel 
    
if __name__=="__main__":
    pr=Customer("佐藤",23,"sato@aaa.bbb.ccc","090-111-2222")
    print(pr.getName())