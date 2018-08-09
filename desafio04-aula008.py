#O intuito deste programa é sortear um de quatro alunos para apagar o quadro.

from random import randrange

#vetor de alunos para que haja possibilidade de fazer randomização
alunos = [input("Digite o nome do primeiro aluno"),
          input("Digite o nome do segundo aluno"),
          input("Digite o nome do terceiro aluno"),
          input("Digite o nome do quarto aluno")
          ]

num = randrange(0, 3)
print("O aluno selecionado foi {}.".format(alunos[num]))

#Outra maneira é proposta pelo G. Guanabara
#from random import choice
#print("{}".format(choice(alunos))
