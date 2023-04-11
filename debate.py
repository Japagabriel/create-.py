import os
import random



def tela():
    os.system('clear')
    print("=======================================")
    print("==== M E N U   P R I N C I P A L ======")
    print("======================================= \n")
    print("\t 1 - Aleatorio quem comeca")
    print("\t 2 - Aleatorio Temas")
    print("\t 0 - Fechar o programa")
    print("======================================= \n")

    op = input("Informe qual a funcao: " )
    return op



def Alcomeca():
    strings = ["1", "2"]
    sorteado = random.choice(strings)
    if sorteado == "1":
        return "CHAPA 01"
    elif sorteado == "2":
        return "CHAPA 02"

def sortRemove(lista_strings):
    if not lista_strings:
        mensagem = "A lista de temas está vazia."
        return mensagem, lista_strings

    sorteado = random.choice(lista_strings)
    lista_strings.remove(sorteado)

    if sorteado == lista_strings[0]:
        mensagem = f"O tema sorteado foi: '{sorteado}' " #foi sorteada e é igual à primeira string restante da lista.
    elif sorteado == lista_strings[-1]:
        mensagem = f"O tema sorteado foi: '{sorteado}' " #foi sorteada e é igual à última string restante da lista.
    else:
        mensagem = f"O tema sorteado foi: '{sorteado}' " #foi sorteada e não é igual à primeira nem à última string restante da lista.

    return mensagem, lista_strings

dadosTemas = ["ORÇAMENTO","ASSISTÊNCIA AO ALUNO","INFRAESTRUTURA","PÓS-GRADUAÇÃO","PGD"]
op = tela()
while op != "0":
    if op == "1":
        a = Alcomeca()
        print(a)
        input("\n Tecle ENTER para continuar")
        op = tela()             
    elif op == "2":
        mensagem, dadosTemas = sortRemove(dadosTemas)
        
        print(mensagem)
        print("\n")
        print(dadosTemas)
        input("\n Tecle ENTER para continuar")
        op = tela()

    else:
        print("===   Opcao Invalida   ===")
        input("\n Tecle ENTER para continuar")
        op = tela()
print("Fim.")