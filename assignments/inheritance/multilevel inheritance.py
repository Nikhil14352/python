class grandfather():
    def property(self):
        print("I have 25 store duplex buliding")
class father(grandfather):
    def vehicle(self):
        print("i have two roll royce cars")
class son(father):
    def inherit(self):
        print("i have two rollroyce and 25 store duplex building")
S=son()
S.property()
S.vehicle()
S.inherit()

mylist=['python','hub']
for i in mylist:
    mylist.append(i.upper())
    print(mylist)

