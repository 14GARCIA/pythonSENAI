# Exercicio2- faca um programa que cadastre(nome,sobrenome, idade, ra)peca 4 nota bimestrais e tire a media 

print("\t ----Cálculo da média----")

# nome = input("Digite seu nome: ")
# sobrenome = input("Digite seu sobrenome: ")
# idade = input("Digite sua idade: ")
# cidade= input("Digite sua cidade: ")
# RA = input("Digite seu RA: ")
# n1 = int(input("digite a nota do primeiro bimestre"))
# n2 = int(input("digite a nota do segundo bimestre"))
# n3 = int(input("digite a nota do terceiro bimestre"))
# n4 = int(input("digite a nota do quarto bimestre"))
    
nota = []
for i in range(4):
   nota.append(int(input("digite uma das notas do bimestre bimestre"))) 

soma =sum(nota)
media =soma / len(nota)
print (media)


