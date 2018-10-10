from __future__ import print_function

import math

class Carre:
	def __init__(self):
		self.tabVal=[]
#class Carre

class Couche:
	def __init__(self):
		self.tabCarre=[]
		self.Lignes=[]
#class Couche

class Matrice:
	def __init__(self):
		self.etape=1
		self.tabCouche=[]
#class Matrice

def init_lignes(couche):
	nbLigne=int((((len(couche.tabCarre))*3)/(math.sqrt(len(couche.tabCarre)))))

	for i in range(0,nbLigne):
		tmp=[]
		couche.Lignes.append(tmp)
	#on organise la couche en ligne

	for carre in couche.tabCarre:
		compteur = int(0)
		for elem in carre.tabVal:
			numLigne=int((couche.tabCarre.index(carre) // math.sqrt(len(couche.tabCarre)) * 3) + ((compteur) // ( math.sqrt(len(carre.tabVal)))))
			couche.Lignes[numLigne].append(elem)
			compteur = compteur +1
	#print('lignes de la couche initialisees')
	return couche

def affiche_lignes(couche):
	for ligne in couche.Lignes:  
		for elem in ligne:
			print(elem, end=' ') 
		print()
	#affiche matrice

def init_affiche_ligne(couche):
	init_lignes(couche)
	affiche_lignes(couche)

def affiche_mat(matrice):
	for couches in matrice.tabCouche:
		init_affiche_ligne(couches)

def initialize():
	basicSquare=Carre()
	basicSquare.tabVal=[0,0,0,0,1,0,0,0,0]
	basicCouche=Couche()
	basicCouche.tabCarre.append(basicSquare)
	basicMatrice=Matrice()
	basicMatrice.tabCouche.append(basicCouche)
	return basicMatrice

def upgrade_matrice(oldMatrice,newMatrice):
	#print('etape de lancienne matrice : ' , oldMatrice.etape)
	newMatrice.etape=oldMatrice.etape + 1
	#print('etape de la nouvelle matrice : ' , newMatrice.etape)
	nbCouche = int((3**(newMatrice.etape)-1)/2)
	#print('nombre de couche : ',nbCouche)
	nbCarre = int((3**((newMatrice.etape)-1))**2)
	#print('nombre de carre : ',nbCarre)
	for couches in range (0,nbCouche):
		#print('couche actuelle : ',couches)
		newMatrice.tabCouche.append(Couche())
		for carre in range (0,nbCarre):
			newMatrice.tabCouche[couches].tabCarre.append(Carre())
			if couches != nbCouche-1:
				oldCouche=int(couches // 3)
				LigneCarre = int(carre // math.sqrt(nbCarre))
				ColumnCarre = int(carre - ((math.sqrt(nbCarre) * LigneCarre)))
				oldCarre = int((LigneCarre//3)*3 + (ColumnCarre//3))
				LigneElem = int(LigneCarre%3)
				ColumnElem = int(ColumnCarre%3)
				oldElem=int(LigneElem*3 + ColumnElem)
				if int(oldMatrice.tabCouche[oldCouche].tabCarre[oldCarre].tabVal[oldElem]) == 1:
					newMatrice.tabCouche[couches].tabCarre[carre].tabVal=[1,1,1,1,1,1,1,1,1]
				else:
					newMatrice.tabCouche[couches].tabCarre[carre].tabVal=[0,0,0,0,0,0,0,0,0]
			else:
				newMatrice.tabCouche[couches].tabCarre[carre].tabVal = [0,0,0,0,0,0,0,0,0]

	for couches in range (0,nbCouche):
		for carre in range (0,nbCarre):
			if newMatrice.tabCouche[couches].tabCarre[carre].tabVal==[1,1,1,1,1,1,1,1,1] and couches%3==0:
				if newMatrice.tabCouche[(couches+3)].tabCarre[carre].tabVal != [1,1,1,1,1,1,1,1,1]:
					newMatrice.tabCouche[(couches+3)].tabCarre[carre].tabVal=[0,0,0,0,1,0,0,0,0]
				if couches == 0:
					if carre - 1 >= 0 and carre%math.sqrt(nbCarre) != 0:
						newMatrice.tabCouche[couches].tabCarre[carre-1].tabVal[4]=1
					if carre + 1 < nbCarre and carre%math.sqrt(nbCarre) != math.sqrt(nbCarre)-1:
						newMatrice.tabCouche[couches].tabCarre[carre+1].tabVal[4]=1
					#print(couches)
					#print('carre ? : ' , carre)
					#print('carre max auquel on veut acceder : ', int(carre + math.sqrt(nbCarre) - 1) )
					if carre - math.sqrt(nbCarre) >= 0 :
						newMatrice.tabCouche[couches].tabCarre[int(carre - math.sqrt(nbCarre))].tabVal[4]=1
				   	if carre + math.sqrt(nbCarre) < nbCarre:
						newMatrice.tabCouche[couches].tabCarre[int(carre + math.sqrt(nbCarre))].tabVal[4]=1
					if carre + math.sqrt(nbCarre) +1 < nbCarre and carre%math.sqrt(nbCarre) != math.sqrt(nbCarre)-1:
						newMatrice.tabCouche[couches].tabCarre[int(carre + math.sqrt(nbCarre) + 1)].tabVal[4]=1
				   	if  carre + math.sqrt(nbCarre) - 1 < nbCarre and carre%math.sqrt(nbCarre) != 0:
						newMatrice.tabCouche[couches].tabCarre[int(carre + math.sqrt(nbCarre) - 1)].tabVal[4]=1
				    	if carre - math.sqrt(nbCarre) -1 >= 0 and carre%math.sqrt(nbCarre) != 0:
						newMatrice.tabCouche[couches].tabCarre[int(carre - math.sqrt(nbCarre) - 1)].tabVal[4]=1
				    	if carre - math.sqrt(nbCarre) + 1 >=0 and carre%math.sqrt(nbCarre) != math.sqrt(nbCarre)-1:
                        			newMatrice.tabCouche[couches].tabCarre[int(carre - math.sqrt(nbCarre) + 1)].tabVal[4]=1
				if newMatrice.tabCouche[couches].tabCarre[carre].tabVal==[1,1,1,1,1,1,1,1,1] and couches%3==1:
					if carre - math.sqrt(nbCarre) >= 0:
                    				newMatrice.tabCouche[couches].tabCarre[int(carre - math.sqrt(nbCarre))].tabVal[7]=1
                			if carre + math.sqrt(nbCarre) < nbCarre:
                    				newMatrice.tabCouche[couches].tabCarre[int(carre + math.sqrt(nbCarre))].tabVal[1]=1
                			if carre - 1 >= 0 and carre%math.sqrt(nbCarre) != 0:
                    				newMatrice.tabCouche[couches].tabCarre[int(carre - 1)].tabVal[5]=1
                			if carre + 1 < nbCarre and carre%math.sqrt(nbCarre) != math.sqrt(nbCarre)-1:
                    				newMatrice.tabCouche[couches].tabCarre[int(carre + 1)].tabVal[3]=1

	return newMatrice

def CreateMat(etape):
	newMat=initialize()

	for i in range(0, etape-1):
		nullMat = Matrice()
		newMat = upgrade_matrice(newMat, nullMat)
	
	return newMat
