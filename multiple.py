class A:
    def fun1(self):
        print("am A class")


class B:
    def fun2(self):
        print("am B class")


class C(A,B):
    def put(self):
        print(" yes inheritance")


obj = C()
obj.fun1
obj.fun2
obj.put
