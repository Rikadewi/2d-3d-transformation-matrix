import pygame
from pygame.locals import *
import math
from OpenGL.GL import *
from OpenGL.GLU import *
import transform2d
import copy
import random
from decimal import Decimal, ROUND_HALF_EVEN

#GLOBAL VARS :
radius = 0

verticies = (
	(1, -1, -1),
	(1, 1, -1),
	(-1, 1, -1),
	(-1, -1, -1),
	(1, -1, 1),
	(1, 1, 1),
	(-1, -1, 1),
	(-1, 1, 1)
	)

edges = (
	(0,1),
	(0,3),
	(0,4),
	(2,1),
	(2,3),
	(2,7),
	(6,3),
	(6,4),
	(6,7),
	(5,1),
	(5,4),
	(5,7)
	)
colors =[
	(1,0,0),
	(0,1,0),
	(0,0,1),
	(1,1,0),
	(0,1,1),
	(1,0,0),
	(0,1,0),
	(0,1,1),
	(1,0,0),
	(0,1,0),
	(0,1,1),
	(1,0,1),
	]

posisiawal = []

def sumbu2d():
	glBegin(GL_LINES)
	point = 100

	glColor3f(0,0,1)
	for i in range(-point,point):
		glVertex2f(-point,i)
		glVertex2f(point,i)

	for i in range(-point,point):
		glVertex2f(i,-point)
		glVertex2f(i,point)

	glColor3f(1,1,1)
	#SUMBU X	
	glVertex2f(-999,0)
	glVertex2f(999,0)
	
	#SUMBU Y
	glVertex2f(0,-999)
	glVertex2f(0,999)

	glEnd()


def twoD(n):
	glBegin(GL_LINE_LOOP)
	for x in range(len(posisiawal)):
		glVertex2f((posisiawal[int(x)][0]), (posisiawal[int(x)][1]))

	glEnd()
	
	glBegin(GL_LINE_LOOP)
	for i in range(n):
		x = random.choice(colors)
		glColor3fv(x)
		glVertex2fv(posisiawal[i])
	glEnd()

	glBegin(GL_POLYGON)
	for i in range(n):
		x = random.choice(colors)
		glColor3fv(x)
		glVertex2fv(posisiawal[i])
	glEnd()

def twoDinput(points,n):
	glBegin(GL_LINE_LOOP)
	for x in points:
		glVertex2f(x[0],x[1])
	glEnd()

	glBegin(GL_LINE_LOOP)
	for i in range(n):
		x = random.choice(colors)
		glColor3fv(x)
		glVertex2fv(points[i])
	glEnd()

	glBegin(GL_POLYGON)
	for i in range(n):
		x = random.choice(colors)
		glColor3fv(x)
		glVertex2fv(points[i])
	glEnd()

def drawFilledCircle(x, y, radius):
	triangleAmount = 200
	twicePi = 2.0 * math.pi;
	
	radius = float(radius)
	x = float(x)
	y = float(y)
	glBegin(GL_TRIANGLE_FAN)
	glVertex2f(x, y) 
	for i in range(triangleAmount+1): 
		glVertex2f(x + (radius * math.cos(i *  twicePi / triangleAmount)), y + (radius * math.sin(i * twicePi / triangleAmount)))
	glEnd()

def drawHollowCircle(x, y, radius):
	lineAmount = 200
	twicePi = 2.0 * math.pi;
	
	glBegin(GL_LINE_STRIP) 
	glVertex2f(x, y)  
	for i in range(lineAmount+1):
		glVertex2f(x + (radius * math.cos(i *  twicePi / lineAmount)), y + (RADIUS* math.sin(i * twicePi / lineAmount))) 
		glEnd()

def scale(arr, arrf):
	for i in range(len(arr)) :
		for j in range(2):
			
			if(round(arr[i][j],2)> round(arrf[i][j],2)):
				arr[i][j] = arr[i][j]- float(0.01)
			elif (round(arr[i][j],2) < round(arrf[i][j],2) ):
				arr[i][j] = arr[i][j]+ float(0.01)
			

def div100(s):
	f = float(s)/100
	return f

def command(arr, x, isCircle,n):
	global radius

	if (x[0] == "translate"):

		x[1] = div100(x[1])
		x[2] = div100(x[2])

		if not(isCircle):
			arrtemp = copy.deepcopy(arr)
			arrf = transform2d.finalarr(arrtemp,x)
			while( not (transform2d.locsamelow(arr,arrf))):
				if(transform2d.sumOfX(arr) > transform2d.sumOfX(arrf)):
					arr = transform2d.translate(arr, ['X',-0.1,0])
				if(transform2d.sumOfX(arr) < transform2d.sumOfX(arrf)):
					arr = transform2d.translate(arr, ['X',0.1,0])
				if(transform2d.sumOfY(arr) > transform2d.sumOfY(arrf)):
					arr = transform2d.translate(arr, ['X',0,-0.1])
				if(transform2d.sumOfY(arr) <transform2d.sumOfY(arrf)):
					arr = transform2d.translate(arr, ['X',0,0.1])
				glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
				sumbu2d()	
				twoDinput(arr,n)
				pygame.display.flip()
		
		else:
			arrtemp = copy.deepcopy(arr)
			arrf = transform2d.Ctranslate(arrtemp,x)
			
			while( not ((round(arr[0][0],2) == round(arrf[0][0],2)) and (round(arr[0][1],2) == round(arrf[0][1]),2))):
				if(round(arr[0][0],2) < round(arrf[0][0],2)):
					arr[0][0] += 0.1 
				if(round(arr[0][0],2) > round(arrf[0][0],2)):
					arr[0][0] -= 0.1 
				if(round(arr[0][1],2) < round(arrf[0][1],2)):
					arr[0][1] += 0.1 
				if(round(arr[0][1],2) > round(arrf[0][1],2)):
					arr[0][1] -= 0.1 

				glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
				sumbu2d()
				drawFilledCircle(arr[0][0], arr[0][1], radius)
				pygame.display.flip()
				pygame.time.wait(10)


	elif (x[0] == "dilate"):
		
		if not(isCircle):
			ktemp = 1.00
			while not(round(float(ktemp),2) == round(float(x[1]),2)):
				
				xtemp = ("X",ktemp)
				arrtemp = copy.deepcopy(arr)
				arrtemp = transform2d.dilate(arrtemp, xtemp)
				glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
				sumbu2d()
				
				twoDinput(arrtemp,n)
				pygame.display.flip()
				pygame.time.wait(10)

				if round(ktemp,2) < round(float(x[1]),2):
					ktemp += 0.01
				if round(ktemp,2) > round(float(x[1]),2):
					ktemp -= 0.01
			arr = copy.deepcopy(arrtemp)
		else :
			finalRad = transform2d.Cdilate(arr,x,radius)
			print(round(finalRad,2))
			while not(round(float(radius),2) == round(float(finalRad),2)) :
				if round(radius,2) < round(finalRad,2) :
					radius += 0.01
				if round(radius,2) > round(finalRad,2) :
					radius -= 0.01
				glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
				sumbu2d()
				
				drawFilledCircle(arr[0][0], arr[0][1], radius)
				pygame.display.flip()
				pygame.time.wait(10)
	
	elif (x[0] == "rotate"):
		deg = 0
		x[2] = div100(x[1])
		x[3] = div100(x[2])
		while(not(round(float(deg),3) >= abs(round(float(x[1]),3)))):
			if float(x[1]) > 0.0:
				arr = transform2d.rotate(arr,['X',0.1,x[2],x[3]])
			else:
				arr = transform2d.rotate(arr,['X',-0.1,x[2],x[3]])
			deg = round(deg + 0.1, 13)
			print(deg)
			glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
			sumbu2d()
			
			if not(isCircle):
				twoDinput(arr,n)
			else:
				drawFilledCircle(arr[0][0], arr[0][1], radius)
			pygame.display.flip()
			pygame.time.wait(1)


	elif (x[0] == "reflect"):
		
		arrf = copy.deepcopy(arr)
		arrf = transform2d.reflect(arrf,x)

		while( not (transform2d.locsamelow(arr,arrf))):
			scale(arr,arrf)
			glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
			sumbu2d()
			
			
			if not(isCircle):
				twoDinput(arr,n)
			else:
				drawFilledCircle(arr[0][0], arr[0][1], radius)

			pygame.display.flip()

	elif (x[0] == "shear"):
		arrtemp = copy.deepcopy(arr)
		arrf = transform2d.shear(arrtemp,x)

		while( not (transform2d.locsamelow(arr,arrf))):
			scale(arr,arrf)
			glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
			sumbu2d()
			
			if not(isCircle):
				twoDinput(arr,n)
			else:
				drawFilledCircle(arr[0][0], arr[0][1], radius)
			pygame.display.flip()

	elif (x[0] == "stretch"):
		arrtemp = copy.deepcopy(arr)
		arrf = transform2d.stretch(arrtemp,x)

		while( not (transform2d.locsamelow(arr,arrf))):
			scale(arr,arrf)
			glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
			sumbu2d()
			
			if not(isCircle):
				twoDinput(arr,n)
			else:
				drawFilledCircle(arr[0][0], arr[0][1], radius)
			pygame.display.flip()
	
	elif (x[0] == "custom"):
		arrtemp = copy.deepcopy(arr)
		arrf = transform2d.custom(arrtemp,x)

		while( not (transform2d.locsamelow(arr,arrf))):
			scale(arr,arrf)
			glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
			sumbu2d()
			
			if not(isCircle):
				twoDinput(arr,n)
			else:
				drawFilledCircle(arr[0][0], arr[0][1], radius)
			pygame.display.flip()
			
	else: #input tidak valid
		print("input tidak valid")

	return arr

def init():
	pygame.init()
	display = (800,600)
	pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

	gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)

	glTranslatef(0.0,0.0, -25)

	for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()

	glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
	glClearColor(0,0,0,0)



def main2d():
	global radius
	init()
	glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
	sumbu2d()
	
	pygame.display.flip()

	isCircle = False
	n = int(input("Input N  : "))
	print("Input titik :")
	for i in range(n):
		z = list(map(lambda x: float(x)/100,input().split(',')))
		posisiawal.insert(0, z)

	arr = copy.deepcopy(posisiawal)

	if (n == 1) :
		print("Inputan adalah sebuah lingkaran!")
		radius = float(input("Input radius : "))
		isCircle = True
	

	# MAKE OBJECT
	init()
	glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
	sumbu2d()
	
	if (n == 1) :
		drawFilledCircle((arr[0][0]), (arr[0][1]),radius)
	else :
		twoD(n)
	
	# Visualized OBJECT and AXIS
	pygame.display.flip()

	aksi = input(">> ")
	aksi = aksi.split()

	while (aksi[0]!="exit"):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()

		if (aksi[0] == "multiple"):
			
			n = int(input())

			while (n>0):
				aksi = input()
				aksi = aksi.split()
				arr = command(arr, aksi, isCircle,n)
				n = n - 1

		elif (aksi[0] == "reset"):
			if(not(isCircle)):
				arr = copy.deepcopy(posisiawal)
				glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
				sumbu2d()
				
				twoDinput(arr,n)
				pygame.display.flip()
				pygame.time.wait(10)
			else:
				glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
				sumbu2d()
				
				drawFilledCircle(posisiawal[0][0],posisiawal[0][1],radius)
				pygame.display.flip()
				pygame.time.wait(10)
		else:
			arr = command(arr, aksi, isCircle,n)
		
		aksi = input(">> ")
		aksi = aksi.split()

		pygame.display.flip()
		pygame.time.wait(10)
