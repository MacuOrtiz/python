from paquete.modulo1 import Cliente
from paquete.modulo2 import Comprar
from paquete1.paquete1 import Usuario #paquete redistribuible 

usuario1= Usuario("Joseo66", "jo21@gmail.com")#paquete redistribuible 
print(usuario1)#paquete redistribuible 

cliente1 = Cliente("Jose", "Ortiz", 21, "jo21@gmail.com", "masculino")
compra1 = Comprar("pantaloneta", "deportiva", 50, 2, cliente1.nombre, cliente1.apellido, cliente1.edad, cliente1.correo, cliente1.genero)

print(cliente1)
print(compra1)
