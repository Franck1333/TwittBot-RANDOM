# TwittBot-RANDOM
This project aims to Send pictures or any other content Randomly on Twitter

## Some Tweets
First Tweet : https://twitter.com/Franck1333/status/1008860353533538304

Second Tweet : https://twitter.com/Franck1333/status/1008869938788995072

Third Tweet : https://twitter.com/Franck1333/status/1008882549861638150

## Getting Started
To get a copy of the project , you can go on the GitHub's webpage of the project and click on the green button to download as a .ZIP file.

However , if you're using a prompt on a unix machine use this line :
```
git clone https://github.com/Franck1333/TwittBot-RANDOM.git
```
However , before doing anything  , you should check updates of your platform before Install and Run this project , it's recommended ;=)
with that command line :

```
sudo apt-get update && sudo apt-get upgrade
```

### Prerequisites
To use the project , you will need some Hardware:

A Raspberry Pi (Why not a ZERO Pi :+1: )

A Micro S.D card (8 Gb Minimum)

A screen (Anything you need to look at your console or SSH/VNC)

And you will also need some libraries that are already include Natively in python :

```
import time
import os
import sys
import datetime

#Blibliothèque Twython (Twitter/Python)
from twython import Twython

#Blibliothèque RANDOM pour l'utilisation de l'aléatoire
import random

#Blibliothèque du Projet
from temps_sys import temps
```

#### KEYS

To make work the project , you will need some Identification keys that you will ask to Twitter to get them;

You will need :
```
#IDENTIFIANTS DE CONNEXION a l'API Twitter -- DEBUT -- 
CONSUMER_KEY = '***'     #Changer ces identifiants par les vôtres
CONSUMER_SECRET = '***'  #Changer ces identifiants par les vôtres
ACCESS_KEY = '***'       #Changer ces identifiants par les vôtres
ACCESS_SECRET = '***'    #Changer ces identifiants par les vôtres
print("Identification en cours...")
twitter = Twython(CONSUMER_KEY,CONSUMER_SECRET,ACCESS_KEY,ACCESS_SECRET)
#IDENTIFIANTS DE CONNEXION a l'API Twitter -- FIN --
```
You can ask all those keys, here at this adress : https://apps.twitter.com/

### Installing
  To get and install the files , use this line: 
  ```
  git clone https://github.com/Franck1333/TwittBot-RANDOM.git
  ```
### RUN
To run the project , you've got many possibilities as : 

#### First Way to run the project : 
  To run the project , you can run the small script file called "Start_TwittBot.sh" ; it's will launch the project in the background

#### Second Way to run the project : 
  To run the project ; if you want to see the console activities , you can launch the file called "Start_TwittBot.sh" into the Command Line Prompt with "./Start_TwittBot.sh"
  
#### Third Way to run the project :
  To run the project ; if you want to see the console activities , you can launch the file called "bot.py" into the Command Line Prompt with "sudo python bot.py"
  
#### The Fourth Way to run the project :
  To run the project ; if you want the project run automatically every 2 minutes :
  
  You can use 'CronTab' like this:
  
  ```
  sudo crontab -e
  ```
  ```
   */2 * * * * /home/pi/TwittBot-RANDOM/MyWork/Start_TwittBot.sh >/dev/null 2>&1
  ```

OR YOU CAN USE : https://crontab-generator.org/

## The Folders and Files
In this project , you will be able to see two main Directories:

### Directories

/TwittBot-RANDOM/"Exemple"/ : Which show you the examples that I use or made for this project

/TwittBot-RANDOM/"MyWork"/ : Which show you the source code of the project

#### Files in /TwittBot-RANDOM/"MyWork"/

bot.py : It's the main python file of the project
temps_sys.py : This python file allow to get the current time
Start_TwittBot.sh : This script allow you to launch the project
READ_CRONTAB.txt : This documents is a tutorial for use Crontab on your system.
##### Files in /TwittBot-RANDOM/MyWork/images
In this folder you will access to some pictures to test the bot:

```
Beijing.jpg
Glass.jpg
HongKong.jpg
Osaka.jpg
Tokyo.jpg
Ziba.jpg
```
I want to go to those places ; I will one day :heart: !!!

## Authors

* **Franck ROCHAT** - *Initial work* - [Franck ROCHAT](https://github.com/Franck1333)
Thank You ! :hearts:




