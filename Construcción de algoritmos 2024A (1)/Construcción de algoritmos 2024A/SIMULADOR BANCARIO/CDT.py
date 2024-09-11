__autor__ = "Gabriel Esteban Paz Guerrero"
__license__ = "GPL"
__version__ = "1.0.0"
__email__ = "gabriel.pazg@campusucc.edu.com"


class CDT: 
    # Aquí inicia mi clase

    """#--------------------------------------------------------------------------------------
    # Atributos
    --------------------------------------------------------------------------------------#"""

    Inversion = 0
    Interes = "%"

    """#--------------------------------------------------------------------------------------
    # Fecha específica
    --------------------------------------------------------------------------------------#"""
    
    Fecha_apertura = ()

    """#-------------------------------------------------------------------------------------------------
    # Métodos
    -------------------------------------------------------------------------------------------------#"""
    
    __method__="AñadirInversion"
    __params__="Ninguno"
    __returns__="Inversion"
    __descriptions__="Este metodo permite añadir una inversion"
    
    def AñadirInversion (self):
        # Aquí inicia mi metodo
        return self.Inversion 

    __method__="InteresInversion"
    __params__="Interes"
    __returns__="Ninguno"
    __descriptions__="Permite sumar el interes a la inversion"
    
    def InteresInversion (Self,Interes):
        #Aqui inicia el metodo
        Self.Inversion = Self.Inversion + Interes
