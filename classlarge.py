class Test:
    def largest(self,a,b):
        if a>b:
            return(a)
        else:
            return (b)
a=int(input("Enter any number:"))
b=int(input("Enter another number:"))
obj=Test()
s=obj.largest(a,b)
print(s)



    