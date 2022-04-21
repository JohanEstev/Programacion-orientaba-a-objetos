class Figuras():
    
    def __init__(self):
        
     

       
        print("-"*30)
        print("Figuras Geometricas")
        print ("-"*30)

    def Ingreso (self): 
        
            self.figura=input("Ingrese el nombre de la figura: ")
        
        
class Cuadrado(Figuras):
    
    pass   
        
    def areacuadrado(self):
        
        lado=print(int(input("Ingrese el valor del lado: ")))
                   
        return self.lado*2
        self.lado=lado
            
    #def perimetro(self):
           # perimetro=self.lado*4
  
    
#class Rectangulo (Figuras):
    
    #def __init__(self,altura,base):
       # self.altura=altura
        #self.base=base
        
    #def arearectangulo(self):
       # return self.altura*self.base
    
   # def perimetro(self):
        #return 2*(self.altura)+(self.base)
        

Resultado=Figuras()
Resultado.Ingreso()
a=Cuadrado()
a.areacuadrado()
