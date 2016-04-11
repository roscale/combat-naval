#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Rosca Alex 4TB
# cnaval.py – 22.03.16

largeur, longueur = 10, 10

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

tailleNavires = { 	"porte-avion"	:5,
					"croiseur"		:4,
					"destroyer" 	:3,
					"sous-marin"	:2 }

def creation_grille(largeur, longueur):
	grille = [["." for y in range(longueur)] for x in range(largeur)]
	return grille


def affiche_grille(grille, largeur, longueur, placements=None):
	print("\n   A B C D E F G H I J")
	for i in range(largeur):
		print(" {} ".format(i), end="")

		### Affichage matrice ###
		for j in range (longueur):
			if placements is None:
				print(".", end=" ")
			else:
				print(grille[i][j], end=" ")
		print()


def placement_bateau(largeur, longueur, bateau, position, orientation, taille):
	verifBool = verif_orientation(largeur, longueur, bateau, position, orientation, taille)
	if not verifBool:
		print("\nPosition invalide\n")
		return None

	verifBool = verif_collisions(bateau, position, orientation, taille)
	if not verifBool:
		print("\nCollision\n")
		return None

	####### Placement #######
	posLong = lettre2nombre[position[0]]
	posLarg = int(position[1])

	if orientation == "H":
		for L in range(posLong, posLong + taille):
			grille[posLarg][L] = "x"

	elif orientation == "V":
		for l in range(posLarg, posLarg + taille):
			grille[l][posLong] = "x"


def verif_orientation(largeur, longueur, bateau, position, orientation, taille):
	posLong = lettre2nombre[position[0]]
	posLarg = int(position[1])

	### Vérification du bord + coordonés de fin(dans la matrice) ###
	if orientation == "H":
		if (posLong + taille > longueur) or (posLarg == 0 or posLarg == largeur - 1):
			return False

	elif orientation == "V":
		if (posLarg + taille > largeur) or (posLong == 0 or posLong == longueur - 1):
			return False

	return True


def verif_collisions(bateau, position, orientation, taille):
	posLong = lettre2nombre[position[0]]
	posLarg = int(position[1])

	if orientation == "H":
		for L in range(posLong, posLong + taille):
			try:
				if grille[posLarg - 1][L - 1] == "x" or grille[posLarg + 1][L - 1] == "x" or grille[posLarg - 1][L + 1] == "x" or grille[posLarg + 1][L + 1] == "x":
					return False
			except:
				pass

	elif orientation == "V":
		for l in range(posLarg, posLarg + taille):
			try:
				if grille[l - 1][posLong - 1] == "x" or grille[l + 1][posLong - 1] == "x" or grille[l - 1][posLong + 1] == "x" or grille[l + 1][posLong + 1] == "x":
					return False
			except:
				pass

	return True


grille = creation_grille(largeur, longueur)
affiche_grille(grille, largeur, longueur)

while True:
	bateau = input("\nQuel navire voulez-vous placer [porte-avion / croiseur / destroyer / sous-marin]: ")
	if bateau == "0":
		break

	position = input("\tOù placez-vous votre {} [XY]: ".format(bateau))
	orientation = input("\tQuelle orientation pour votre {} [H/V]: ".format(bateau))
	taille = tailleNavires[bateau]

	placement_bateau(largeur, longueur, bateau, position, orientation, taille)
	affiche_grille(grille, largeur, longueur, "bateaux")
