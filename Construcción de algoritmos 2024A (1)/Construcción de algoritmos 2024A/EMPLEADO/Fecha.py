__autor__ = "Gabriel Esteban Paz Guerrero"
__license__ = "GPL"
__version__ = "1.0.0"
__email__ = "gabriel.pazg@campusucc.edu.com"

class Fecha:
    # Aquí inicia mi clase
    """#---------------------------------------------------------------------------------------------------
    # Atributos
    ---------------------------------------------------------------------------------------------------#"""

    Dia = 0
    Mes = 0
    Anio = 0
    # Aquí inicia mi clase
    """#---------------------------------------------------------------------------------------------------
    # Métodos
    ---------------------------------------------------------------------------------------------------#"""
    
    __method__="Dar_Dia"
    __params__="Ninguno"
    __returns__="Dia de la clase"
    __descriptions__="Devuelve el dia de la clase"
    
    def Dar_Dia (self):
        # Aquí va mi algoritmo
        return self.Dia
        
    __method__="Dar_Mes"
    __params__="Ninguno"
    __returns__="Mes de la clase" 
    __descriptions__="Devuelve el mes de la clase"
    
    def Dar_Mes (self):
        # Aquí va mi algoritmo
        return self.Mes
        
    __method__="Dar_Anio"
    __params__="Ninguno"
    __returns__="Año de la clase"
    __descriptions__="Devuelve el año de la clase"
    
    def Dar_Anio(self):
        # Aquí va mi algoritmo
        return self.Anio
    
    __method__="Dar_Fecha"
    __params__="Ninguno"
    __returns__="Fecha de la clase"
    __descriptions__="Devuelve la fecha de la clase"
    
    def Dar_Fecha(self):
        # Aquí va mi algoritmo
        return self.dia+"/"+self.mes+"/"+self.anio
    
    
