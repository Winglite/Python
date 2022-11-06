# DESAFIO 1

# Dada a letra N do alfabeto, nos diga qual a sua posição.
# ENTRADA: Um único caracter N, uma letra maiúscula ('A'-'Z') do alfabeto (que contém 26 letras).
# SAÍDA: Um único inteiro, que representa a posição da letra no alfabeto.

letra1 = input("Informe uma letra de A a Z: ")
letra = letra1.upper()

# imprima a posição dessa letra no Alfabeto;
lista = [chr(i) for i in range(ord('A')-1, ord('Z')+1)]
print(lista.index(letra))



# DESAFIO 2

#Humberto tem um papagaio muito esperto. Quando está com as duas pernas no chão, o papagaio fala em português
#Quando levanta a perna esquerda, fala em inglês. Por fim, quando levanta a direita fala em francês. Nico,
#amigo de Humberto, ficou fascinado com o animal. Em sua emoção perguntou: “E quando ele levanta as duas?”.
#Antes que Humberto pudesse responder, o papagaio gritou: “Aí eu caio, idiota!”.

#ENTRADA: A entrada consiste de diversos casos de teste. Cada caso de teste consiste uma string informando qual
# a situação de levantamento de pernas do papagaio.

#SAIDA: Para cada condição de levantamento de pernas do papagaio, imprima a linguagem que ele utilizará.
#  Caso ele levante ambas as pernas, imprima “caiu”. Quebre uma linha a cada caso de teste.


while True: 
    try: 
        perna = input()
           #Programe aqui dentro as condições necessárias para satisfazer o problema
        if perna == "esquerda":
            print("ingles")
        elif perna == "direita":
            print("frances")
        elif perna == "nenhuma":
            print("portugues")
        elif perna == "ambas":
            print("caiu")
           # e imprima a saída de acordo com a situação das pernas do papagaio
    except EOFError: 
        break




#DESAFIO 3
#A empresa que você trabalha resolveu conceder um aumento salarial a todos funcionários, de acordo com a tabela abaixo:

#Salário	         Percentual de Reajuste
#0 - 600.00               17%
#600.01 - 900.00          13% 
#900.01 - 1500.00         12%
#1500.01 - 2000.00        10%
#Acima de 2000.00         5%

#Leia o salário do funcionário e calcule e mostre o novo salário, 
#bem como o valor de reajuste ganho e o índice reajustado, em percentual.

#A entrada contém apenas um valor de ponto flutuante, que pode ser maior ou igual a zero, 
#com duas casas decimais, conforme exemplos abaixo.

#Entrada	       Saída
#1000	         Novo salario: 1120,00 
#                Reajuste ganho: 120,00                                                                                     
#                Em percentual: 12 %



salario = int(input()) 
porcentagem_aumento1 = 0.17
porcentagem_aumento2 = 0.13
porcentagem_aumento3 = 0.12
porcentagem_aumento4 = 0.10
porcentagem_aumento5 = 0.05

if (salario <=600.0):
    salario_novo = salario + (salario * 0.17)
    reajuste = porcentagem_aumento1 * salario
    percentual = porcentagem_aumento1 * 100

elif (salario >= 600.01 and salario <= 900.00):
    salario_novo = salario + (salario * 0.13)
    reajuste = porcentagem_aumento2 * salario
    percentual = porcentagem_aumento2 * 100

elif (salario >= 900.01 and salario <= 1500.00):
    salario_novo = salario + (salario * 0.12)
    reajuste = porcentagem_aumento3 * salario
    percentual = porcentagem_aumento3 * 100

elif (salario >=1500.01 and salario <= 2000.00):
    salario_novo = salario + (salario * 0.10)
    reajuste = porcentagem_aumento4 * salario
    percentual = porcentagem_aumento4 * 100

else: 
    salario_novo = salario + (salario * 0.05)
    reajuste = porcentagem_aumento5 * salario
    percentual = porcentagem_aumento5 * 100
    
salario_novo = f'{salario_novo:.2f}'

reajuste = f'{reajuste:.2f}'

percentual = f'{percentual:.0f}'

# TODO:  Calcule o salário do funcionário e print o novo salário, bem como o valor de reajuste ganho e o índice reajustado (em porcentagem)
print(f'Novo salario: {salario_novo}\n Reajuste ganho: {reajuste}\n Em percentual: {percentual} %')