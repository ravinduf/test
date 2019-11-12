class student:
    #instance attributes
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def printname(self):
        print("{} is {} old".format(self.name,self.age))
        
class path(student):

    def printpath(self):
        print("Hello")

r=path('ravindu',15)
r.printname()
r.printpath()