# Objective: Given a number, find out whether its colorful or not.

# Colorful Number: When in a given number, product of every digit of a sub-sequence are different. 
# That number is called Colorful Number. See Example

# Example:

# Given Number : 3245
# Output : Colorful

# Number 3245 can be broken into parts like 3 2 4 5 32 24 45 324 245.
# this number is a colorful number, since product of every digit of a sub-sequence are different.
# That is, 3 2 4 5 (3*2)=6 (2*4)=8 (4*5)=20, (3*2*4)= 24 (2*4*5)= 40

# Given Number : 326
# Output : Not Colorful.

# 326 is not a colorful number as it generates 3 2 6 (3*2)=6 (2*6)=12.

numero = int(input("Digite um número: "))
numero_str = str(numero)
digitos = [int(d) for d in numero_str]
produtos = []
colorido = True

for i in range(len(digitos)):
    for j in range(i + 1, len(digitos) + 1):
        subsequencia = digitos[i:j]
        produto = 1
        for digito in subsequencia:
            produto *= digito
        if produto in produtos:
            colorido = False
            break
        produtos.append(produto)
    if not colorido:
        break

if colorido:
    print(f"{numero} é um número colorido")
else:
    print(f"{numero} não é um número colorido")