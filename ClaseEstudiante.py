class estudiante():
    def __init__(self,nombre,apellido,correo,cedula,telefono):  
        self.nombre = nombre
        self.apellido = apellido
        self.correo = correo
        self.cedula = cedula
        self.telefono = telefono    
        
    def Obtener_Informacion(self):
        print ("\nMi nombre es:" ,self.nombre, "\nmi apellido es:", self.apellido,"\nmi correo es: ", self.correo,"\nmi cedula es:", self.cedula, "\nmi telefono es",self.telefono)
        
e = estudiante("Jose" , "cabrales", "jcabrales881@gmail.com","1043296835", "3058228496")

e.Obtener_Informacion()
        

        