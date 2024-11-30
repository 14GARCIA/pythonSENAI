import os 
import platform
def obrigado():
    print("obrigado por utilizar o nosso sistema!!")

while True: 
    os.system("cls")
    obrigado()
    nome = input("digite seu nome")
    print ("Seja Bem vindo,", nome)
    print("\t Calculadora \t")
    ope = int(input("digite o que deseja fazer 1-soma; 2-subtração 3-multiplicacao 4-divisão"))
    if ope == 1 :
         n1=float(input("digite o primeiro numero"))
         n2=float(input("digite o segundo numero"))
         soma = n1+n2
         print(f"O resultado da conta{n1}+{n2} foi: {soma}")
    elif ope == 2:
        n1=float(input("digite o primeiro numero"))
        n2=float(input("digite o segundo numero"))
        subtracao = n1-n2
        print(f"O resultado da conta{n1}-{n2} foi: {subtracao}")
    elif ope == 3:
        n1=float(input("digite o primeiro numero"))
        n2=float(input("digite o segundo numero"))
        multiplicacao = n1*n2 
        print(f"O resultado da conta{n1}*{n2} foi: {multiplicacao}")
    elif ope == 4:
         n1=float(input("digite o primeiro numero"))
         n2=float(input("digite o segundo numero"))
         if n2 != 0:
             divisao = n1/n2
             print(f"O resultado da conta{n1}/{n2} foi: {divisao}")
             
         else:
            print("erro divisao por 0")
  
   
    resposta = input("deseja nova consulta? s/n: ").strip().upper()
    if resposta != "S" :
        break
    
obrigado()


