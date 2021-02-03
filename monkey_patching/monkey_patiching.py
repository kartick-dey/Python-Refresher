class MonkeyPatching:
    def __init__(self, x):
        self.x = x

    def get_data(self):
        print("Get Data from DB")

    def fun1(self):
        self.get_data()

    def fun2(self):
        self.get_data()

obj = MonkeyPatching(5)
obj.fun1()
obj.fun2()

def new_get_data(self):
    print("Get data from Monkey Patching")

print("After Monkey Pathcing......")
MonkeyPatching.get_data = new_get_data
obj.fun1()
obj.fun2()