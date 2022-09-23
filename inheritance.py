class student:
    def __int__(self, name):
        self.name = name

    def getdata(self):
        self.name = input("enter the name")


class hod(student):
    def __int__(self, hodname):
        self.hodname = hodname

    def putdata(self):
        self.hodname = input("enter the hod name")

    def display(self):
        print("student name is", self.name)
        print("hodname is", self.hodname)


obj = hod()
obj.getdata()
obj.putdata()
obj.display()
