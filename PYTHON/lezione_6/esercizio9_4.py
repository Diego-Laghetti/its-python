#esercizio9_4
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type, numserv = 0) -> None:
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.numserv = numserv
    
    def describe_restaurant(self):
        print(f"The name is: {self.restaurant_name}")
        print(f"The cuisine is: {self.cuisine_type}")
        print(f"The resaturant has served: {self.numserv}")

    def open_restaurant(self):
        print("The restaurant is open")

    def get_numserv(self):
        return f'{self.numserv}'
    
    def set_numserv(self, numserv):
        self.numserv = numserv

    def incrnumserv(self, n: int) -> int:
        self.numserv += n
        return self.numserv        

if __name__ == "__main__":
    r1 = Restaurant("Restaurant from your class", "Indian")
    r1.describe_restaurant()
    r1.open_restaurant()
    r1.incrnumserv(3)
    r1.describe_restaurant()
    r1.set_numserv(0)
    r1.describe_restaurant()

