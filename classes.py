class Myclass:
    var="test"
    def funcao (self):
        print("This is the message inside my class")
myobject=Myclass()
print(myobject.var)
myobject.funcao()

myobject2=Myclass()
myobject2.var="Hello World"

print(myobject.var)
print (myobject2.var)