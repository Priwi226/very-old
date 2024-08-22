#!/usr/bin/env python
# -*- coding: utf-8 -*-

                                    #               Importovanie pluginn
import os

print "Vypis particii:"
os.system ("lsblk -o NAME,FSTYPE,SIZE,MOUNTPOINT,LABEL")
print "Najdy svoj CD-ROM:\n"
CD = raw_input ("Zadaj cestu k CD-ROM: \n")
Subor = raw_input ("Zadaj nazov suboru bez koncovky:\n")
cesta = raw_input ("Zadaj niesto uloženia:\n")
print "A čakaj\n"
os.system ("cat /dev/"+ (CD) +"  > ~/"+ (Subor) +".iso")
os.system ("mv "+ (Subor) +".iso "+ (cesta))
print "Tvoj subor"+ (Subor) +"je uložený"+ (cesta) +"\n"+ (cesta , Subor)




