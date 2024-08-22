#!/usr/bin/env python
# -*- coding: utf-8 -*-

# udanie statusu + mena + priezviska
Status = raw_input ("Pán - stlač P\nPani - stlač Z\nSlečna - stlač S:\n")

if Status == "P": 
                 Oslovenie = "Pán"
elif Status == "Z":
                 Oslovenie = "Pani"
elif Status == "S":
                 Oslovenie = "Slečna" 
else :
    print "Nesprávna volba skus ešte raz"
    exit ()
    
Meno = raw_input("Ako sa voláš krsním menom? ")             #zadanie krsneho mena
Priezvisko = raw_input ("Ako sa voláš priezviskom? ")       #zadanie Priezviska 

Cele_meno = Meno + " " + Priezvisko                         #vytvorenie mena a priezviska spoliu z medzerou

Meno_c = int(len(Meno))                                     #prevedenie množiny zo string (znakou) na integer (celé číslo) + Spočítanie písmen z MENO a vyjadrenie číslovkou

Priezvisko_c = int(len(Priezvisko))                         #prevedenie množiny zo string (znakou) na integer (celé číslo) + Spočítanie písmen z PRIEZVISKO a vyjadrenie číslovkou

Spolu = Meno_c+Priezvisko_c                                 #spočítanie písmen MENA a PRIEZVISKA

Spolu_c = str(Spolu)                                        #prevedenie množiny SPOLu z integer (celé číslo) na množinu string (znak)


    

#samotný výpis 

print "\n\n\nAhoj " + (Oslovenie) + ". " + (Cele_meno)

print "Tvoje krsné meno sa začína na " + Meno[0] + " a končí na " + Meno[-1] + ". A priezvisko začína na " + Priezvisko[0] + " a končí na " + Priezvisko[-1]

print "Od zadu sa to píše: " + (Meno[::-1]) + " " + (Priezvisko[::-1]) + " a má " + (Spolu_c) +" písmen."

print "Pri čom tvoje inciály sú: " + (Meno[0]) + (Priezvisko[0])
