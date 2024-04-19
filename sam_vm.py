import sys
import re

def avaliar(instrucoes, pilha):
    comando = ""
    valor = ""
    index = 0
    fbr = 0
    while index < len(instrucoes):
        x = instrucoes[index]
        if (len(x)>1):
            #print("Primeiro Caso")
            comando = x[0]
            print(comando)
            valor = x[1]
            print(valor)
        else:
            #print("Segundo Caso")
            comando = x[0]
            print(comando)

        # Inserção de valores
        if comando == "PUSHIMM":
            print("Valor inserido")
            pilha.append(int(valor))
        # Manipulação de pilha
        elif comando == "ADDSP":
            print("Aloca espaco na pilha")
            for x in range(abs(int(valor))):
                if int(valor) > 0:
                    pilha.append(0)
                else:
                    pilha.pop()
        elif comando == "STOREABS":
            print("Armazena valor em posicao absoluta")
            pilha[int(valor)] = pilha.pop()
        elif comando == "STOREOFF":
            print("Armazena valor em posicao relativa")
            pilha[int(fbr) + int(valor)] = pilha.pop()
        elif comando == "PUSHABS":
            print("Pega valor de posicao absoluta")
            pilha.append(pilha[int(valor)])
        elif comando == "PUSHOFF":
            print("Pega valor de posicao relativa")
            pilha.append(pilha[int(fbr) + int(valor)])
        
        # Operações aritméticas com inteiros
        elif comando == "ADD":
            print("Soma")
            tam_pilha = len(pilha)
            pilha[tam_pilha-2] = (pilha[tam_pilha-2] + pilha[tam_pilha-1])
            pilha.pop()
        elif comando == "SUB":
            print("Subtracao")
            tam_pilha = len(pilha)
            pilha[tam_pilha-2] = (pilha[tam_pilha-2] - pilha[tam_pilha-1])
            pilha.pop()
        elif comando == "TIMES":
            print("Multiplicacao")
            tam_pilha = len(pilha)
            pilha[tam_pilha-2] = (pilha[tam_pilha-2] * pilha[tam_pilha-1])
            pilha.pop()
        elif comando == "DIV":
            print("Divisao")
            tam_pilha = len(pilha)
            pilha[tam_pilha-2] = (pilha[tam_pilha-2] / pilha[tam_pilha-1])
            pilha.pop()
        elif comando == "MOD":
            print("Modulo")
            tam_pilha = len(pilha)
            pilha[tam_pilha-2] = (pilha[tam_pilha-2] % pilha[tam_pilha-1])
            pilha.pop()

        # Operações lógicas
        elif comando == "AND":
            print("E")
            tam_pilha = len(pilha)
            pilha[tam_pilha-2] = (1 if ((pilha[tam_pilha-2] != 0) & (pilha[tam_pilha-1] != 0)) else 0)
            pilha.pop()
        elif comando == "NAND":
            print("Nao E")
            tam_pilha = len(pilha)
            pilha[tam_pilha-2] = (0 if ((pilha[tam_pilha-2] != 0) & (pilha[tam_pilha-1] != 0)) else 1)
            pilha.pop()
        elif comando == "OR":
            print("Ou")
            tam_pilha = len(pilha)
            pilha[tam_pilha-2] = (1 if ((pilha[tam_pilha-2] != 0) | (pilha[tam_pilha-1] != 0)) else 0)
            pilha.pop()
        elif comando == "NOR":
            print("Nao Ou")
            tam_pilha = len(pilha)
            pilha[tam_pilha-2] = (0 if ((pilha[tam_pilha-2] != 0) | (pilha[tam_pilha-1] != 0)) else 1)
            pilha.pop()
        elif comando == "NOT":
            print("Nao")
            tam_pilha = len(pilha)
            pilha[tam_pilha-1] = (1 if pilha[tam_pilha-1] == 0 else 0)
        elif comando == "XOR":
            print("Ou exclusivo")
            tam_pilha = len(pilha)
            pilha[tam_pilha-2] = (1 if ((pilha[tam_pilha-2] != 0) ^ (pilha[tam_pilha-1] != 0)) else 0)
            pilha.pop()

        # Operações de comparação
        elif comando == "EQUAL":
            print("Igualdade")
            tam_pilha = len(pilha)
            pilha[tam_pilha-2] = (1 if pilha[tam_pilha-2] == pilha[tam_pilha-1] else 0)
            pilha.pop()
        elif comando == "GREATER":
            print("Maior")
            tam_pilha = len(pilha)
            pilha[tam_pilha-2] = (1 if pilha[tam_pilha-2] > pilha[tam_pilha-1] else 0)
            pilha.pop()
        elif comando == "LESS":
            print("Menor")
            tam_pilha = len(pilha)
            pilha[tam_pilha-2] = (1 if pilha[tam_pilha-2] < pilha[tam_pilha-1] else 0)
            pilha.pop()
        elif comando == "ISNIL":
            print("Nulo")
            tam_pilha = len(pilha)
            pilha[tam_pilha-1] = (1 if pilha[tam_pilha-1] == 0 else 0)
        elif comando == "CMP":
            print("Compara")
            tam_pilha = len(pilha)
            pilha[tam_pilha-2] = (1 if pilha[tam_pilha-2] < pilha[tam_pilha-1] else (-1 if pilha[tam_pilha-2] > pilha[tam_pilha-1] else 0))
            pilha.pop()
        elif comando == "ISPOS":
            print("Positivo")
            tam_pilha = len(pilha)
            pilha[tam_pilha-1] = (1 if pilha[tam_pilha-1] > 0 else 0)
        elif comando == "ISNEG":
            print("Negativo")
            tam_pilha = len(pilha)
            pilha[tam_pilha-1] = (1 if pilha[tam_pilha-1] < 0 else 0)

        # Comandos de fluxo
        elif comando == "JUMP":
            print("Pula")
            index = instrucoes.index([valor])
            print(index)
            x = instrucoes[index]
        elif comando == "JUMPC":
            print("Pula condicional")
            tam_pilha = len(pilha)
            if pilha[tam_pilha-1] == 1:
                index = instrucoes.index([valor])
                print(index)
                x = instrucoes[index]
                pilha.pop()
            else:
                pilha.pop()
        elif comando == "JUMPIND":
            print("Pula indireto")
            index = int(pilha.pop())
            print(index)
            x = instrucoes[index]
        elif comando == "RST":
            print("Pula indireto")
            index = int(pilha.pop())
            print(index)
            x = instrucoes[index]
        elif comando == "JSR":
            print("Chama rotina")
            pilha.append(index)
            index = instrucoes.index([valor])
            print(index)
            x = instrucoes[index]
        
        # Comandos de manipulação de registradores e FBR
        elif comando == "LINK":
            print("Adiciona o FBR na pilha e FBR = SP - 1")
            pilha.append(fbr)
            fbr = len(pilha)-1
            print("fbr = ", fbr)
        elif comando == "UNLINK":
            print("Retira o FBR da pilha e FBR = SP")
            fbr = pilha.pop()
            print("fbr = ", fbr)
        elif comando == "POPFBR":
            print("Retira o FBR da pilha e FBR = SP")
            fbr = pilha.pop()
            print("fbr = ", fbr)
                
        # Comandos de parada
        elif comando == "STOP":
            print("Finalizou com")
            print(pilha[0])
            if len(pilha) > 1:
                print("Aviso: Ainda tem ", len(pilha)-1, " valores na pilha")
            break

        index += 1
        print("Pilha: ", pilha)

def trata_instrucao(instrucao):
    regex = r"^(\w+)(?:\s([A-Z0-9-]+))?"
    match = re.match(regex, instrucao)
    try:
        return match.group(0)
    except AttributeError:
        return 0

def main():
    instrucoes = []
    pilha = []

    with open(sys.argv[1]) as f:
        for x in f:
            instrucao = trata_instrucao(x.strip())
            if instrucao == 0:
                continue
            instrucoes.append(instrucao.split(' '))

    print(instrucoes)
    avaliar(instrucoes, pilha)

if __name__ == '__main__':
    main()