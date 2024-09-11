__autor__ = "Gabriel Esteban Paz Guerrero"
__license__ = "GPL"
__version__ = "1.0.0"
__email__ = "gabriel.pazg@campusucc.edu.com"

class CuentaAhorros: 
    # Aquí inicia mi clase
    
    """#--------------------------------------------------------------------------------------
    # Atributos
    --------------------------------------------------------------------------------------#"""

    __Saldo = 10
    __Interes = "0.6%"

    
    """#-------------------------------------------------------------------------------------------------
    # Métodos
    -------------------------------------------------------------------------------------------------#"""
    
    __method__="DarSaldo"
    __params__= "Ninguno"
    __returns__="Saldo"
    __descriptions__="Este metodo retorna el saldo de la cuenta"
    def DarSaldo(self):
        #Aqui inicia el metodo
        return self.__Saldo
    
    __method__="RetirarValor"
    __params__= "monto"
    __returns__="nada"
    __descriptions__="Este metodo permite retirar un monto a la cuenta"
    def RetirarValor(self, monto):
        self.__Saldo=self.__Saldo - monto
    
    __method__="SumarInteres"
    __params__="Interes"
    __returns__="Ninguno"
    __descriptions__="Permite sumar el interes al saldo"
    
    def SumarInteres(Self,Interes):
        #Aqui inicia el metodo
        Self.__Saldo = Self.__Saldo + Interes

    __method__="VerSaldo"
    __params__= "nuevoSaldo"
    __returns__="nada"
    __descriptions__="Este metodo modificar el saldo por uno nuevo"

    def ModificarSaldo(self, nuevoSaldo):
        #Aqui inicia el metodo
        self.__Saldo = nuevoSaldo