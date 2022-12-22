# Hierarchical

class A:
    def Ainfo(self):
        print("A")
    def About(self):
        print("A class")        

class B(A):
    def Binfo(self):
        print("B")
        A().Ainfo()

class C(B):
    def Cinfo(self):
        print("C")
        B().Binfo()
        
class E:
    def Einfo(self):
        print("E")
        
class D(E,C):
    def Dinfo(self):
        print("D")
        C().Cinfo()
        E().Einfo()
    
Dobj=D()
Dobj.Dinfo()
