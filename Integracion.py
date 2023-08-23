# ejercicio 1 y 2
'''
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return (a * b) // gcd(a, b)


num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))

mcd = gcd(num1, num2)
mcm = lcm(num1, num2)

print(f"El Máximo Común Divisor entre {num1} y {num2} es: {mcd}")
print("")
print(f"El Mínimo Común Múltiplo entre {num1} y {num2} es: {mcm}")
'''
'''
#ejercicio 3

def contar_palabras(cadena):
    palabras = cadena.split()
    frecuencia = {}
    
    for palabra in palabras:
        if palabra in frecuencia:
            frecuencia[palabra] += 1
        else:
            frecuencia[palabra] = 1
    
    return frecuencia

cadena = input("Ingrese una cadena de caracteres: ")
resultado = contar_palabras(cadena)

print("Frecuencia de palabras:")
for palabra, frecuencia in resultado.items():
    print(f"{palabra}: {frecuencia}")

'''

#ejercicio 4
'''
def contar_palabras(cadena):
    palabras = cadena.split()
    frecuencia = {}
    
    for palabra in palabras:
        if palabra in frecuencia:
            frecuencia[palabra] += 1
        else:
            frecuencia[palabra] = 1
    
    return frecuencia

def palabra_mas_repetida(diccionario):
    palabra_max = max(diccionario, key=diccionario.get)
    frecuencia_max = diccionario[palabra_max]
    return (palabra_max, frecuencia_max)

cadena = input("Ingrese una cadena de caracteres: ")
diccionario = contar_palabras(cadena)
palabra_repetida, frecuencia_repetida = palabra_mas_repetida(diccionario)

print("Frecuencia de palabras:")
for palabra, frecuencia in diccionario.items():
    print(f"{palabra}: {frecuencia}")

print(f"Palabra más repetida: {palabra_repetida}, Frecuencia: {frecuencia_repetida}")
'''

#ejercicio 5

'''

'''

#ejercicio 6
class Persona():
    def __init__(self,Nombre="",Edad=0,dni=""):
        self.nombre=Nombre
        self.edad=Edad
        self.dni=dni

    def GetNombre(self):
        return self.nombre
    def GetEdad(self):
        return self.edad
    def GetDni(self):
        return self.dni
    
    def SetNombre(self,name):
        self.nombre= name
    def SetEdad(self,age):
        self.edad = age
    def SetDni(self,id):
        self.dni= id
    
    def Mostrar(self):
        print(f"nombre: {self.nombre}\n edad: {self.edad} \n DNI:{self.dni}")

    def Es_mayor_de_edad(self):
        if self.edad >= 18:
            return True
        else:
            return False
        
#ejercicio 7

class Cuenta(Persona):
    def __init__(self,nombre,dni,cantidad,edad):
        super().__init__(nombre,dni,edad)
        
        self.cantidad = cantidad

    def GetCantidad(self):
        return self.cantidad
    
    def SetCantidad(self,cantidad):
        self.cantidad= cantidad
    def Mostrar(self):
        print(f"nombre: {self.nombre}\n edad: {self.edad} \n DNI:{self.dni} \n dinero total:{self.cantidad}")
    
    def ingresar(self,dinero):
        if dinero<0:
            print("No se puede ingresar cantidades negativas")
        else:
            self.cantidad += dinero

    def retirar(self,dinero):
        if dinero <0:
            print("no puedes retirar cantidades negativas")
        else:
            self.cantidad =- dinero

class CuentaJoven(Cuenta):
    def __init__(self,nombre,dni,cantidad,edad,bonificacion= 10):
        super.__init__(nombre,dni,cantidad,edad)
        self.bonificacion = bonificacion

    def es_titular_valido(self):
        if self.edad> 25 or self.edad<18:
            return False
        else:
            return True
    
    def retirar(self,dinero):
        if self.es_titular_valido() and dinero>0:
            self.cantidad =- dinero
        else:
            print("no puedes retirar cantidades negativas")

    def mostrar(self,dinero):
        print(f"Cuenta joven {self.bonificacion}%")