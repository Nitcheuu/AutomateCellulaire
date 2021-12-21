import pandas as pd
import numpy as np


csv = False
etat_actuel = np.array([])

def chargerCSV():
	global csv
	df = pd.read_csv("initialisation.csv")
	csv = True
	return np.array(df)


def autocell():
	global csv
	global etat_actuel
	if not csv:
		etat_actuel = chargerCSV()
	else:
		etat_actuel = etat_suivant(etat_actuel, verifier_voisins(etat_actuel))

	return etat_actuel


def verifier_voisins(etat_actuel):
	voisins = []
	for y in range(len(etat_actuel)):
		voisins_x = []
		for x in range(len(etat_actuel[y])):
			i = indices(x, y, etat_actuel)
			nb_voisins = etat_actuel[i[2]:i[3], i[0]:i[1]].sum() - etat_actuel[y, x]
			voisins_x.append(nb_voisins)
		voisins.append(voisins_x)
	return np.array(voisins)



def indices(x, y, etat_actuel):
	i = [x-1, x+2, y-1, y+2]
	if x == 0:
		i[0] = x
	if x == len(etat_actuel[y]):
		i[1] = x + 1
	if y == 0:
		i[2] = y
	if y == len(etat_actuel):
		i[3] = y + 1
	return i


def etat_suivant(etat_actuel, voisins):
	suivant = []
	suivant_x = []
	for y in range(len(etat_actuel)):
		suivant_x = []
		for x in range(len(etat_actuel[y])):
			if etat_actuel[y, x] == 1:
				if voisins[y, x] == 2:
					suivant_x.append(1)
				else:
					suivant_x.append(0)
			else:
				if voisins[y, x] == 3:
					suivant_x.append(1)
				else:
					suivant_x.append(0)
		suivant.append(suivant_x)
	return np.array(suivant)
