class Parent():
    def first (self):
        print ("This is first function")
class Child (Parent):
    def second (self):
        print("This is second function")
ob=Child()
ob.first()
ob.second()