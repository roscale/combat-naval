#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Rosca Alex 4TB
# cnaval.py – 22.03.16

class Grille():
	lettre2nombre = { 	"A": 0,
						"B": 1,
						"C": 2,
						"D": 3,
						"E": 4,
						"F": 5,
						"G": 6,
						"H": 7,
						"I": 8,
						"J": 9 }

	def __init__(self, largeur, longueur):
		self.largeur = largeur
		self.longueur = longueur
		self.matrice = [["." for y in range(longueur)] for x in range(largeur)]

	def affiche(self):
		print("\n   A B C D E F G H I J")
		for i in range(self.largeur):
			print(" {} ".format(i), end="")

			for j in range(self.longueur):
				print(self.matrice[i][j], end=" ")
			print()



class Bateau():
	tailleNavires = { 	"porte-avion"	:5,
						"croiseur"		:4,
						"destroyer" 	:3,
						"sous-marin"	:2	}

	def __init__(self, typeBateau, position, orientation, taille):

		self.typeBateau = typeBateau
		self.posLarg = int(position[1])
		self.posLong = Grille.lettre2nombre[position[0]]
		self.orientation = orientation
		self.taille = taille

		####### Vérifications #######
		verifBool = self.verif_orientation()
		if verifBool is False:
			print("\nPosition invalide\n")
			return None

		verifBool = self.verif_collisions()
		if verifBool is False:
			print("\nCollision\n")
			return None

		####### Placement #######
		if self.orientation == "H":
			for L in range(self.posLong, self.posLong + self.taille):
				grille.matrice[self.posLarg][L] = "x"

		elif self.orientation == "V":
			for l in range(self.posLarg, self.posLarg + self.taille):
				grille.matrice[l][self.posLong] = "x"


	def verif_orientation(self):
		self.posLarg = int(position[1])
		self.posLong = Grille.lettre2nombre[position[0]]

		### Vérification du bord + coordonés de fin(pour qu'il soit dans la matrice) ###
		if self.orientation == "H":
			if (self.posLong + self.taille > grille.longueur) or (self.posLarg == 0 or self.posLarg == grille.largeur - 1):
				return False

		elif self.orientation == "V":
			if (self.posLarg + self.taille > grille.largeur) or (self.posLong == 0 or self.posLong == grille.longueur - 1):
				return False

		return True


	def verif_collisions(self):
		self.posLarg = int(position[1])
		self.posLong = Grille.lettre2nombre[position[0]]

		if self.orientation == "H":
			### Extrémités
			try:
				if grille.matrice[self.posLarg][self.posLong - 1] == "x" or grille.matrice[self.posLarg][self.posLong + self.taille] == "x":
					return False
			except:
				pass

			### Côtés
			for L in range(self.posLong, self.posLong + self.taille):
				if grille.matrice[self.posLarg + 1][L] == "x" or grille.matrice[self.posLarg - 1][L] == "x":
					return False

		elif self.orientation == "V":
			### Extrémités
			try:
				if grille.matrice[self.posLarg - 1][self.posLong] == "x" or grille.matrice[self.posLarg + self.taille][self.posLong] == "x":
					return False
			except:
				pass

			### Côtés
			for l in range(self.posLarg, self.posLarg + self.taille):
				if grille.matrice[l][self.posLong - 1] == "x" or grille.matrice[l][self.posLong + 1] == "x":
					return False

		return True



largeur, longueur = 10, 10

grille = Grille(largeur, longueur)
grille.affiche()

while True:
	typeBateau = ""
	while typeBateau not in Bateau.tailleNavires:
		typeBateau = input("\nQuel navire voulez-vous placer [porte-avion / croiseur / destroyer / sous-marin]: ")
		if typeBateau == "exit":
			exit()

	position = input("\tOù placez-vous votre {} [XY]: ".format(typeBateau)).upper()
	orientation = input("\tQuelle orientation pour votre {} [H/V]: ".format(typeBateau)).upper()
	taille = Bateau.tailleNavires[typeBateau]
	bateau = Bateau(typeBateau, position, orientation, taille)

	grille.affiche()
