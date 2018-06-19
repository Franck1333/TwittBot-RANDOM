#!/usr/bin/env python
# -*- coding: cp1252 -*-

#Aides : https://twython.readthedocs.io/en/latest/usage/advanced_usage.html
#Aides : https://www.raspberrypi.org/forums/viewtopic.php?t=111751
#Aides : https://stackoverflow.com/questions/701402/best-way-to-choose-a-random-file-from-a-directory

import serial
import time
import os
import sys
import datetime

#Blibliothèque Twython (Twitter/Python)
from twython import Twython

#Blibliothèque RANDOM pour l'utilisation de l'aléatoire
import random

#CHOIX DU FICHIER --DEBUT--
randompic = random.choice(os.listdir("/home/pi/TwittBot-RANDOM/MyWork/images/"))    #Choix d'une Image parmis celles présente dans le Repertoire indiqué

file = '/home/pi/TwittBot-RANDOM/MyWork/images/' + randompic                        #Enregistrement du Chemin et du fichier choisi dans une variable 'file'

photo = open(file, 'rb')                                                            #Ouverture du fichier choisi

print("Fichier RANDOM choisi se trouvant à cette endroit:", file)                   #Affichage du Chemin + Fichier choisi dans la console
#CHOIX DU FICHIER --FIN--
