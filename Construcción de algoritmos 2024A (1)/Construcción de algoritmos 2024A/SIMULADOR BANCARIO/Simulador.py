__autor__ = "Gabriel Esteban Paz Guerrero"
__license__ = "GPL"
__version__ = "1.0.0"
__email__ = "gabriel.pazg@campusucc.edu.com"

'''----------------------------------------------------------------
#Importaciones
----------------------------------------------------------------'''
from Ahorros import CuentaAhorros
from CDT import CDT
from Corriente import CuentaCorriente

class Simulador: 
    # Aquí inicia mi clase
    """#--------------------------------------------------------------------------------------
    # Atributos
    --------------------------------------------------------------------------------------#"""
    __Nombre = ""
    __Cedula = ""

    """#--------------------------------------------------------------------------------------
    # Dias, meses y años
    --------------------------------------------------------------------------------------#"""

    __mesActual = 0

    """#--------------------------------------------------------------------------------------
    # Asociaciones (cuentas)
    --------------------------------------------------------------------------------------#"""

    __CuentaCorriente = CuentaCorriente()
    __CDT = CDT()
    __CuentaAhorros = CuentaAhorros()

    """#---------------------------------------------------------------------------------------------------
    # Métodos
    ---------------------------------------------------------------------------------------------------#"""
    
    __method__="ConsignarCuentaCorriente"
    __params__="Monto"
    __returns__="nada"
    __descriptions__="Este metodo permite consignar un m onto a la cuenta corriente"
    def ConsignarCuentaCorriente(self, monto):
        # Aquí inicia mi metodo
        #self.__CuentaCorriente.Saldo=self.__CuentaCorriente.Saldo+monto #metodo no recomendado
        self.__CuentaCorriente.ConsignarValor(monto)
        
    __method__="CalcularSaldoTotal"
    __params__="Ninguno"
    __returns__="SaldoTotal"
    __descriptions__="Este metodo suma el saldo de todas las cuentas"
    def CalcularSaldoTotal(self):
        # Aquí inicia mi metodo
        total = self.__CuentaAhorros.DarSaldo() + self.__CuentaCorriente.DarSaldo()
        return total
    
    __method__="PasarAhorrosACorriente"
    __params__="Ninguno"
    __returns__="nada"
    __descriptions__="Este metodo transfiere el saldo de Ahorros a corriente"
    def PasarAhorrosACorriente (self):
        SaldoTemporal = self.__CuentaAhorros.DarSaldo()
        self.__CuentaAhorros.RetirarValor(SaldoTemporal)
        self.__CuentaCorriente.ConsignarValor(SaldoTemporal)
    
    __method__="IngresarNombre"
    __params__="Ninguno"
    __returns__="Nombre"
    __descriptions__="Este metodo permite ingresar un nombre"
    
    def IngresarNombre (self):
        # Aquí inicia mi metodo
        return self.Nombre
    
    __method__="IngresarCedula"
    __params__="Ninguno"
    __returns__="Cedula"
    __descriptions__="Este metodo permite ingresar una cedula"
    
    def IngresarCedula (self):
        # Aquí inicia mi metodo
        return self.Cedula
    
    __method__="Abrir_CuentaCorriente"
    __params__="Ninguno"
    __returns__="CuentaCorriente"
    __descriptions__="Este metodo permite Abrir una cuenta corriente"

    def Abrir_CuentaAhorros(self):
        # Aquí inicia mi metodo
        return self.CuentaCorriente
    
    __method__="Abrir_CDT"
    __params__="Ninguno"
    __returns__="CDT"
    __descriptions__="Este metodo permite Abrir un CDT"

    def Abrir_CDT (self):
        # Aquí inicia mi metodo
        return self.CDT
    
    __method__="Abrir_CuentaAhorros"
    __params__="Ninguno"
    __returns__="CuentaAhorros"
    __descriptions__="Este metodo permite Abrir una cuenta de ahorros"

    def Abrir_CuentaAhorros (self):
        # Aquí inicia mi metodo
        return self.CuentaAhorros