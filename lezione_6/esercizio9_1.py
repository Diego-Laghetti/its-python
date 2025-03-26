#esercizio9_1
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    
    def describe_restaurant(self):
        print(f"The name is: {self.restaurant_name}")
        print(f"The cuisine is: {self.cuisine_type}")

    def open_restaurant(self):
        print("The restaurant is open")

r1 = Restaurant("Restaurant from your class", "Indian")
r1.describe_restaurant()
r1.open_restaurant()