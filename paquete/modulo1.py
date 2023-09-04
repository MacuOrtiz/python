class Cliente:
    def __init__(self, nombre, apellido, edad, correo, genero):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.correo = correo
        self.genero = genero 



    def __str__(self):
        return f"El clinete {self.nombre} {self.apellido} tiene {self.edad} años"




