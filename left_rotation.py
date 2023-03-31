# A left rotation operation on an array shifts each of the array's elements 1 unit to the left. 
# For example, if 2 left rotations are performed on array [1,2,3,4,5], then the array would become [3,4,5,1,2]. 
arr = [1, 2, 3, 4, 5]

print(arr)

num_rotacoes = 2

for i in range(num_rotacoes):
    primeiro_elemento = arr.pop(0)
    arr.append(primeiro_elemento)

print(arr)