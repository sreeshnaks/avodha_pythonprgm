class A:
    def __int__(self,name):
     self.name=name
    def getdata(self):
     self.name=input("enter the name")
class B(A):
     def __int__(self,hodname):
      self.hodname=hodname
     def putdata(self):
      self.hodname=input("enter the hod name")
     def display(self):
        print("student name is",self.name)
        print("hodname is",self.hodname)

class C(B):
     def fun(self):
        print("this is class c")

class D(C):
     def fun1(self):
        print("this is class d")

obj=D("","")
obj.getdata()
obj.putdata()
obj.display()
obj.fun()
obj.fun1()