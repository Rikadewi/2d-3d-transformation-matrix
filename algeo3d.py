import pygame
from pygame.locals import *
import transform3d
from OpenGL.GL import *
from OpenGL.GLU import *
import copy
import math
import random

verticies = [
	[1, -1, -1],
	[1, 1, -1],
	[-1, 1, -1],
	[-1, -1, -1],
	[1, -1, 1],
	[1, 1, 1],
	[-1, -1, 1],
	[-1, 1, 1]
	]

edges = [
	[0,1],
	[0,3],
	[0,4],
	[2,1],
	[2,3],
	[2,7],
	[6,3],
	[6,4],
	[6,7],
	[5,1],
	[5,4],
	[5,7]
	]

colors = (
	(1,0,0),
	(0,1,0),
	(0,0,1),
	(0,1,0),
	(1,0,0),
	(1,1,1),
	(1,0,0),
	(0,1,1),
	(0,1,0),
	(0,0,1),
	(1,0,0),
	(1,0,0),
	(0,0,1),
	(0,1,1),
	)
surfaces = [
	(4,0,3,6),
	(0,1,2,3),
	(3,2,7,6),
	(6,7,5,4),
	(4,5,1,0),
	(1,5,7,2)
	]


def sumbu3d():
	glBegin(GL_LINES)
	glColor3f(1,0,0)
	glVertex3f(-200,0,0)
	glVertex3f(200,0,0)
	glColor3f(0,1,0)
	glVertex3f(0,-200,0)
	glVertex3f(0,200,0)
	glColor3f(0,0,1)
	glVertex3f(0,0,200)
	glVertex3f(0,0,-200)
	glEnd()



def threeDinput(points):
	glBegin(GL_QUADS)
	
	for surface in surfaces:
		x=0
		for vertex in surface:
			x +=1
			glColor3fv(colors[x])
			glVertex3fv(points[vertex])
	glEnd()

	glBegin(GL_LINES)
	for tup in edges:
		for j in tup:
			glColor3fv((1,1,1))
			glVertex3f(points[j][0],points[j][1],points[j][2])
	glEnd()

	

def scale3(arr, arrf):
	for i in range(len(arr)) :
		for j in range(3):
			
			if(round(arr[i][j],2)> round(arrf[i][j],2)):
				arr[i][j] = arr[i][j]- float(0.01)
			elif (round(arr[i][j],2) < round(arrf[i][j],2) ):
				arr[i][j] = arr[i][j]+ float(0.01)
			

def div100(s):
	f = float(s)/100
	return f

def command3(arr, x):

	if (x[0] == "translate"):
		# translate <dx> <dy> <dz>
		x[1] = div100(x[1])
		x[2] = div100(x[2])
		x[3] = div100(x[3])
		
		arrf = copy.deepcopy(arr)
		arrf = transform3d.translate3(arrf,x)
		while( not (transform3d.locsamelow3(arr,arrf))):
			if(round(transform3d.sumOfX3(arr) ,2) > round(transform3d.sumOfX3(arrf),2)):
				arr = transform3d.translate3(arr, ['X',-0.1,0,0])
			if(round(transform3d.sumOfX3(arr) ,2) < round(transform3d.sumOfX3(arrf),2)):
				arr = transform3d.translate3(arr, ['X',0.1,0,0])
			if(round(transform3d.sumOfY3(arr),2) > round( transform3d.sumOfY3(arrf),2)):
				arr = transform3d.translate3(arr, ['X',0,-0.1,0])
			if(round(transform3d.sumOfY3(arr),2) <round(transform3d.sumOfY3(arrf),2)):
				arr = transform3d.translate3(arr, ['X',0,0.1,0])
			if(round(transform3d.sumOfZ3(arr),2) > round(transform3d.sumOfZ3(arrf),2)):
				arr = transform3d.translate3(arr, ['X',0,0,-0.1])
			if(round(transform3d.sumOfZ3(arr),2) < round(transform3d.sumOfZ3(arrf),2)):
				arr = transform3d.translate3(arr, ['X',0,0,0.1])
			glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
			threeDinput(arr)
			sumbu3d()
			
			pygame.display.flip()
			pygame.time.wait(10)
			
		
	elif (x[0] == "dilate"):
		# dilate <k>

		ktemp = 1.00
		while not(round(float(ktemp),2) == round(float(x[1]),2)):
			
			xtemp = ("X",ktemp)
			arrf = copy.deepcopy(arr)
			arrf = transform3d.dilate3(arrf, xtemp)
			glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
			threeDinput(arrf)
			sumbu3d()
			
			pygame.display.flip()

			if round(ktemp,2) < round(float(x[1]),2):
				ktemp += 0.01
			if round(ktemp,2) > round(float(x[1]),2):
				ktemp -= 0.01
		arr = copy.deepcopy(arrf)

	
	elif (x[0] == "rotate"):
		# rotate <param> <deg>
		# param = x, diputar terhadap sumbu x
		# param = y, diputar terhadap sumbu y
		# param = z, diputar terhadap sumbu z

		deg = 0
		while(not(round(float(deg),3) >= abs(round(float(x[2]),3)))):
			if float(x[2]) > 0.0:
				arr = transform3d.rotate3(arr,['X',x[1],0.1])
			else:
				arr = transform3d.rotate3(arr,['X',x[1],-0.1])
			deg = round(deg + 0.1, 3)
			
			glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
			threeDinput(arr)
			sumbu3d()
			
			pygame.display.flip()

	elif (x[0] == "reflect"):
		# reflect <param>
		# param = x, dicerminkan terhadap sumbu x
		# param = y, dicerminkan terhadap sumbu y
		# param = z, dicerminkan terhadap sumbu z

		arrtemp = copy.deepcopy(arr)
		arrf = transform3d.reflect3(arrtemp,x)

		while( not (transform3d.locsamelow3(arr,arrf))):
			scale3(arr,arrf)
			glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
			threeDinput(arr)
			sumbu3d()
			
			pygame.display.flip()
		#arr = transform3d.reflect3(arr, x)
		
		arr = copy.deepcopy(arrf)

	elif (x[0] == "shear"):
		# shear <param> <k>
		# param = x, shear terhadap sumbu x
		# param = y, shear terhadap sumbu y
		# param = z, shear terhadap sumbu z

		arrtemp = copy.deepcopy(arr)
		arrf = transform3d.shear3(arrtemp,x)

		while( not (transform3d.locsamelow3(arr,arrf))):
			scale3(arr,arrf)
			glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
			threeDinput(arr)
			sumbu3d()
			
			pygame.display.flip()
			
		arr = copy.deepcopy(arrf)
	
	elif (x[0] == "stretch"):
		# stretch <param> <k>
		# param = x, stretch terhadap sumbu x
		# param = y, stretch terhadap sumbu y
		# param = z, stretch terhadap sumbu z

		arrtemp = copy.deepcopy(arr)
		arrf = transform3d.stretch3(arrtemp,x)

		while( not (transform3d.locsamelow3(arr,arrf))):
			scale3(arr,arrf)
			glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
			threeDinput(arr)
			sumbu3d()
			
			pygame.display.flip()
	
	elif (x[0] == "custom"):
		# custom <a> <b> <c> <d> <e> <f> <g> <h> <i>
		arr = transform3d.custom3(arr, x)
	
	else: #input tidak valid
		print("input tidak valid")

	return arr

posisiawal = []
def main3d():
	#JGN LUPA APUS
	arr = copy.deepcopy(verticies)
	posisiawal = copy.deepcopy(verticies)
	
	pygame.init()
	display = (800,600)
	pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

	gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)

	glTranslatef(0.0,0.0, -10)

	gluLookAt(3.0, 3.0, 5.0, 0.0, 0.0, 0.0, 0.0, 5.0, 0.0)
	
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			quit()
	
	glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
	threeDinput(verticies)
	sumbu3d()
	

	pygame.display.flip()
	pygame.time.wait(10)
		
	aksi = input(">> ")
	aksi = aksi.split()

	while (aksi[0]!="exit"):
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					quit()

			if (aksi[0] == "multiple"):
				
				n = aksi[1]

				while (n>0):
					aksi = input()
					aksi = aksi.split()
					arr = command3(arr, aksi)
					n = n - 1

			elif (aksi[0] == "reset"):
				arr = copy.deepcopy(posisiawal)
				
				glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
				threeDinput(arr)
				sumbu3d()
				
				pygame.display.flip()
				pygame.time.wait(10)
			elif (aksi[0] == "cam"):
				x=0
				y=0
				z=0
				loop = True
				while loop:
					for event in pygame.event.get():
						if event.type == pygame.QUIT:
							pygame.quit()
							quit()

						elif event.type == pygame.KEYDOWN:
							if event.key == pygame.K_ESCAPE:
								pygame.quit()
								quit()

							if event.key == pygame.K_a:
								x = 0.1

							elif event.key == pygame.K_d:
								x = -0.1

							elif event.key == pygame.K_w:
								z = 0.1

							elif event.key == pygame.K_s:
								z = -0.1

							elif event.key == pygame.K_h:
								y = 0.1
							
							elif event.key == pygame.K_u:
								y = -0.1

							elif event.key == pygame.K_r:
								loop = False
								pygame.mouse.set_visible( True )

						elif event.type == pygame.KEYUP:

							if event.key == pygame.K_a and x > 0:
								x = 0

							elif event.key == pygame.K_d and x < 0:
								x = -0

							if event.key == pygame.K_w and z > 0:
								z = 0

							if event.key == pygame.K_s and z < 0:
								z = -0

							if event.key == pygame.K_h and y > 0:
								y = 0

							if event.key == pygame.K_u and y < 0:
								y = -0

							elif event.key == pygame.K_r:
								loop = True
								#pygame.mouse.set_visible( False )

					glTranslatef(x,y,z)

					glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
					threeDinput(arr)
					sumbu3d()
					
					pygame.display.flip()
					pygame.time.wait(10)

			else:
				arr = command3(arr, aksi)

			aksi = input(">> ")
			aksi = aksi.split()

			pygame.display.flip()
			pygame.time.wait(10)

