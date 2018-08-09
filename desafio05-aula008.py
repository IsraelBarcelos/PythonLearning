#O intuito deste programa é sortear a ordem de apresentação de trabalhos de 4 grupos
#Do a non-repeat random
from random import sample


alunos = [input("Digite o nome do grupo 1"),
          input("Digite o nome do grupo 2"),
          input("Digite o nome do grupo 3"),
          input("Digite o nome do grupo 4")
          ]
result = sample(range(0, 4), 4)
print(alunos[result[0]], alunos[result[1]], alunos[result[2]], alunos[result[3]])


#Outro método proposto pelo G Guanabara foi:
#print("{}".format(shufle(alunos)))
# O que é consideravelmente melhor.