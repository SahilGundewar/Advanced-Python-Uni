class Apple:
    def show(self):
        print("Apple")


class Mango:
    def show(self):
        print("Mango")


class Orange:
    def show(self):
        print("Orange")


class FruitFactory:
    def getFruit(self, fruit):
        if fruit == "Apple":
            return Apple()
        elif fruit == "Mango":
            return Mango()
        elif fruit == "Orange":
            return Orange()


name = input("Enter Fruit: ")

factory = FruitFactory()
fruit = factory.getFruit(name)
fruit.show()