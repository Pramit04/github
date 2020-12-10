class Parent():
    def first(self):
        print("This is first function")
class Parent2(Parent):
    def second(self):
        print("this is second function")
class child(Parent2):
    def second(self):
        print("this is third value")
obj=child()
obj.first()
obj.second()

