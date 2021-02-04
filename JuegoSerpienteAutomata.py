import time
import os
import random

matrix=[]

def matriz():
	
	for i in range(10):          
		a =[]
		for j in range(10):      
			a.append(" ")
		matrix.append(a)

def acomodo():
	for h in range(10):
		for k in range(10):
			print(matrix[h][k], end = " ")
		print( )		


matriz()
puntos=0
i=0 
j=0
cordenadax=0 
cordenaday=0

while True:
	
	
	if matrix[j][i]==matrix[cordenadax][cordenaday]:
		cordenadax=random.randint(1,9)
		cordenaday=random.randint(1,9)
		matrix[cordenadax][cordenaday]="O"
		puntos+=1

	if i<cordenaday:
		while i<=(cordenaday-1):
			i+=1		
			os.system("cls")
			print(j,i,cordenadax,cordenaday,"Puntos:  ",puntos)
			for x in range (puntos):
				acomodo()
				matrix[j][i]="►"
				matrix[j][i-1]=" "
			time.sleep(0.1)
	elif j<cordenadax:			
		while j<=(cordenadax-1):
			j+=1
			os.system("cls")
			print(j,i,cordenadax,cordenaday,"Puntos:   ",puntos)
			acomodo()
			for x in range (puntos):
				matrix[j][i]="▼"
				matrix[j-1][i]=" "
			time.sleep(0.1)

	elif i>cordenaday:
		while i>=(cordenaday+1):
			i-=1
			os.system("cls")
			print(j,i,cordenadax,cordenaday,"Puntos:   ",puntos)
			acomodo()
			matrix[j][i]="◄"
			matrix[j][i+1]=" "
			time.sleep(0.1)
	elif j>cordenadax:			
		while j>=(cordenadax+1):
			j-=1
			os.system("cls")
			print(j,i,cordenadax,cordenaday,"Puntos:   ",puntos)
			acomodo()				
			matrix[j][i]="▲"
			matrix[j+1][i]=" "
			time.sleep(0.1)
