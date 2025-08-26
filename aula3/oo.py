class Aluno:
    def __init__(self, nome, ra):
        self._nome = nome
        self._ra = ra
    
    def estudar(self):
        print('Estudando')
    
    def colar(self, materia):
        print("colando " + materia)

    def __str__(self):
        return("Aluno: " + self._nome + ' RA: ' + self._ra)    

    def __repr__(self):
        return("Aluno: " + self._nome)   


aluno1 = Aluno('José','12345')
aluno2 = Aluno('Maria','23456')
print(aluno1)
print(aluno2)