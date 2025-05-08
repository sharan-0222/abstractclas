class bmw :
    def fuel(self):
        print("petrol")

    def top_speed(self):
        print("200kmph")

class ferrari :
    def fuel(self):
        print("diesel")

    def top_speed(self):
        print("300kmph") 

ferrari=ferrari()
bmw=bmw()

for car in (ferrari,bmw):
    car.fuel()
    car.top_speed()