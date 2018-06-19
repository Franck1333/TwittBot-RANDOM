#!/usr/bin/env python
# -*- coding: cp1252 -*-

import time
import os
import sys
import datetime

#Bliblioth�que Twython (Twitter/Python)
from twython import Twython

#Bliblioth�que RANDOM pour l'utilisation de l'al�atoire
import random

#Bliblioth�que du Projet
from temps_sys import temps

#IDENTIFIANTS DE CONNEXION a l'API Twitter -- DEBUT -- 
CONSUMER_KEY = '***'     #Changer ces identifiants par les v�tres
CONSUMER_SECRET = '***'  #Changer ces identifiants par les v�tres
ACCESS_KEY = '***'       #Changer ces identifiants par les v�tres
ACCESS_SECRET = '***'    #Changer ces identifiants par les v�tres
print("Identification en cours...")
twitter = Twython(CONSUMER_KEY,CONSUMER_SECRET,ACCESS_KEY,ACCESS_SECRET)
#IDENTIFIANTS DE CONNEXION a l'API Twitter -- FIN --

def publication ():
    #Publication du Message sur Twitter -- DEBUT --

    #MESSAGE TEXTUEL --DEBUT --

    #G�n�ration al�atoire d'une Phrase en Anglais --DEBUT--
    nouns = ["puppy", "car", "rabbit", "girl", "monkey","OtonaJP","A dude", "My mom", "The king", "Some guy", "A cat with rabies", "A sloth", "Your homie", "This cool guy my gardener met yesterday", "Superman","These dudes", "Both of my moms", "All the kings of the world", "Some guys", "All of a cattery's cats", "The multitude of sloths living under your bed", "Your homies", "Like, these, like, all these people", "Supermen"]                            #Liste de Noms utilisables
    verbs = ["runs", "hits", "jumps", "drives", "barfs","eats", "kicks", "gives", "treats", "meets with", "creates", "hacks", "configures", "spies on", "retards", "meows on", "flees from", "tries to automate", "explodes"]                                                                                                                                                                                                                                           #Liste de Verbes utilisable
    adv = ["crazily", "dutifully", "foolishly", "merrily", "occasionally","eventually","exactly","faithfully","finally","fortunately","frequently","gleefully","gracefully","happily","hastily","honestly","hopelessly","hourly","hungrily","innocently","inquisitively","irritably","jealously"]                                                                                                                                                                       #Liste d'adverbes utilisables 
    adj = ["adorable", "clueless", "dirty", "odd", "stupid","quizzical","highfalutin","dynamic","wakeful","cheerful","thoughtful","cooperative","questionable","abundantuneven","yummy","juicy"]                                                                                                                                                                                                                                                                        #Liste d'adjectifs utilisables

    random.shuffle(nouns)       #M�lange des �l�ments qui sont dans la liste des Noms
    random.shuffle(verbs)       #M�lange des �l�ments qui sont dans la liste des Verbes
    random.shuffle(adv)         #M�lange des �l�ments qui sont dans la liste des Adverbes
    random.shuffle(adj)         #M�lange des �l�ments qui sont dans la liste des Adjectifs

    num = random.randrange(0,13)                                                     #M�thode permettant la g�n�ration de la phrase al�atoirement et la stock dans une variable 'num'
    phrase = nouns[num] + ' ' + verbs[num] + ' ' + adv[num] + ' ' + adj[num]
    print (nouns[num] + ' ' + verbs[num] + ' ' + adv[num] + ' ' + adj[num])         #Affichage de la Phrase g�n�rer al�atoirement
    print("Legende generer aleatoirement :",phrase)
    #G�n�ration al�atoire d'une Phrase en Anglais --FIN--

    Message = phrase            #Variable contenant le Message � publi�
    print("Prise en compte du Message Textuel a Publie")
    #MESSAGE TEXTUEL --FIN --

    #PHOTO --DEBUT--

    #CHOIX DU FICHIER --DEBUT--
    randompic = random.choice(os.listdir("/home/pi/TwittBot-RANDOM/MyWork/images/"))    #Choix d'une Image parmis celles pr�sente dans le Repertoire indiqu�
    file = '/home/pi/TwittBot-RANDOM/MyWork/images/' + randompic                        #Enregistrement du Chemin et du fichier choisi dans une variable 'file'
    photo = open(file, 'rb')                                                            #Ouverture du fichier choisi
    print("Fichier RANDOM choisi se trouvant � cet endroit:", file)                   #Affichage du Chemin + Fichier choisi dans la console
    #CHOIX DU FICHIER --FIN--
    print("Chargement de la Photo en cours...")
    response = twitter.upload_media(media=photo)
    print("Prise en compte de la Photo a Publie")
    #PHOTO --FIN--

    #Etape de Publication du Contenu
    twitter.update_status(status=Message,media_ids=[response['media_id']])   #M�thode utilisant la variable "Message" permettant de le Publier + le fichier choisi al�atoirement

    print("Le Message a ete envoye avec succes")
    #Publication du Message sur Twitter -- FIN -- 

if __name__ == "__main__":
    publication()       #Fonctionnalit� de Publication de Fichier Photos Al�atoire
    temps()             #Fonctionnalit� permettant d'Afficher le temps en format "Heure,Minute,Seconde" suite � Publication du contenu 
