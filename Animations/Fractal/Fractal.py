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

def init_lignes(Couche):
	nbLigne=int((((len(Couche.tabCarre))*3)/(math.sqrt(len(Couche.tabCarre)))))

	for i in range(0,nbLigne):
		tmp=[]
		Couche.Lignes.append(tmp)

	for carre in Couche.tabCarre:
		compteur = int(0)
		for elem in carre.tabVal:
			numLigne=int((Couche.tabCarre.index(carre) // math.sqrt(len(Couche.tabCarre)) * 3) + ((compteur) // ( math.sqrt(len(carre.tabVal)))))
			Couche.Lignes[numLigne].append(elem)
			compteur = compteur +1
	return Couche

def affiche_lignes(Couche):
	for ligne in Couche.Lignes:  
		for elem in ligne:
			print(elem,end=' ') 
		print()
	print()
	#affiche matrice

def init_affiche_ligne(Couche):
	init_lignes(Couche)
	affiche_lignes(Couche)

def affiche_mat(Matrice):
	for couches in Matrice.tabCouche:
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
	newMatrice.etape=oldMatrice.etape + 1
	nbCouche = int((3**(newMatrice.etape)-1)/2)
	nbCarre = int((3**((newMatrice.etape)-1))**2)
	for couches in range (0,nbCouche):
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
	for i in range(0,etape-1):
		nullMat = Matrice()
		newMat = upgrade_matrice(newMat,nullMat)

	return newMat
