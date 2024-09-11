__autor__ = "Gabriel Esteban Paz Guerrero"
__license__ = "GPL"
__version__ = "1.0.0"
__email__ = "gabriel.pazg@campusucc.edu.com"

class CuentaCorriente: 
    # Aquí inicia mi clase
    
    """#--------------------------------------------------------------------------------------
    # Atributos
    --------------------------------------------------------------------------------------#"""

    __Saldo = 0
    
    """#-------------------------------------------------------------------------------------------------
    # Métodos
    -------------------------------------------------------------------------------------------------#"""
    
    __method__="ConsignarValor"
    __params__= "monto"
    __returns__="nada"
    __descriptions__="Este metodo permite consignar un monto a la cuenta"
    def ConsignarValor(self, monto):
        self.__Saldo=self.__Saldo + monto
    
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
    
    __method__="VerSaldo"
    __params__= "nuevoSaldo"
    __returns__="nada"
    __descriptions__="Este metodo modificar el saldo por uno nuevo"

    def ModificarSaldo(self, nuevoSaldo):
        #Aqui inicia el metodo
        self.Saldo = nuevoSaldo