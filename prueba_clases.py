from datetime import datetime

class Contacto:
    def __init__(self, nombre, apellido, numero, email, fecha_nacimiento):
        self.nombre = nombre
        self.apellido = apellido
        self.numero = numero
        self.email = email
        self.fecha_nacimiento = fecha_nacimiento

    def full_name(self):
        return self.nombre + " " + self.apellido

    def edad(self):
        today = datetime.today()
        return today.year


contacto = Contacto("David", "Rosingana", "657596874", "david@david.com", "23/09/1994")

print(contacto.full_name())