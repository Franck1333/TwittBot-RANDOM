#!/usr/bin/env python
# -*- coding: cp1252 -*-

import serial
import time
import os
import sys
import datetime

#OBTENTION DE L'HEURE ACTUEL sous format HEURE,MINUTE,SECONDE

def temps():
    #-- DEBUT -- Heure,Minute,Seconde
    tt = time.time()
    system_time = datetime.datetime.fromtimestamp(tt).strftime('%H:%M:%S')
    print ("Publié a :", system_time)
    #-- FIN -- Heure,Minute,Seconde




if __name__ == "__main__":
    temps()
