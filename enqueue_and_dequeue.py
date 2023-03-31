# A basic queue has the following operations:

# Enqueue: add a new element to the end of the queue.
# Dequeue: remove the element from the front of the queue and return it.
# In this challenge, you must first implement a queue. Then process q queries, where each query is one of the following 3 types:

# 1: Enqueue element  into the end of the queue.
# 2: Dequeue the element at the front of the queue.
# 3: Print the element at the front of the queue.

fila = []

while True:
    resposta = input("Deseja enfileirar um valor? (S/N) ").lower()

    if resposta == "s":
        valor = input("Digite o valor a ser enfileirado: ")
        fila.append(valor)
        print("Fila atual: ", fila)
    elif resposta == "n":
        resposta = input("Deseja desenfileirar um valor? (S/N) ").lower()

        if resposta == "s":
            elemento = fila.pop(0)
            print("Elemento removido: ", elemento)
            print("Fila atual: ", fila)
        elif resposta == "n":
            print("Programa finalizado.")
            break
        else:
            print("Opção inválida. Tente novamente.")
    else:
        print("Opção inválida. Tente novamente.")