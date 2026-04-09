class Student:
    def setId(self, id):  # @Reserved
        self.id = id

    def getId(self):
        return self.id

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name


s = Student()
s.setId(1903)
s.setName("Vivek Singh")
print(s.getId())
print(s.getName())