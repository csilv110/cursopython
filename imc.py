Sair = 'Não'
while Sair == 'Não':
   peso = float(input("Digite seu peso: "))
   altura = float(input("Digite sua altura: "))

   imc = peso / (altura*altura)

   print('Seu IMC é ',imc)

   Sair = input('Deseja sair? Sim/Não: ')
