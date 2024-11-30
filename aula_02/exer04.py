import os 
import platform
def obrigado():
    print("obrigado por utilizar o nosso sistema!!")

while True: 
    os.system("cls")
    
    obrigado()
    
    nome = input("digite seu nome")
    
    print ("Seja Bem vindo,", nome)
    
    nome=str(input("digite seu nome: "))
    

    idade = int(input("digite sua idade: "))

    if idade <= 12:
        print("você é criança")
        
    elif idade < 18:
        print("você é um adolecente")
        
    elif idade <= 24 :
        print("você é jovem")
        
    elif idade < 60: 
        print("você ja é adulto")
        
    else:
        print("você ja e idoso")

    resposta = input("deseja nova consulta? s/n: ").strip().upper()
    if resposta != "S" :
        break
    
obrigado()