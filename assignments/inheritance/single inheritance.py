class Test():
    def accept(self,x,y,z):
        self.a=x
        self.b=y
        self.c=z
    def calc(self):
        self.sum=self.a+self.b+self.c
        self.mul=self.a+self.b+self.c
class demo(Test):
    def display(self):
        print("sum=",self.sum,"mul=",self.mul)
d=demo()
d.accept(20,30,40)
d.calc()
d.display()


