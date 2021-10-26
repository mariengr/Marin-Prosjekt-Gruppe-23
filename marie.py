import numpy as np

from main import get_knutepunkt

def get_theta(filename):
    knutepunkter = get_knutepunkt(filename)
    for i in knutepunkter:
        




def get_transformasjonsmatrise(): #en funksjon som lager transformasjonsmatrisen
   #t = 0
   # T = [np.cos(t), np.cos(t), np.sin(t), np.cos(t) ]
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

t = 2

T = np.array( [ [ np.cos(t), -np.sin(t), 0. ,0., 0., 0.] , 
[ np.sin(t), np.cos(t), 0., 0., 0., 0.] ,
[0., 0., 1, 0., 0., 0.] , 
[0., 0., 0., np.cos(t), -np.sin(t), 0.], 
[0., 0., 0., np.sin(t), np.cos(t), 0.], 
[0., 0., 0., 0., 0., 1] ])
