import numpy as np

def setup():
    global bord, white, black, coller, NCC
    white = 0
    black = 1
    coller = 0
    NCC = 0
    bord = np.zeros([8,8])
    bord[:,:] = np.nan
    
    bord[3,4] = white
    bord[4,3] = white
    bord[4,4] = black
    bord[3,3] = black


def put():
    
    global X_line, Y_line, coller, bord
    
    print('X軸:Y軸')
    Coordinate = str(input())
    X_line = int(Coordinate[0])
    Y_line = int(Coordinate[1])
    '''collerが0なら白'''
    bord[Y_line, X_line] = coller
    change()
    coller +=1
    if coller >1:
        coller = 0


def change():
    global NCC#not_coller_counter
    for interpose_counter in range(1,6):
        if bord[Y_line, X_line + interpose_counter] != coller and bord[Y_line, X_line + interpose_counter] != None:
            NCC =+ 1

        elif bord[Y_line, X_line + interpose_counter] == coller and NCC >=1:
            for i in range(NCC):
                bord[Y_line, X_line + interpose_counter] = coller
            NCC = 0

        elif bord[Y_line, X_line + interpose_counter] == None or bord[Y_line, X_line + interpose_counter] == coller:
            break

'''
def change():
    for right in range(1, 7):
        if X_line + right <= 7:    
            if bord[Y_line, X_line + right] == coller:
                return
            else:
                break
        else:
            break
'''

setup()
print("{}スタート".format(coller))
print(bord)
for i in range(1):
    put()
    print(bord)
    print('-----')
print('----------------')