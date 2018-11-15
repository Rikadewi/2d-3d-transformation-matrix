import math
import copy



def sumOfX3(l1):
	#print(sum(i for i, _ in l1))
	return sum(i for i, _,_ in l1)

def sumOfY3(l1):
	return sum(n for _, n,_ in l1)

def sumOfZ3(l1):
	return sum(n for _, _, n in l1)


def locsamelow3(l1,l2):
	i = 0
	flag = True
	while (i < len(l1) and flag):
		j = 0
		while(j <= 2 and flag):
			flag = round(l1[i][j],2) == round(l2[i][j],2)
			print(round(l1[i][j],2), ' compare : ',round(l2[i][j],2) )
			j +=1
		i += 1
	return flag

def kalimatriks3(matriks, point):
	#perkalian matriks 3x3 dengan matriks point 3x1
	x = matriks[0][0]*point[0] + matriks[0][1]*point[1] + matriks[0][2]*point[2]
	y = matriks[1][0]*point[0] + matriks[1][1]*point[1] + matriks[1][2]*point[2]
	z = matriks[2][0]*point[0] + matriks[2][1]*point[1] + matriks[2][2]*point[2]
	return [x,y,z]

def translate3(arr, x):
	
	dx = float(x[1])
	dy = float(x[2])
	dz = float(x[3])

	for point in arr:
		point[0] += dx
		point[1] += dy
		point[2] += dz

	return arr

def dilate3(arr, x):
	
	k = float(x[1])
	matriks = [[k, 0, 0],[0, k, 0],[0, 0, k]]
	i = 0
	for point in arr:
		arr[i] = kalimatriks3(matriks, point)
		i += 1
	return arr

def rotate3(arr, x):
	
	param = x[1]
	deg = float(x[2])
	
	if(param == "x"):
		matriks = [[1, 0, 0],[0, math.cos(math.radians(deg)), -math.sin(math.radians(deg))],[0, math.sin(math.radians(deg)), math.cos(math.radians(deg))]]

	elif(param == "y"):
		matriks = [[math.cos(math.radians(deg)), 0, math.sin(math.radians(deg))],[0, 1, 0],[-math.sin(math.radians(deg)), 0, math.cos(math.radians(deg))]]

	else: #param = z
		matriks = [[math.cos(math.radians(deg)), -math.sin(math.radians(deg)), 0],[math.sin(math.radians(deg)), math.cos(math.radians(deg)), 0],[0, 0, 1]]
	 
	i = 0
	for point in arr:
		arr[i] = kalimatriks3(matriks, point)
		i += 1
	
	return arr

def reflect3(arr, x):
	
	param = x[1]

	if(param == "x"):
		matriks = [[1, 0, 0],[0, -1, 0],[0, 0, -1]]

	elif(param == "y"):
		matriks = [[-1, 0, 0],[0, 1, 0],[0, 0, -1]]
	
	else: #param = "z"
		matriks = [[-1, 0, 0],[0, -1, 0],[0, 0, 1]]

	i = 0
	for point in arr:
		arr[i] = kalimatriks3(matriks, point)
		i += 1
	
	return arr

def shear3(arr, x):
	
	param = x[1]
	k = float(x[2])
	
	if(param == "x"):
		matriks = [[1, k, k],[0, 1, 0],[0, 0, 1]]

	elif(param == "y"):
		matriks = [[1, 0, 0],[k, 1, k],[0, 0, 1]]
	
	else: #param = "z"
		matriks = [[1, 0, 0],[0, 1, 0],[k, k, 1]]

	i = 0
	for point in arr:
		arr[i] = kalimatriks3(matriks, point)
		i += 1

	return arr

def stretch3(arr, x):
	
	param = x[1]
	k = float(x[2])

	if (param == "x"):
		matriks = [[k, 0, 0],[0, 1, 0],[0, 0, 1]]
	elif (param == "y"):
		matriks = [[1, 0, 0],[0, k, 0],[0, 0, 1]]
	else: #param = z
		matriks = [[1, 0, 0],[0, 1, 0],[0, 0, k]]

	i = 0
	for point in arr:
		arr[i] = kalimatriks3(matriks, point)
		i += 1

	return arr

def custom3(arr, x):
	
	a = float(x[1])
	b = float(x[2])
	c = float(x[3])
	d = float(x[4])
	e = float(x[5])
	f = float(x[6])
	g = float(x[7])
	h = float(x[8])
	i = float(x[9])

	matriks = [[a, b, c],[d, e, f], [g, h ,i]]

	i = 0
	for point in arr:
		arr[i] = kalimatriks3(matriks, point)
		i += 1
	
	return arr


'''
def command3(arr, x):

	if (x[0] == "translate"):
		# translate <dx> <dy> <dz>
		x[1] = div100(x[1])
		x[2] = div100(x[2])
		x[3] = div100(x[3])
		print(x[1])
		print(x[2])
		print(x[3])
		#arr = translate3(arr, x)

	elif (x[0] == "dilate"):
		# dilate <k>
		arr = dilate3(arr, x)
	
	elif (x[0] == "rotate"):
		# rotate <param> <deg>
		# param = x, diputar terhadap sumbu x
		# param = y, diputar terhadap sumbu y
		# param = z, diputar terhadap sumbu z
		arr = rotate3(arr, x)

	elif (x[0] == "reflect"):
		# reflect <param>
		# param = x, dicerminkan terhadap sumbu x
		# param = y, dicerminkan terhadap sumbu y
		# param = z, dicerminkan terhadap sumbu z
		arr = reflect3(arr, x)

	elif (x[0] == "shear"):
		# shear <param> <k>
		# param = x, shear terhadap sumbu x
		# param = y, shear terhadap sumbu y
		# param = z, shear terhadap sumbu z
		arr = shear3(arr, x)
	
	elif (x[0] == "stretch"):
		# stretch <param> <k>
		# param = x, stretch terhadap sumbu x
		# param = y, stretch terhadap sumbu y
		# param = z, stretch terhadap sumbu z
		arr = stretch3(arr, x)
	
	elif (x[0] == "custom"):
		# custom <a> <b> <c> <d> <e> <f> <g> <h> <i>
		arr = custom3(arr, x)
	
	else: #input tidak valid
		print("input tidak valid")

	return arr
'''