#O intuito do programa é calcular a área de uma parede e receber de volta o volume de tinta para que ela seja pintada

height = float(input("Digite a altura da parede:"))
width = float(input("Digite a largura da parede"))
area = height*width
print("A área da parede é {}, logo o volume de tinta necessário para pintala é {}".format(area, area/2))
#Foi tomado por definição que um litro de tinta pinta 2m^2