class Parent():
    def func1(self):
        print("This is parent")
class child(Parent):
    def func1(self):
        print("This is child")
obj=child()
obj.func1()