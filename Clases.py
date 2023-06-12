class Fecha:
    def __init__(self, anho:int=2023, mes:int=5, dia:int=2):
        self.anho = anho
        self.mes=mes
        self.dia = dia
    def __repr__(self):
        return f'{self.dia}/{self.mes}/{self.anho}'
    def compareTo(self,fecha):
        fecha1 = ((self.anho*100)+self.mes)*100 + self.dia
        fecha2 = ((fecha.anho*100)+fecha.mes)*100 + fecha.dia
        return fecha1 - fecha2

class Persona:
    def __init__(self, nombre:str="", apellido:str="", nacimiento:Fecha=None):
        self.nombre = nombre
        self.apellido = apellido
        self.nacimiento = nacimiento
    def __repr__(self):
        return f'Persona -> nombre={self.nombre} apellido= {self.apellido} nacimiento={self.nacimiento}'
    def compareTo(self, persona):
        return self.nacimiento.compareTo(persona.nacimiento)

class Ordenador:
    def por_nacimiento(self, personitas):
        for externo in range(0,len(personitas)-1):
            for interno in range(1,len(personitas)):
                if personitas[externo].compareTo(personitas[interno]) > 0:
                    personitas[externo],personitas[interno] = personitas[interno], personitas[externo] #Compara 2 fechas
                    return personitas

