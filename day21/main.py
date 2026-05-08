# khai bao 1 đổi tượng trong python 

class Person:
    def __init__(self, name = "kaka", ho= "koko"):
        self.name = name
        self.ho = ho
        self.tuoi = 0

    # method: phuong thu 
    def fullname(self):
        print(self.ho +' '+ self.name + " " + str(self.tuoi) )
    
    # get set
    def getName(self):
        return self.name
    
    def setName(self, name):
        self.name = name

# kế thừa trong class 

class SinhVien(Person): 
    def __init__(self):
        super().__init__()
        self.masv = ""
  

sv1 = SinhVien()

sv1.masv = "2231"
sv1.ho = "huynh"
sv1.name = "thai"
print(sv1.masv)
print(sv1.name)
print(sv1.ho)
sv1.fullname()


