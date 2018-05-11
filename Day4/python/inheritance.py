
class Parent:
    def __init__(self):
	print ("Inside Parent constructor")
	self.__privateData = 100
	self._protectedData = 200
	self.publicData = 300

    def setValues(self, val1, val2, val3):
	self.__privateData = val1
	self._protectedData = val2
	self.publicData = val3

    def printValues(self):
	print ("Value of private Data is " + str ( self.__privateData ) )
	print ("Value of protected Data is " + str ( self._protectedData ) )
	print ("Value of public Data is " + str ( self.publicData ) )

class Child(Parent):
    def __init__(self):
	Parent.__init__(self)
	self.data = 10000

    def printValues(self):
	Parent.printValues(self)
	print("Value of Child Data is " + str(self.data) + "\n")

def main():
    obj1 = Child()
    print("Values of member variables before calling setValues function")
    obj1.printValues()
    obj1.setValues(5000,6000,7000)
    print("Values of member variables after calling setValues function")
    obj1.printValues()

    print("Attempt to read public variables directly ", obj1.publicData)
    print("Attempt to read protected variables directly ", obj1._protectedData)
    print("Attempt to read Child's public variables directly ", obj1.data)
    #print("Attempt to read private variables directly ", obj1.__privateData)

main()
