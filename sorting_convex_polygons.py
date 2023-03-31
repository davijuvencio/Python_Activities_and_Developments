# Develop a function whose objective is to order the vertices of a convex polygon. 
# The input of this function will be a list, containing the vertices (x,y) of the polygon. 
# The output should be the same list sorted clockwise or counterclockwise.

import numpy as np

poligono = [[0,0],[0,1],[1,0],[1,1]]


def vertices(lista):
    axang = []
    for i in range(len(poligono)):
        axang.append(np.arctan2(np.mean(poligono,axis=0)[1]-poligono[i][1],np.mean(poligono,axis=0)[0]-poligono[i][0]))
    ax = np.argsort(axang)
          
    return np.array(lista)[ax]

print(vertices(poligono))