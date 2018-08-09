#O intuito do programa é retornar a hipotenusa de um número.

#from math import sqrt
#from math import pow
#catOp = float(input("Digite o valor do cateto oposto:"))
#catAdj = float(input("Digite o valor do cateto adjacente:"))
#print("A hipotenusa do triângulo retângulo é {}".format(sqrt(pow(catOp, 2)+pow(catAdj, 2))))
#Uma forma mais facil, utilizando o método hypot é :

from math import hypot
print("O valor da hipotenusa é {}".format(hypot(float(input("Digite o valor do cateto oposto")),
                                                float(input("Digite o valor do cateto adjacente")))))
