#------------------------------------------------------------------------------------------------------------------------------------------------------------#
#1) Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, 
#utilizando as seguintes fórmulas:
#a. Para homens: (72.7*h) - 58       
#b. Para mulheres: (62.1*h) - 44.7	

genero = input('Digite o seu gênero, M para masculino e F para feminino: ')
if 'M' in genero:
    alturadapeossa = float(input('Digite aqui a sua altura e vamos lhe informar qual seria o seu peso ideal para o genêro masculino: '))
    pesoideal = (alturadapeossa * 72.7) - 58
    print (f'O seu peso ideal é: {pesoideal:.2f}')
elif 'F' in genero:
    alturadapeossa = float(input('Digite aqui a sua altura e vamos lhe informar qual seria o seu peso idealpara o genêro feminino: '))
    pesoideal = (alturadapeossa * 62.1) - 44.7
    print (f'O seu peso ideal é: {pesoideal:.2f}')
    
#Com a função input, pude perguntar se a pessoa era do genêro masculino ou feminino, com isso, utilizei o if, podendo assim, criar duas situações 
#diferentes, uma para se a pessoa é mulher e outra se é homem. Como resultado final, dando o peso ideal do invíduo dependendo do seu gênero.
#------------------------------------------------------------------------------------------------------------------------------------------------------------#
#2) João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o
#rendimento diário de seu trabalho. Toda vez que ele traz um peso de peixes maior que o
#estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) deve pagar uma
#multa de R$ 4,00 por quilo excedente. João precisa que você faça um programa que leia a
#variável peso (peso de peixes) e calcule o excesso. Gravar na variável excesso a quantidade
#de quilos além do limite e na variável multa o valor da multa que João deverá pagar. Imprima
#os dados do programa com as mensagens adequadas.

pesca = float(input('Quantidade do peso da pesca do dia: '))
if pesca > 50:
    Pescaexcedente = (pesca - 50)
    multa = Pescaexcedente * 4.00
    print(f'A pesca excedeu um total de {Pescaexcedente} quilos, criando-se assim, uma multa de {multa:.2f}R$')
else:
    print('A pesca de hoje não excedeu nenhum quilo ;)')
    
#Primeiro criei uma variável pesca, para saber qual foi a quantidade de kg da pesca no dia
#segundo, utilizei a função if, para que caso tenha ultrapassado o limite (50kg) emita uma mensagem.
#------------------------------------------------------------------------------------------------------------------------------------------------------------#
#3) Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas
#no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados
#11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos
#dê:
#a. salário bruto.
#b. quanto pagou ao INSS.
#c. quanto pagou ao sindicato.
#d. o salário líquido.
#e. calcule os descontos e o salário líquido, conforme a tabela abaixo:

hora = float(input('Quantos R$ voce ganha por hora?: '))
hora_mes = float(input('Quantas horas você trabalha por mês?: '))
salário_bruto =  hora * hora_mes 
IR = salário_bruto*11/100
INSS = salário_bruto*8/100
SINDICATO = salário_bruto*5/100
liquido = salário_bruto - salário_bruto*24/100

print(f'O seu salário bruto é {salário_bruto}')
print(f'Valor total pago para o IR é de {IR}')
print(f'Valor total pago para o INSS é de {INSS}')
print(f'Valor total pago para o sindicato é de {SINDICATO}')
print(f'O seu salário liquído é {liquido}')

#Usei a função input para perguntar pra pessoa quanto que ela ganha por hora e 
#quantas horas a pessoa trabalha por mes. Com isso, fiz todos os cálculos necessários 
#para se obter os respectivos valores pedidos. 
#------------------------------------------------------------------------------------------------------------------------------------------------------------#
#2.2)Faça um Programa que peça um número inteiro e determine se ele é par ou ímpar.

onumero = int(input('Informe um número para saber se ele é ímpar ou par: '))
parimpar = onumero % 2 
if parimpar == 0:
    print('O seu número é par')
else:
    print('O seu número é impar')

#Perguntei primeiro qual número ele desejaria usar, depois, criei uma variável para saber o resto da divisão por 2
#Sabemos que qualquer numero par, a sua divisão por dois sempre resultará em zero, já um número impar, não. Sendo assim, utilizei 
#o if e o else para as duas situações.
#------------------------------------------------------------------------------------------------------------------------------------------------------------#
#2.3)Faça um Programa que peça um número e informe se o número é inteiro ou decimal. 

numerointdec = float(input('Digite um número para saber se ele é decimal ou inteiro: '))
if (numerointdec // 1) == numerointdec:
    print('O seu número é inteiro')
else:
    print('O seu número é decimal')

#Pedi para colocar o número usando a função input com float, depois, coloquei a seguinte condição utilizando o if:
#Usando o operador de divisão INTEIRA, se o número dividido for igual a ele mesmo, significa que é inteiro, se não (else), é decimal.
#------------------------------------------------------------------------------------------------------------------------------------------------------------#
#2.4)Faça um Programa que leia uma estrutura A com 10 números inteiros, calcule e mostre a soma
#dos quadrados dos elementos desta estrutura.

somaqdrdo = 0
for i in range(10):
    somaqdrdo += int(input(f"{i+1}º número int: ")) 
    somatotal = somaqdrdo ** 2
print(f"A soma dos quadrados dos numeros digitados é {somatotal}")

#criei um for para ir de 0 até 9, depois, somei o (somaqdrdo == 0) + os números inteiros que a pessoa digitou
#depois disso, utlizei o operadorar para soma dos quadrados. e no final, dando print na soma desses valores.
#------------------------------------------------------------------------------------------------------------------------------------------------------------#