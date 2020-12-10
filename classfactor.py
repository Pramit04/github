class Test:
    def factorial(self,x):
        if x==1:
            return 1
        else:
            return (x*self.factorial(x-1))
num=int(input("Enter any number:"))
obj=Test()
s=obj.factorial(num)
print(s)