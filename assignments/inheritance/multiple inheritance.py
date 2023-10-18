class six_wheeler:
    def bus(self):
        print('i have 25 seats i can carry 25 member in my bus')
class four_wheeler:
    def car(self):
        print('i have 5 seats i can carry 5 members ')
class passenger(six_wheeler,four_wheeler):
    def customer(self):
        print('i can go by bus or car')
a=passenger()
a.bus()
a.car()
a.customer()


    
