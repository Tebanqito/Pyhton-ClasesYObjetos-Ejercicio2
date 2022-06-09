class Alumno:
    _nombre = None
    _nota = 0

    def __init__(self, nombre, nota):
        self._nombre = nombre
        self._nota = nota

    def inicializarNombre(self, nombre):
        self._nombre = nombre

    def inicializarNota(self, nota):
        self._nota = nota

    def obtenerNombre(self):
        return self._nombre

    def obtenerNota(self):
        return self._nota

alumno = Alumno("Esteban", 10)

if alumno.obtenerNota() < 7:
    print("El alumno ", alumno.obtenerNombre(), " no ah aprobado")
else:
    print("El alumno ", alumno.obtenerNombre(), " si ah aprobado")