#O intuito do programa é ler um angulo e apresentar o valor de suas projeções. // read angle and present projections

#A pessoa digita um valor em graus // user type degree value

from math import radians, sin, cos, tan

#simples import de radians // simple importation of radians

# a conversão para radianos para utilização das funções sin e cos // it has to be converted to radians to work methods.

ang = radians(float(input("Digite um valor em graus")))

print("O seno é {}, o cosseno é {} e a tangente é {}.".format((sin(ang)), cos(ang), tan(ang)))
