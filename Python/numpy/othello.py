import numpy as np

white = 0
black = 1
coller = 0
counter = 0
bordsize = 8
bord = np.zeros([bordsize, bordsize])
bord[:,:] = np.nan
    
bord[3,4] = white
bord[4,3] = white
bord[4,4] = black
bord[3,3] = black



def put():
    global X_line, Y_line
    print(bord)
    while True:
        print('X軸:Y軸')
        Coordinate = str(input())
        X_line = int(Coordinate[0])
        Y_line = int(Coordinate[1])
        '''collerが0なら白'''
        if np.isnan(bord[Y_line, X_line]) == True:
            bord[Y_line, X_line] = coller
            print(bord)
            return X_line, Y_line
            break
        
        print('おけません')

def change():
    x_line, y_line = put()
    count = 0
    for i in range(1, bordsize - x_line +1):
        if bord[y_line, x_line + i] != coller and np.isnan(bord[Y_line, X_line + i]) is False: #no.isnanについてもう少し調べる(mathが代わり？)
            count =+1
        elif bord[y_line, x_line +i] == coller:
            for hoge in range(1, count +1):
                bord[y_line, x_line + hoge] == coller
        
        


print(change())