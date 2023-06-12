from Clases import Fecha,Persona,Ordenador

if __name__=='__main__':
    persona = Persona(nombre='Peter', apellido='Parker', nacimiento =Fecha(anho=1999, mes=12, dia=31))
    print(persona)

#otra consigna
if __name__=='__main__':
    ordenador = Ordenador()
    personas = []
    personas.append(Persona(nombre='Bruce',apellido='Wayne', nacimiento=Fecha(1950,3,1)))
    personas.append(Persona(nombre='Clark',apellido='Kent',nacimiento=Fecha(1875,4,7)))
    personas.append(Persona(nombre='Arthur',apellido='Curry',nacimiento=Fecha(1955,12,1)))
    personas = ordenador.por_nacimiento(personas)
    print(personas)

import unittest
class TestOrdenador(unittest.TestCase):

    def test_2_personas(self):
        persona1 = 1800
        persona2 = 1900
        self.assertEqual(self.ordenador,ordenador.por_nacimiento(persona1 < persona2))
    
    def test_2_iguales(self):
        persona1 = 2000
        persona2 = 2000
        self.assertEqual(self.ordenador,ordenador.por_nacimiento(persona1 = persona2))

    def test_3_personas(self):
        pass

if __name__ == '__main__':
    unittest.main