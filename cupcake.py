from abc import ABC, abstractmethod
import csv
from pprint import pprint

def read_csv(file):
    with open(file) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            pprint(row)

def write_new_csv(file, cupcakes):
    with open(file, "w", newline="\n") as csvfile:
        fieldnames = ["size","name", "price","flavor", "color", "frosting", "sprinkles", "filling"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()

        for cupcake in cupcakes:
            if hasattr(cupcakes, "filling"):
                writer.writerow({"size": cupcake.size, "name": cupcake.name,"price": cupcake.price, "color": cupcake.color, "frosting": cupcake.frosting, "filling": cupcake.filling, "sprinkles": cupcake.sprinkles })
            else:
                writer.writerow({"size": cupcake.size, "name": cupcake.name,"price": cupcake.price, "color": cupcake.color, "frosting": cupcake.frosting, "sprinkles": cupcake.sprinkles })

def add_cupcake(file, cupcake):
    with open(file, "a", newline="\n") as csvfile:
        fieldnames = ["size","name", "price","flavor", "color", "frosting", "sprinkles", "filling"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        if hasattr(cupcake, "filling"):
            writer.writerow({"size": cupcake.size, "name": cupcake.name,"price": cupcake.price, "color": cupcake.color, "frosting": cupcake.frosting, "filling": cupcake.filling, "sprinkles": cupcake.sprinkles })
        else:
            writer.writerow({"size": cupcake.size, "name": cupcake.name,"price": cupcake.price, "color": cupcake.color, "frosting": cupcake.frosting, "sprinkles": cupcake.sprinkles })

def get_cupcakes(file):
    with open(file) as csvfile:
        reader = csv.DictReader(csvfile)
        reader = list(reader)
        return reader

def find_cupcake(file, name):
    for cupcake in get_cupcakes(file):
        if cupcake["name"] == name:
            return cupcake
        else:
            return None

def add_cupcake_dictionary(file,cupcake):
    with open(file, "a", newline="\n") as csvfile:
        fieldnames = ["size","name", "price","flavor", "color", "frosting", "sprinkles", "filling"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writerow(cupcake)

class Cupcake(ABC):
    size = "regular"
    def __init__(self, name, price, color, frosting):
        self.name = name 
        self.price = price 
        self.color = color
        self.frosting = frosting
        self.sprinkles = []
    
    def add_sprinkles(self, *args):
        for sprinkle in args:
            self.sprinkles.append(sprinkle)

    @abstractmethod
    def calculate_price(self,quantity):
        pass

class Mini(Cupcake):
    size = "mini"
    def __init__(self, name, price, color, flavor, frosting):
        self.name = name
        self.price = price
        self.color = color
        self.flavor = flavor
        self.frosting = frosting
        self.sprinkles = []

    def calculate_price(self,quantity):
        pass

cupcake_1_mini= Mini("Chocolate", 2.50, "red", "Chocolate", "White")
cupcake_2_mini = Mini("regular","triple chocolate",2.99, "chocloate","chocolate")

# read_csv("sample.csv")

if __name__ == "__main__":
    pass