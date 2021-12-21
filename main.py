import pygame as pg
from automate import autocell
pg.init()


on = True
menu = True
initialise = False
evennements = {}
fenetre_jeu = None
delai = 1


def affichage(etat_actuel, taille_cel):
	global fenetre_jeu
	x = 0
	y = 0
	for ligne in etat_actuel:
		for cel in ligne:
			rectangle = pg.Rect(x, y, taille_cel, taille_cel)
			if cel == 0:
				pg.draw.rect(fenetre_jeu, (255, 255, 255), rectangle)
			else:
				pg.draw.rect(fenetre_jeu, (0, 0, 0), rectangle)
			x += taille_cel
		y += taille_cel
		x = 0
	pg.display.flip()


def touches():
	global evennements
	liste_touches = []
	for evennement in evennements:
		if evennement.type == pg.KEYDOWN:
			liste_touches.append(evennement.key)
	return liste_touches


def quitter():
	global on
	global evennements
	for event in evennements: # détection des events
		if event.type == pg.QUIT: # quand on appuie sur la croix
			on = False
			pg.quit()


def fenetre(largeur, hauteur):
	global initialise
	global fenetre_jeu
	if not initialise:
		fenetre_jeu = pg.display.set_mode((largeur, hauteur))
		pg.display.set_caption('AutoCell')
		initialise = True
	quitter()


def interface(largeur=1280, hauteur=720):
	global delai
	fenetre(largeur, hauteur)
	actions = touches()
	if pg.K_RIGHT in actions:
		if delai > 0.5:
			delai -= 0.1
	if pg.K_LEFT in actions:
		delai += 0.1



temps = 0
while on:
	interface()
	if pg.time.get_ticks() / 1000 > temps:
		temps += delai
		automate = autocell()
	try:
		evennements = pg.event.get()
	except:
		pass
	affichage(automate, 15)