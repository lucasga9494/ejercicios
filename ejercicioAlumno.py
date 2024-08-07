class notaAlumno():
    def __init__(self,alumno,nota1,nota2,nota3,sumaNota):
        self.nota1=nota1
        self.nota2=nota2
        self.nota3=nota3
        self.sumaNota=sumaNota
        self.alumno=alumno
        
        if self.sumaNota >=6:
            print('El alumno ',self.alumno,' Aprobo')   
        else:
            print('El alumno Reprobo')

def menu():
  
    alumno=input('Nombre del alumno/a: ')
    nota1=int(input('Nota 1: '))
    nota2=int(input('Nota 2: '))
    nota3=int(input('Nota 3: '))
    sumaNota=((nota1+nota2+nota3)/3)
    notaAlumno(alumno,nota1,nota2,nota3,sumaNota)

menu()