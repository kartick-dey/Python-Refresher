class ClassMethods:
    TYPES = ('hardcover', 'paperback')

    def __init__(self, name, book_type, weight):
        self.name = name
        self.book_type = book_type
        self.weight = weight

    def __repr__(self):
        return f"<Book {self.name}, {self.book_type}, weight {self.weight}g>"

    def instance_method(self):
        print(f"Called instance method of {self}")

    @classmethod
    def class_method(cls):
        print(f"Called from class method of class {self}")

    @classmethod
    def hardcober(cls, name, page_weght):
        return ClassMethods(name, ClassMethods.TYPES[0], page_weght + 100) # instead of ClassMethods we can use cls as well

    @classmethod
    def paperback(cls, name, page_weght):
        return ClassMethods(name, ClassMethods.TYPES[1], page_weght)

    @staticmethod
    def static_method():
        print("Called from static method.")

    
classObj = ClassMethods()

# both are same

classObj.instance_method()
ClassMethods.instance_method(classObj)

# To call a class method we no need to create an instance

ClassMethods.class_method() # no need to pass instance bcz it automatically take class as an input parameter.

hard = ClassMethods.hardcober("Python", 2400)
light = ClassMethods.paperback("SQL", 1200)

print('Hard: ', hard)
print("Light: ", light)