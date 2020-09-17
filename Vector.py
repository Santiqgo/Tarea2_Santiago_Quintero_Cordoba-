#!/usr/bin/env python
# coding: utf-8

#Se va a usar el símbolo de numero para comentar en lugar de las tres comillas porque la anterior causo problemas en la ejecución en varios momentos

#en el archivo se hacen las clases que deberán emplearse en la tarea

#Iniciamos con nuestra clase principal la cual se encarga de crear un vector con componentes cartesianas (x,y,z) y con los atributos x,y,z, y la magnitud de dicho vector

class VectorCartesiano:
    
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z
        self.cartesiano = [self.x,self.y,self.z]
        self.magnitud = (x**2 + y**2 + z**2)**0.5

########################################################################################################################

#Se crea un método llamado cruz el cual dado dos vectores pertenecientes a la case VertorCartesiano entrega otro vector perteneciente a la clase y sus componentes se dan por el producto cruz, por otro lado se sobrecargan métodos conocidos como suma, resta, igualdad, [], multiplicación por sus receptivos métodos vectoriales
    def __mul__(self, other):
         return VectorCartesiano(self.x * other.x,self.y * other.y,self.z * other.z)
    
    def Cruz(self, other):
        return VectorCartesiano(self.y * other.z - self.z * other.y ,
                                self.z * other.x - self.x * other.z,
                                self.x * other.y - self.y * other.x)
    
    def __add__(self,other):
        return VectorCartesiano(self.x + other.x, self.y + other.y, self.z + other.z)
    
    def __sub__(self,other): 
        return VectorCartesiano(self.x - other.x, self.y - other.y, self.z - other.z)
    
    def __getitem__(self,index):
        self.cartesiano[index]
    
    def __eq__(self, other):
        if self.cartesiano[0] == other.cartesiano[0] and self.cartesiano[1] == other.cartesiano[1] and self.cartesiano[2] == other.cartesiano[2]:
            return True
        else:
            return False
        
########################################################################################################################

#Para un caso externo fue de mayor comodidad hallar las componentes esféricas de vectores, osea que dado un vector (x,y,z) en la base cartesiana se hallaría otro vector en la misma base con componente (r,theta,phi), se tomaron los casos posibles, pueden existir más pero no todos pasaron por mi mente
    def cartesianoapolar(self):
        from math import acos,atan,pi,copysign
        
        if  self.x == 0:#en el caso que x=0 se usa un valor ya conocido thetha

            return VectorCartesiano(self.magnitud,acos(self.z/self.magnitud),copysign(pi*0.5,self.y))
        
        elif self.x > 0 and self.y > 0 :

            return VectorCartesiano(self.magnitud,acos(self.z/self.magnitud),atan(self.y/self.x))

        elif self.x > 0 and self.y < 0 :

            return VectorCartesiano(self.magnitud,acos(self.z/self.magnitud),atan(self.y/self.x) + 2*pi)

        elif self.x == 0 and self.y == 0 and self.z == 0:#dado el vector nulo se envia al vector nulo

            return VectorCartesiano(0,0,0)
        
        elif self.x != 0 and self.y == 0:
           
            return VectorCartesiano(self.magnitud,acos(self.z/self.magnitud),0)
        
        else:
            
            return VectorCartesiano(self.magnitud,acos(self.z/self.magnitud),atan(self.y/self.x) + pi)
########################################################################################################################        

#Por ultimo se crea un método que permite calcular el angulo entre dos vectores cartesianos
    def angulo(self,other):
        
        from math import acos
        return acos((self*other).magnitud/(self.magnitud * other.magnitud))
    
########################################################################################################################        

#Se crea una clase que herede los atributos de VectorCartesiano, se emplean formulas conocidas para hallar los valores theta y phi y los valores n,m se pueden ver las veces que se le dan vueltas a media circunferencia y una circunferencia respectivamente

class VectorPolar(VectorCartesiano):

    def __init__(self,r,theta,phi):
        
        from math import cos,sin,pi
        
        self.r=abs(r)
        
        n = int(theta/pi)
        m = int(phi/(2*pi))

        if theta > pi:

            if theta%pi == 0:
                
                self.theta = pi
            else:
                
                self.theta = theta - n*pi
                
        elif theta < 0:
            
            if theta%pi == 0:
                
                self.theta = pi
            else:
                
                self.theta = theta + n*pi

        
        else:
            self.theta = theta

        if phi > 2*pi:
            
            if phi%(2*pi) == 0:
                
                self.phi = 2*pi
            else:
                
                self.phi = phi - m*2*pi
                
        elif phi < 0:

            if phi%(2*pi) == 0:
                
                self.phi = 2*pi
            else:
                
                self.phi = self.phi = phi + m*2*pi
        
        else:
            self.phi = phi
                
        self.esferico = [self.r,self.theta,self.phi]
########################################################################################################################

#Se llama el constructor de VectorCartesiano para poder inicializar los atributos de VectorCartesiano
        VectorCartesiano.__init__(self,self.r*sin(self.theta)*cos(self.phi),
                                  self.r*sin(self.theta)*sin(self.phi),
                                  self.r*cos(self.theta)) # Transformación de las componentes en cartesianas
########################################################################################################################

#Con la inicializacion pasada se logra obtener la magnitud de forma correcta, el metodo creado a continuación hace lo mismo que la inicializacion pero se hace porque la tarea pide de ello

    def polaracartesiano(self):
        from math import cos,sin,pi
        return VectorCartesiano(self.r*sin(self.theta)*cos(self.phi),
                                self.r*sin(self.theta)*sin(self.phi),
                                self.r*cos(self.theta))
########################################################################################################################

#Transformación de los elementos de la base, con esta transformación ya hemos reparado todos los problemas ya que heredamos de las clases pero nuestras variables son diferentes
    def vecpolaraveccartesiano(self):
        from math import cos,sin,pi
        return VectorCartesiano(self.r*sin(self.theta)*cos(self.phi)*sin(self.theta)*cos(self.phi) +self.r*sin(self.theta)*
                sin(self.phi)*sin(self.theta)*sin(self.phi) + self.r*cos(self.theta)*cos(self.theta),
                self.r*sin(self.theta)*cos(self.phi)*cos(self.theta)*cos(self.phi) + self.r*sin(self.theta)*sin(self.phi)*
                cos(self.theta)*sin(self.phi) - self.r*cos(self.theta)*sin(self.theta),
                -self.r*sin(self.theta)*cos(self.phi)*sin(self.phi) +  self.r*sin(self.theta)*sin(self.phi)*cos(self.phi)) 
