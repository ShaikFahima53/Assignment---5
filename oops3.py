class Student:
    __name = None
    __rollNumber = None

    def setName(self, name):
        self.__name = name
        
    def getName(self):
        return  self.__name

    def setRollNumber(self, rollNumber):
        self.__rollNumber = rollNumber

    def getRollNumber(self):
        return self.__rollNumber


demo1 = Student()
demo1.setName("Fahima")
print("Name:",demo1.getName())
demo1.setRollNumber(12006853)
print("Roll Number:", demo1.getRollNumber())
