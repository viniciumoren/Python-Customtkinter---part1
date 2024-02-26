import os

def principal ():
    nomes = ['Marcio', 'Evelim','Vinicius','Emerson','Mateus','Amanda','Fabio','Gilson']

    print('Bem vindo ao Jogo da Adivinhação de Nomes')
    print('Tente adivinhar um nome')
    
    
    while True:
        palpite = input('Digite um nome:').strip().capitalize()
        os.system('cls')
        
        
        if verificarnome(palpite, nomes):
            print('Parabéns você acertou o nome')
            break
        else:
            print('Este nome não existe, tente novamente')
        
def verificarnome(palpite, nomes):
    if palpite in nomes:
        return True
    else:
        return False
    
principal()  
    