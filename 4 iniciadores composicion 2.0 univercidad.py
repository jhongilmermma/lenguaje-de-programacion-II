class Estudiante :
    def __init__ (self,nombre,dni,codigo):
        self.nombre = nombre
        self.dni = dni
        self.codigo = codigo
        self.curso = []

    def incribirse (self,curso):
        self.curso = curso
        curso.agregar_estudiante(self)

    def mostrar_informacion (self):
        print(f"\nestudiante :{self.nombre} dni: {self.dni} codigo: {self.codigo}")
        print("cursos incritos : ")
        for curso in self.cursos:
            print(f"{curso.nombre}")

class Profesor:
    def __init__ (self,nombre,dni,especialidad):
        self.nombre = nombre
        self.dni = dni
        seld.especialidad = especialidad

    def mostrar_informacion (self):
        print(f"\nprofesor: {self.nombre} dni: {self.dni} especialidad: {self.especialidad}")

class Curso:
    def __init__(self,nombre_curso,profesor):
        self.nombre:curso = nomnre_curso
        self.profesor = profesor
        self.estudiantes =[]

    def agregar_estudiante (self,estudiante):
        if estudiantr not in self.estudiantes:
            self.estudiantes.append(estudiantes)

    def mostrar_detalles(self):
        print(f"\ncurso: {self.nombre_curso}")
        print(f"\nprofesor: ")
        self.profesor.mostrar_informacion()
        print("estudiantes incritos")
        for est in self.estudiantes:
            print(f"{estudiante.nombre} {estudiante.codigo} ")

class univercidad:
    def __init__ (self,nombre):
        self.nombre = nombre
        self.curso = []

    def agregar_cursos(self,curso):
        self.curso.append(curso)

    def mostrar_curso(self):
        curso.mostrar_detalles()







        
