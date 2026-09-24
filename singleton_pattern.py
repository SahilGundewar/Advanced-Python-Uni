class Printer:
    obj = None

    def __new__(cls):
        if cls.obj is None:
            cls.obj = super().__new__(cls)
        return cls.obj

    def print_doc(self, name):
        print("Printing:", name)


p1 = Printer()
p2 = Printer()

p1.print_doc("File1")
p2.print_doc("File2")

print(p1 == p2)