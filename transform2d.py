import math
import copy
from decimal import Decimal, ROUND_HALF_EVEN

def findPivot(arr, axis):
    if axis == 'x':
        min = arr[0][0]
    else: # axis is y
        min = arr[0][1]

    for i in arr :
        if axis == 'x':
            if i[1] < min :
                min = i[0]
        if axis == 'y':
            if i[0] < min :
                min = i[0]

    return float(min)
        
def kalimatriks(matriks, point):
    #perkalian matriks 2x2 dengan matriks point 1x2
    x = matriks[0][0]*point[0] + matriks[0][1]*point[1]
    y = matriks[1][0]*point[0] + matriks[1][1]*point[1] 
    return [x,y]


def translate(arr, x):
    
    dx = float(x[1])/100
    dy = float(x[2])/100

    for point in arr:
        point[0] = point[0] + dx
        point[1] = point[1] + dy

    return arr

def Ctranslate(arr, x):
    
    dx = float(x[1])
    dy = float(x[2])

    arr[0][0] =  arr[0][0] + dx
    arr[0][1] =  arr[0][1] + dy

    return arr

def dilate(arr, x):
    
    k = float(x[1])
    matriks = [[k, 0],[0, k]]
    i = 0
    for point in arr:
        arr[i] = kalimatriks(matriks, point)
        i += 1
    return arr

def Cdilate(arr, x,radius):
    radius *= float(x[1])
    return radius

def rotate(arr, x):
    
    deg = float(x[1])
    a = -1*float(x[2])
    b = -1*float(x[3])
    
    arr = translate(arr, ['X',a,b])

    matriks = [[float(math.cos(math.radians(deg))), float(-math.sin(math.radians(deg)))],[float(math.sin(math.radians(deg))),float(math.cos(math.radians(deg)))]]
    print(matriks)

    i = 0
    for point in arr:
        arr[i] = kalimatriks(matriks, point)
        i += 1

    a = -1*a;
    b = -1*b;

    arr = translate(arr, ['X',a,b])
    print(arr)
    return arr

def reflect(arr, x):
    
    param = x[1]

    if(param == "x"):
        matriks = [[1, 0],[0, -1]]

        i = 0
        for point in arr:
            arr[i] = kalimatriks(matriks, point)
            i += 1

    elif(param == "y"):
        matriks = [[-1, 0],[0, 1]]

        i = 0
        for point in arr:
            arr[i] = kalimatriks(matriks, point)
            i += 1
     
    elif(param == "y=x"):
        matriks = [[0, 1],[1, 0]]

        i = 0
        for point in arr:
            arr[i] = kalimatriks(matriks, point)
            i += 1
     
    elif(param == "y=-x"):
        matriks = [[0, -1],[-1, 0]]

        i = 0
        for point in arr:
            arr[i] = kalimatriks(matriks, point)
            i += 1

    else: #param = (a,b)
        param = param.split(',')

        a = param[0].split('(')
        aa = -1*float(a[1])/100

        b = param[1].split(')')
        bb = -1*float(b[0])/100

        arr = translate(arr, ['X',aa,bb])

        matriks = [[-1, 0],[0, -1]]

        i = 0
        for point in arr:
            arr[i] = kalimatriks(matriks, point)
            i += 1

        aa = -1*aa;
        bb = -1*bb;

        arr = translate(arr, ['X',aa,bb])

    return arr

def Creflect(arr, x):
    
    param = x[1]

    if(param == "x"):
        matriks = [[1, 0],[0, -1]]

        i = 0
        for point in arr:
            arr[i] = kalimatriks(matriks, point)
            i += 1

    elif(param == "y"):
        matriks = [[-1, 0],[0, 1]]

        i = 0
        for point in arr:
            arr[i] = kalimatriks(matriks, point)
            i += 1
     
    elif(param == "y=x"):
        matriks = [[0, 1],[1, 0]]

        i = 0
        for point in arr:
            arr[i] = kalimatriks(matriks, point)
            i += 1
     
    elif(param == "y=-x"):
        matriks = [[0, -1],[-1, 0]]

        i = 0
        for point in arr:
            arr[i] = kalimatriks(matriks, point)
            i += 1

    else: #param = (a,b)
        param = param.split(',')

        a = param[0].split('(')
        aa = -1*float(a[1])

        b = param[1].split(')')
        bb = -1*float(b[0])

        arr = translate(arr, ['X',aa,bb])

        matriks = [[-1, 0],[0, -1]]

        i = 0
        for point in arr:
            arr[i] = kalimatriks(matriks, point)
            i += 1

        aa = -1*aa;
        bb = -1*bb;

        arr = translate(arr, ['X',aa,bb])

    return arr

def shear(arr, x):
    
    param = x[1]
    k = float(x[2])
    
    if (param == "x"):
        matriks = [[1, k],[0, 1]]
    else: #param = y
        matriks = [[1, 0],[k, 1]]

    i = 0
    for point in arr:
        arr[i] = kalimatriks(matriks, point)
        i += 1

    return arr

def stretch(arr, x):
    
    param = x[1]
    k = float(x[2])

    if (param == "x"):
        matriks = [[k, 0],[0, 1]]
    else: #param = y
        matriks = [[1, 0],[0, k]]

    i = 0
    for point in arr:
        arr[i] = kalimatriks(matriks, point)
        i += 1

    return arr

def custom(arr, x):
    
    a = float(x[1])
    b = float(x[2])
    c = float(x[3])
    d = float(x[4])

    matriks = [[a, b],[c, d]]

    i = 0
    for point in arr:
        arr[i] = kalimatriks(matriks, point)
        i += 1
    
    return arr

# neW PACKAGE
def finalarr(l1,x):
    for i in l1:
        i[0] = round(i[0]+float(x[1]) ,13)
        i[1] = round(i[1]+float(x[2]) , 13)
    return l1

def locsame(l1,l2):
    i = 0
    flag = True
    while (i < len(l1) and flag):
        j = 0
        while(j <= 1 and flag):
            flag = round(l1[i][j],13) == round(l2[i][j],13)
            j +=1
        i += 1
    return flag

def locsamelow(l1,l2):
    i = 0
    flag = True
    while (i < len(l1) and flag):
        j = 0
        while(j <= 1 and flag):
            flag = round(l1[i][j],2) == round(l2[i][j],2)
            j +=1
        i += 1
    return flag

def sumOfX(l1):
    return sum(i for i, _ in l1)

def sumOfY(l1):
    return sum(n for _, n in l1)





