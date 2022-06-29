#REMOVENDO EXTREMOS 

#Escreva uma função que tenha uma lista de valores e um número inteiro não negativo, n, como seus parâmetros.
#A função deve criar uma nova cópia da lista com os n maiores elementos e os n menores elementos removidos.
#Em seguida, ele deve retornar a nova cópia da lista como o único resultado da função. A ordem dos elementos na lista
#retornada não precisa coincidir com a ordem dos elementos na lista original.
#Escreva um programa principal que demonstre sua função. Sua função main deve ler uma lista
#de números do usuário e remover os dois maiores e os dois menores valores dela. Exiba a
#lista com os extremos removidos, seguido pela lista original. Seu programa deve gerar uma
#mensagem de erro apropriada se o usuário inserir menos de 4 valores.

lista= []
while True:
    num= input("Digite um número: ")
    if int(num) < 0:
        print("NÚMEROS NEGATIVOS NÃO ENTRAM PARA LISTA")
        continue
    elif num == " ":
        break
    else:
        lista.append(num)

def funçao(lista):
    max= 0
    min= 0
    if lista == 0:
        max= min= lista
    else:
        if lista < max:
            max= lista
        if lista > min:
            min= lista
    if len(lista) < 4:
        return "PRECISA DE PELO MENOS 4 VALORES"

def main():
    num = input("Digite um número: ")
    print(funçao(num))

if __name__=='__main__':
 main()
