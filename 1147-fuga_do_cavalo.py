import string

jogadas_cavalo = []
cont = 1
direcoes_cavalo = [-2, -1,-2,1,2,1,2,-1]
direcoes_peao = [-1,-1,1,-1]

def convert_ascii_low(letra):
    return (ord(letra)-97)

def jg_cavalo(letra, numero):
    letra_ascii = convert_ascii_low(letra)
    numero = int(numero) 
    
    for i in range(0,7,2):

        letra = letra_ascii+direcoes_cavalo[i]
        num = numero+direcoes_cavalo[i+1]
        letra_ = letra_ascii+direcoes_cavalo[i+1]
        num_ = numero+direcoes_cavalo[i]

        if letra in range(0,8) and num in range(1,9):
            jogadas_cavalo.append(f"{string.ascii_lowercase[letra]}{num}")
        if letra_ in range(0,8) and num_ in range(1,9):
            jogadas_cavalo.append(f"{string.ascii_lowercase[letra_]}{num_}")

    return jogadas_cavalo

def jg_peoes(letra, numero):

    letra_ascii = convert_ascii_low(letra)
    numero = int(numero)

    for i in range(0,4,2):
        letra = letra_ascii+direcoes_peao[i]
        num = numero+direcoes_peao[i+1]
        if letra >= 0 and num >= 1 and str(f"{string.ascii_lowercase[letra]}{num}") in jogadas_cavalo:
            jogadas_cavalo.remove(f"{string.ascii_lowercase[letra]}{num}")

while True:
    
    first = input()
    if first == "0":
        break
    n, l = list(first)
    jg_cavalo(l,n)
    for i in range(8):
        posicao, letra = list(input())
        jg_peoes(letra, posicao)

    print(f"Caso de Teste #{cont}: {len(jogadas_cavalo)} movimento(s).")
    cont += 1
    jogadas_cavalo = []

