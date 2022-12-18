# singel

class A:
    def Ainfo(self):
        print ("A")
class B(A):
    def Binfo(self):
        print("B")
        A().Ainfo()
Bobj=B()
Bobj.Binfo()
