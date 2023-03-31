import random

class No:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None

def inserir_no(raiz, no):
    if raiz is None:
        return no
    if no.valor < raiz.valor:
        raiz.esquerda = inserir_no(raiz.esquerda, no)
    else:
        raiz.direita = inserir_no(raiz.direita, no)
    return raiz

def criar_arvore(profundidade, quantidade):
    raiz = None
    for i in range(quantidade):
        valor = random.randint(1, 100)
        no = No(valor)
        if raiz is None:
            raiz = no
        else:
            raiz = inserir_no(raiz, no)
    return raiz

def imprimir_em_ordem(raiz):
    if raiz is not None:
        imprimir_em_ordem(raiz.esquerda)
        print(raiz.valor, end=" ")
        imprimir_em_ordem(raiz.direita)

profundidade = int(input("Digite a profundidade da árvore: "))
quantidade = int(input("Digite a quantidade de elementos da árvore: "))
valor = int(input("Digite o valor a ser inserido na árvore: "))

arvore = criar_arvore(profundidade, quantidade)

no = No(valor)
inserir_no(arvore, no)

print("Árvore em ordem:")
imprimir_em_ordem(arvore)