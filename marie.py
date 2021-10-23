import numpy as np

def get_transformasjonsmatrise(): #en funksjon som lager transformasjonsmatrisen
   #t = 0
   # T = [np.cos(t), np.cos(t), np.sin(t), np.cos(t) ]"
    matrix = []
    row=[]
    for i in range(6):
        a=[]
        for j in range(6):
            a.append('i')
        matrix.append(a)

    for j in range(6):
        for k in range(6):
            print(matrix[j][k], end = ' ')
        print()

get_transformasjonsmatrise()

