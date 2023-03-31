# Insert a value at a specific position in a list

lista = [1, 2, 3, 4, 5]

print("Lista:", lista)

valor = int(input("Digite o valor a ser inserido: "))

posicao = int(input("Digite a posição em que deseja inserir o valor: "))

lista.insert(posicao, valor)

print("Lista atualizada:", lista)