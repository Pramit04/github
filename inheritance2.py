class Parent():
    def first(self):
        print("This is first function")
class Parent2():
    def second(self):
        print("This is second function")
class child(Parent,Parent2):
    def third(self):
        print ("This is third function")
obj=child()
obj.first()
obj.second()
obj.third()