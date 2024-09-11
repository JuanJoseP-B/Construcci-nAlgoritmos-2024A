__autor__ = "Gabriel Esteban Paz Guerrero"
__license__ = "GPL"
__version__ = "1.0.0"
__email__ = "gabriel.pazg@campusucc.edu.com"

'''----------------------------------------------------------------
#Importaciones
----------------------------------------------------------------'''
from Fecha import Fecha

class Empleado:
    # Aquí inicia mi clase
    """#--------------------------------------------------------------------------------------------------------------------------------
    # Atributos
    --------------------------------------------------------------------------------------------------------------------------------#"""
    nombre = ""
    apellido = ""
    salario = 0

    '''#-------------------------------------------------------------------------------------------------
    # 1 Masculino y 2 femenino
    -------------------------------------------------------------------------------------------------#'''
    Sexo = 0

    '''#-------------------------------------------------------------------------------------------------
    # Asociaciones
    --------------------------------------------------------------------------------------------------'''

    fechaNacimiento = Fecha()
    fechaIngreso = Fecha()

    """#-------------------------------------------------------------------------------------------------
    # Métodos
    -------------------------------------------------------------------------------------------------#"""
    
    __method__="Cambiar_Salario"
    __params__="nuevoSalario"
    __returns__="nada"
    __descriptions__="Este metodo permite cambiar el salario del empleado por uno nuevo"

    def Cambiar_Salario (self, nuevoSalario):
        # Aquí inicia mi metodo
        self.salario = nuevoSalario
        
    __method__="DarSalario"
    __params__="ninguno"
    __returns__="Salario empleado"
    __descriptions__="Devuelve el salario del empleado"
        
    def DarSalario(self):
        #Aqui inicia el metodo
        return self.salario
    
    __method__="AumentoSalarial"
    __params__="Aumento"
    __returns__="Ninguno"
    __descriptions__="Permite aumentar el salario en un  valor ingresado por el usuario"
    
    def AumentoSalarial(self, aumento):
        #Aqui inicia el metodo
        self.Salario = self.salario + aumento
        
    __method__="CalcularSalarioAnual"
    __params__="Ninguno"
    __returns__="Salario anual"
    __descriptions__="permite calcular el salario anual del empleado"
    def CalcularSalarioAnual(self):
        #aqui empieza mi método
        return self.salario*12
    
    __method__="CalcularImpuestoSalarialAnual"
    __params__="Ninguno"
    __returns__="Impuesto del salario anual"
    __descriptions__="permite calcular el impuesto a el salario anual del empleado"
    def CalcularImpuestoSalarialAnual (self):
        #aqui empieza mi método
        SalarioAnual = self.CalcularSalarioAnual()
        return SalarioAnual * 0.19
    
    __method__="CalcularImpuestoSalarialMesual"
    __params__="Ninguno"
    __returns__="Impuesto del salario mensual"
    __descriptions__="permite calcular el impuesto a el salario mensual del empleado"
    def CalcularImpuestoMensual (self):
        #aqui empieza mi método
        SalarioMesual = self.salario
        return SalarioMesual * 0.19
        #Forma 2
        #return self.Salario * 0.19
        #Forma 3
        #return self.DarSalario() * 0.19
        
    __method__="DarFechaIngreso"
    __params__="Ninguno"
    __returns__="FechaIngreso"
    __descriptions__="Muestra la fevha de ingreso del empleado"
    def DarFechaIngreso(self):
        # Aquí empieza mi método
        return self.fechaIngreso.Dar_Fecha()
    
    __method__="DarFechaNacimiento"
    __params__="Ninguno"
    __returns__="Fecha de nacimiento"
    __descriptions__="Muestra la fecha de nacimiento del empleado"
    def DarFechaNacimiento(self):
        # Aquí empieza mi método
        return "Tu fecha de nacimiento es: "+ self.fechaNacimiento.Dar_Fecha()
    