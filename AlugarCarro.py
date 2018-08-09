#O intuito do programa é utilizar matemática e lógica para um problema simples.

numDias = float(input("Qual o número de dias rodados com o carro?"))
numKM = float(input("Qual o número de kilometros rodados?"))
print("O valor total do aluguel do é de {} R$".format(numDias*60+numKM*0.15))
#Não é necessário neste caso a utilização de parenteses para separar o cálculo matemático