class Datos:

    def __init__(self, numero, imagen, efecto, tiempo):
        self.numero = numero
        self.imagen = imagen
        self.efecto = efecto
        self.tiempo = tiempo
        
    def set_numero(self, numero):
        self.numero = numero    

    def get_numero(self):
        return self.numero
    
    def set_imegen(self, imagen):
        self.imagen = imagen
    
    def get_imagen(self):
        return self.imagen
    
    def set_efecto(self, efecto):
        self.efecto = efecto
    
    def get_efecto(self):
        return self.efecto
    
    def set_tiempo(self, tiempo):
        self.tiempo = tiempo 

    def get_tiempo(self):
        return self.tiempo
    
    def __repr__(self):
        return str(self.__dict__)

