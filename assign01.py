class functions():
    def __init__(self):
        self.books = []

    def addbook(self, book):
        self.books.append(book)
        print("Book added successfully!")

    def borrowbook(self, title):
        if title in self.books:
            self.books.remove(title)
            print("Book borrowed successfully!")
        else:
            print("Book not found!")

    def returnbook(self, book):
        self.books.append(book)
        print("Book returned successfully!")

    def display(self):
        print("Available books:", self.books)


class users():
    def __init__(self):
        self.users = []

    def adduser(self, user):
        self.users.append(user)
        print("User added successfully!")

    def removeuser(self, user):
        if user in self.users:
            self.users.remove(user)
            print("User removed successfully!")
        else:
            print("User not found!")

    def display(self):
        print("Available users:", self.users)

library = functions()
member = users()

library.addbook("Python")
library.addbook("Maths")
library.addbook("SE")

library.display()

library.borrowbook("Python")
library.display()

library.returnbook("Python")
library.display()

member.adduser("Sahil")
member.adduser("Sarthak")

member.display()

member.removeuser("Sahil")
member.display()