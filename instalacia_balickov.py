#!/usr/bin/env python
# -*- coding: utf-8 -*-
#chýba  
        # Viber  : http://download.cdn.viber.com/cdn/desktop/Linux/viber.deb

        #HMTL ---- sudo add-apt-repository ppa:webupd8team/brackets  ------  sudo apt-get update   ------ sudo apt-get install brackets
                                    #               Importovanie pluginn
import os
                                    #               Vykonať všetko 
print "    Obsah tejto inštalácie:\n\
Bully                       Screenlets\n\
Slowloris                   Skype\n\
Grub                        Finger print\n\
Google Earth                Conky\n\
Samba                       Code\n\
Youtube                     Tweak\n\
RAR                         Identifikatory\n\
Play on linux               Reaver\n\
Virtual box                 Wireshark\n\
VLC                         Ettercap\n\
K3B                         Inkscape\n\
Unetbottin                  Synaptic\n\
DIVx - Convert              Multisystem\n\
Teamviewer                  XnViewMP\n\
XnConvert                   Subterfuge\n\
Burg                        Konverzia ISO\n\
Konverzia MP3               Wine\n\
Aptitude                    Win USB\
Android tools               Handbrake\n\
Gparter                     Record Dekstop\n\
Adobe Flash Player          TOR\n\
Viber                       Steam\n\
Odstranenie hlášok"


                                    #               Zadanie čo má inšatlovať ALL

Vsetko = raw_input ("Inštalovať všetko ?\n A-ano, N-nie: ")
while Vsetko not in set (["A", "a", "N", "n"]):
    Vsetko = raw_input ("Inštalovať všetko ?\n A-ano, N-nie: ")
if Vsetko =="A":
    Aktualizacia = "A"
    KISO = "A"
    MP3 = "A"
    Wine = "A"
    Kamery = "A"
    Apitude = "A"
    Scrennlets = "A"
    Skype = "A"
    Fingerprint = "A"
    Conky = "A"
    Code = "A"
    Tweak = "A"
    Indikatory = "A"
    Wifi = "A"
    Ettercab = "A"
    Bully = "A"
    Slowloris = "A"
    Grub = "A"
    Earth = "A"
    Samba = "A"
    Youtube = "A"
    RAR = "A"
    Play_on_Linux = "A"
    Virtual_box = "A"
    VLC = "A"
    k3b = "A"
    inkscape = "A"
    unetbottin = "A"
    Synaptic = "A"
    Divx = "A"
    multisystem = "A"
    Teamviewer = "A"
    XnViewMP = "A"
    XnConvert = "A"
    Subterfuge = "A"
    rm = "A"
    Kamery = "A"
    Wine ="A"
    Aptitude ="A"
    Photorec ="A"
    Android ="A"
    Handbrake ="A"
    Gparted = "A"
    Record = "A"
    Win_usb = "A"
    Flashtools ="A"
    Filezilla = "A"
    Gimp = "A"
    adobe = "A"
    Tor ="A"
    Gnome ="A"
    Viber ="A"
    Steam ="A"
    Hlasky ="A"
    
                                    #               Zadanie rucnej instalacie 

if Vsetko == "N":
                                    #               Aktualizácia
    Aktualizacia = raw_input ("Spustit aktualizáciu ?\n A-ano, N-nie: ")
    while Aktualizacia not in set(["A", "N"]):
        Aktualizacia = raw_input ("Spustit aktualizáciu ?\n A-ano, N-nie: ")
            
                                    #               Wine
    Wine = raw_input ("Inštalovať Wine ?\n A-ano, N-nie: ")
    while Wine not in set (["A", "N"]):
        Wine = raw_input ("Inštalovať Wine ?\n A-ano, N-nie: ")
    
                                        #               Grub
    Grub = raw_input ("Inštalovať Grub ? \n A-ano, N-nie: ")
    while Grub not in set (["A", "N"]):
        Grub = raw_input ("Inštalovať Grub ? \n A-ano, N-nie: ")
        
                                            #               Photorec
    Photorec = raw_input ("Inštalovat Photorec ? \n A-ano, N-nie ")
    while Photorec not in set (["A", "N"]):
        Photorec = raw_input ("Inštalovat Photorec ? \n A-ano, N-nie ")
                                            #               Finger print
    Fingerprint = raw_input ("Inštalovať Finger print ?\n A-ano, N-nie: ")
    while Fingerprint not in set (["A", "N"]):
        Fingerprint = raw_input ("Inštalovať Finger print ?\n A-ano, N-nie: ")

                                    #               Konverzia ISO
    KISO = raw_input ("Inštalovať Konverzia ISO ?\n A-ano, N-nie: ")
    while KISO not in set (["A", "N"]):
        KISO = raw_input ("Inštalovať Konverzia ISO ?\n A-ano, N-nie: ") 
        
                                    #               Konverzia MP3
    MP3 = raw_input ("Inštalovať Konverzia mp3 ?\n A-ano, N-nie: ")
    while MP3 not in set (["A", "N"]):
        MP3 = raw_input ("Inštalovať Konverzia mp3 ?\n A-ano, N-nie: ")   

                                    #               Scrennlets
    Scrennlets = raw_input ("Inštalovať Srennleats ?\n A-ano, N-nie: ")
    while Scrennlets not in set (["A", "N"]):
        Scrennlets = raw_input ("Inštalovať Srennleats ?\n A-ano, N-nie: ")
    
                                    #               Skype
    Skype = raw_input ("Inštalovať Skype ?\n A-ano, N-nie: ")
    while Skype not in set (["A", "N"]):
        Skype = raw_input ("Inštalovať Skype ?\n A-ano, N-nie: ")
    

                                    #               Conky manager
    Conky = raw_input ("Inštalovať Conky manager? \n A-ano, N-nie: ")
    while Conky not in set (["A", "N"]):
        Conky = raw_input ("Inštalovať Conky manager? \n A-ano, N-nie: ")

                                    #               Programovacie jazyky
    Code = raw_input ("Inštalovať Programovacie jazyky ? \n A-ano, N-nie: ")
    while Code not in set (["A", "N"]):
        Code = raw_input ("Inštalovať Programovacie jazyky ? \n A-ano, N-nie: ")

                                    #               Tweak
    #Tweak = raw_input ("Inštalovať Tweak ? \n A-ano, N-nie: ")
    #hile Tweak not in set (["A", "N"]):
        #Tweak = raw_input ("Inštalovať Tweak ? \n A-ano, N-nie: ")

                                    #               Indykatory
    Indikatory = raw_input ("Inštalovať Indikytory ? \n A-ano, N-nie: ")
    while Indikatory not in set (["A", "N"]):
        Indikatory = raw_input ("Inštalovať indikatory ? \n A-ano, N-nie: ")

                                    #               Wifi
    Wifi = raw_input ("Inštalovať Wifi ? \n A-ano, N-nie: ")
    while Wifi not in set (["A", "N"]):
        Wifi = raw_input ("Inštalovať Wifi ? \n A-ano, N-nie: ")
    
                                    #               Ettercab
    Ettercab = raw_input ("Inštalovať Ettercab ? \n A-ano, N-nie: ")
    while Ettercab not in set (["A", "N"]):
        Ettercab = raw_input ("Inštalovať Ettercab ? \n A-ano, N-nie: ")
    
                                    #               Bully
    Bully = raw_input ("Inštalovať Bully ? \n A-ano, N-nie: ")
    while Bully not in set (["A", "N"]):
        Bully = raw_input ("Inštalovať Bully ? \n A-ano, N-nie: ")

                                    #               Slowloris
    Slowloris = raw_input ("Inštalovať Slowloris ? \n A-ano, N-nie: ")
    while Slowloris not in set (["A", "N"]):
        Slowloris = raw_input ("Inštalovať Slowloris ? \n A-ano, N-nie: ")

                                    #               Google Earth
    Earth = raw_input ("Inštalovať Google earht ? \n A-ano, N-nie: ")
    while Earth not in set (["A", "N"]):
        Earth = raw_input ("Inštalovať Earth ? \n A-ano, N-nie: ")
    
                                    #               Samba
    Samba = raw_input ("Inštalovať Samba ? \n A-ano, N-nie: ")
    while Samba not in set (["A", "N"]):
        Samba = raw_input ("Inštalovať Samba ? \n A-ano, N-nie: ")
    
                                    #               Youtube-dl
    Youtube = raw_input ("Inštalovať Youtube ? \n A-ano, N-nie: ")
    while Youtube not in set (["A", "N"]):
        Youtube = raw_input ("Inštalovať Youtube ? \n A-ano, N-nie: ")
 
                                    #               RAR
    RAR = raw_input ("Inštalovať rar ? \n A-ano, N-nie: ")
    while RAR not in set (["A", "N"]):
        RAR = raw_input ("Inštalovať rar ? \n A-ano, N-nie: ")

                                    #               Play on linux
    Play_on_Linux = raw_input ("Inštalovať Play_on_Linux ? \n A-ano, N-nie: ")
    while Play_on_Linux not in set (["A", "N"]):
        Play_on_Linux = raw_input ("Inštalovať Play_on_Linux ? \n A-ano, N-nie: ")
    
                                    #               Virtual box
    Virtual_box = raw_input ("Inštalovať Virtual box ? \n A-ano, N-nie: ")
    while Virtual_box not in set (["A", "N"]):
        Virtual_box = raw_input ("Inštalovať Virtual box ? \n A-ano, N-nie: ")
    
                                    #               VLC
    VLC = raw_input ("Inštalovať VLC ? \n A-ano, N-nie: ")
    while VLC not in set (["A", "N"]):
        VLC = raw_input ("Inštalovať VLC ? \n A-ano, N-nie: ")
    
                                    #               K3B
    k3b = raw_input ("Inštalovať k3b ? \n A-ano, N-nie: ")
    while k3b not in set (["A", "N"]):
        k3b = raw_input ("Inštalovať k3b ? \n A-ano, N-nie: ")

                                    #               Inkscape
    inkscape = raw_input ("Inštalovať inkscape ? \n A-ano, N-nie: ")
    while inkscape not in set (["A", "N"]):
        inkscape = raw_input ("Inštalovať inkcape ? \n A-ano, N-nie: ")

                                    #               Unetbootin
    unetbottin = raw_input ("Inštalovať Unetbootin ? \n A-ano, N-nie: ")
    while unetbottin not in set (["A", "N"]):
        unetbootin = raw_input ("Inštalovať unetbootin ? \n A-ano, N-nie: ")

                                    #               Synaptic
    Synaptic = raw_input ("Inštalovať Synaptic ? \n A-ano, N-nie: ")
    while Synaptic not in set (["A", "N"]):
        Synaptic = raw_input ("Inštalovať Synaptic ? \n A-ano, N-nie: ")
        
                                    #               Aptitude
    Aptitude = raw_input ("Inštalovať Aptitude ? \n A-ano, N-nie: ")
    while Aptitude not in set (["A", "N"]):
        Aptitude = raw_input ("Inštalovať Aptitude ? \n A-ano, N-nie: ")

                                    #               Divx-converter
    Divx = raw_input ("Inštalovať Divx-converter ? \n A-ano, N-nie: ")
    while Divx not in set (["A", "N"]):
        Divx = raw_input ("Inštalovať Divx-converter ? \n A-ano, N-nie: ")

                                    #               Multisystem
    multisystem = raw_input ("Inštalovať Multisystem ? \n A-ano, N-nie: ")
    while Divx not in set (["A", "N"]):
        multisystem = raw_input ("Inštalovať Multisystem ? \n A-ano, N-nie: ")

                                    #               Teamviewer
    Teamviewer = raw_input ("Inštalovať Teamviewer ? \n A-ano, N-nie: ")
    while Teamviewer not in set (["A", "N"]):
        Teamviewer = raw_input ("Inštalovať Teamviewer ? \n A-ano, N-nie: ")

                                    #               XnViewMP
    XnViewMP = raw_input ("Inštalovať XnViewMP ? \n A-ano, N-nie: ")
    while XnViewMP not in set (["A", "N"]):
        XnViewMP = raw_input ("Inštalovať XnViewMP ? \n A-ano, N-nie: ")

                                    #               XnConvert
    XnConvert = raw_input ("Inštalovať XnConvert ? \n A-ano, N-nie: ")
    while XnConvert not in set (["A", "N"]):
        XnConvert = raw_input ("Inštalovať XnConvert ? \n A-ano, N-nie: ")

                                    #               Subterfuge
    Subterfuge = raw_input ("Inštalovať Subterfuge ? \n A-ano, N-nie: ")
    while Subterfuge not in set (["A", "N"]):
        Subterfuge = raw_input ("Inštalovať Subterfuge ? \n A-ano, N-nie: ")
        
                                    #               Kamery
    Kamery = raw_input ("Inštalovať Kamery do Firefoxu ? \n A-ano, N-nie: ")
    while Kamery not in set (["A", "N"]):
        Kamery = raw_input ("Inštalovať Kamery do Firefoxu ? \n A-ano, N-nie: ")
        
                                    #               Record Desktop
    Record = raw_input ("Inštalovať Record Desktop ? \n A-ano, N-nie: ")
    while Record not in set (["A", "N"]):
        Record = raw_input ("Inštalovať Record Dektop ? \n A-ano, N-nie: ")
        
                                    #               Android tools
    Android =raw_input ("Inštalovať Android-tools ? \n A-ano, N-nie: ")
    while Android not in set (["A", "N"]):
        Android =raw_input ("Inštalovať Android-tools ? \n A-ano, N-nie: ")
        
                                    #               Handbrake
    Handbrake =raw_input ("Inštalovať Handbrake ? \n A-ano, N-nie: ")
    while Handbrake not in set (["A", "N"]):
        Handbrake =raw_input ("Inštalovať Handbrake ? \n A-ano, N-nie: ")
        
                                    #               Gparted
    Gparted =raw_input ("Inštalovať Gparted ? \n A-ano, N-nie: ") 
    while Gparted not in set (["A", "N"]):
            Gparted =raw_input ("Inštalovať Gparted ? \n A-ano, N-nie: ")
            
                                    #               Win USB
    Win_usb = raw_input ("Inštalovať Win USB ? \n A-ano, N-nie: ")
    while Win_usb not in set (["A", "N"]):
        Win_usb = raw_input ("Inštalovať Win USB ? \n A-ano, N-nie: ")
        
                                    #               FlashTools
    Flashtools = raw_input ("Inštalovať Flashtools ? \n A-ano, N-nie: ")
    while Flashtools not in set (["A", "N"]):
        Flashtools = raw_input ("Inštalovať Flashtools ? \n A-ano, N-nie: ")
        
                                            #               Filezilla
    Filezilla = raw_input ("Inštalovať Filezilla ? \n A-ano, N-nie: ")
    while Filezilla not in set (["A", "N"]):
        Filezilla = raw_input ("Inštalovať Filezilla ? \n A-ano, N-nie: ")
        
                                            #               Gimp
    Gimp = raw_input ("Inštalovať Gimp ? \n A-ano, N-nie: ")
    while Gimp not in set (["A", "N"]):
        Gimp = raw_input ("Inštalovať Gimp ? \n A-ano, N-nie: ")
        
                                    #               Adobe flash player
    adobe = raw_input ("Inštalovať Adobe Flash Player ? \n A-ano, N-nie: ")
    while adobe not in set (["A", "N"]):
        adobe = raw_input ("Inštalovať Adobe Flash Player ? \n A-ano, N-nie: ")
        
                                    #               Tor
    Tor = raw_input ("Inštalovať Tor/Tor-Browser ? \n A-ano, N-nie: ")
    while Tor not in set (["A", "N"]):
        Tor = raw_input ("Inštalovať Tor/Tor-Browser ? \n A-ano, N-nie: ")  
        
                                    #               Viber
    Viber = raw_input ("Inštalovať Viber ? \n A-ano, N-nie: ")
    while Viber not in set (["A", "N"]):
        Viber = raw_input ("Inštalovať Viber ? \n A-ano, N-nie: ")
    
                                    #              Steam
    Steam = raw_input ("Inštalovať Steam ? \n A-ano, N-nie: ")
    while Steam not in set (["A", "N"]):
        Steam = raw_input ("Inštalovať Steam ? \n A-ano, N-nie: ")
        
                                    #              Steam
    Hlasky = raw_input ("Inštalovať Hlasky ? \n A-ano, N-nie: ")
    while Hlasky not in set (["A", "N"]):
        Hlasky = raw_input ("Inštalovať Hlasky ? \n A-ano, N-nie: ")
                                    #               Gnome 3.16
    #Gnome = raw_input ("Inštalovať Gnome ?\n A-ano, N-nie: ")
    #while Gnome not in set (["A", "N"]):
        #Gnome = raw_input ("Inštalovať Gnome ?\n A-ano, N-nie: ")

                                    #               Instalaciacia hier
Hry = raw_input ("Inštalovať Hry ?\n A-ano, N-nie: ")
while Vsetko not in set (["A", "N"]):
    Vsetko = raw_input ("Inštalovať Hry ?\n A-ano, N-nie: ")

if Hry =="A":
    DOOM = "A"
    Silent_Hunter = "A"
    
if Hry =="N":
        
                                                    #           DOOM
    DOOM = raw_input ("Inštalovať DOOM ?\n A-ano, N-nie: ")
    while DOOM not in set (["A", "N"]):
        DOOM = raw_input ("Inštalovať DOOM ?\n A-ano, N-nie: ")
            
                                                    #           Silent Hunder linux            
    Silent_Hunter = raw_input ("Inštalovať Silent Hunter ?\n A-ano, N-nie: ")
    while Silent_Hunter not in set (["A", "N"]):
        Silent_Hunter = raw_input ("Inštalovať Silent Hunter ?\n A-ano, N-nie: ")
        
                                        #               Mazanie suborov po inštalácii
    rm = raw_input ("Zmazať stiahnute subory po inštalácii? \n A-ano, N-nie: ")
    while rm not in set (["A", "N"]):
        rm = raw_input ("Zmazať stiahnute subory po inštalácii? \n A-ano, N-nie: ")
        

            
            
        


########################################Tvorba reposiry ####################

print "                         Pridavanie Repozitárov "

f=open ("repository.py","a")
f.write ("#!/usr/bin/env python \n\
# -*- coding: utf-8 -*-\n \n\
import os \n\n")
f.close

if Grub =="A":
    f=open ("repository.py","a")
    f.write ("os.system (\"sudo add-apt-repository ppa:danielrichter2007/grub-customizer -y \")\n""")
    f.write ("os.system (\"sudo add-apt-repository ppa:n-muench/burg -y\") \n")
    f.close
if Fingerprint == "A":
    f=open ("repository.py","a")
    f.write ("os.system (\"sudo add-apt-repository ppa:fingerprint/fingerprint-gui -y\") \n""")
    f.close
if Conky == "A":
    f=open ("repository.py","a")
    f.write ("os.system (\"sudo add-apt-repository -y ppa:teejee2008/ppa -y\") \n")
    f.close
if Tweak == "A":
    f=open ("repository.py","a")
    f.write ("os.system (\"sudo add-apt-repository ppa:tualatrix/ppa -y\") \n")
    f.close
if Indikatory =="A":
    f=open ("repository.py","a")
    f.write ("os.system (\"sudo add-apt-repository ppa:nilarimogard/webupd8 -y\")\n\
os.system (""\"sudo add-apt-repository ppa:noobslab/apps -y\")\n\
os.system (""\"sudo add-apt-repository ppa:atareao/atareao -y\")\n\
os.system (""\"sudo add-apt-repository ppa:indicator-multiload/stable-daily -y\")\n\
os.system (""\"sudo add-apt-repository ppa:atareao/atareao -y\")\n\
os.system (""\"sudo add-apt-repository ppa:umang/indicator-stickynotes -y\")\n\
os.system (""\"sudo add-apt-repository ppa:noobslab/indicatorssudo -y\")\n\
os.system (""\"sudo add-apt-repository ppa:bhdouglass/indicator-remindor -y\")\n")
    f.close
if multisystem =="A":
    f=open ("repository.py","a")
    f.write ("os.system (\"sudo apt-add-repository 'deb http://liveusb.info/multisystem/depot all main'\")\n")
    f.close
if Win_usb =="A":
    f=open ("repository.py","a")
    f.write ("os.system (\"sudo add-apt-repository ppa:colingille/freshlight -y -qq \")\n")
    f.close
if Tor =="A":  
    f=open ("repository.py","a")
    f.write ("os.system (\"sudo add-apt-repository ppa:webupd8team/tor-browser -y\")\n")
    f.close
if Silent_Hunter =="A":
    f=open ("repository.py","a")
    f.write ("os.system (\"sudo add-apt-repository ppa:baegirxx-googlemail/dftd-latest -y\")\n")
    f.close
	
os.system ("python repository.py")
os.system ("exit")
os.system ("chmod +x repository.py")
os.system ("sudo ./repository.py")




################################################Samotná inštalácia ################################


                                    #               Aktualizácia
if Aktualizacia == "A":
    print "\n\n                                                      Aktualizacia"
    print "sudo apt-get update -qq"
    os.system ("sudo apt-get update -qq")
    print "sudo apt-get upgrade -y -qq"
    os.system ("sudo apt-get upgrade -y -qq")
    print "sudo apt-get autoremove"
    os.system ("sudo apt-get autoremove")
    os.system ("clear")
    print "sudo apt-get dist-upgrade -y -qq"
    os.system ("sudo apt-get dist-upgrade -y -qq")
    print "sudo apt-get autoremove"
    os.system ("sudo apt-get autoremove")
    os.system ("clear")
    print "Vytvorenie skripu v adresary /bin/"
    os.system ("cd /bin/")
    f=open ("aktualizacia","w")
    f.write ("#!/usr/bin/env python\n\
# -*- coding: utf-8 -*-\n\
import os\n\
Sposob = raw_input (\"Reštartovať -R\\nVypnúť -V\\nBez reštartu/vypnutia -0\\enter\\n\")\n\
while Sposob not in set ([\"R\", \"r\", \"V\", \"v\" \"0\", \"\"]):\n\
    Sposob = raw_input (\"Reštartovať -R\\nVypnúť -V\\nBez reštartu/vypnutia -0\\Enter\\n\")\n\
os.system (\"sudo apt-get update -y\")\n\
os.system (\"sudo apt-get upgrade -y\")\n\
os.system (\"sudo apt-get dist-upgrade -y\")\n\
os.system (\"sudo apt-get autoremove -y\")\n\
if Sposob ==\"R\":\n\
    os.system (\"sudo reboot\")\n\
if Sposob ==\"r\":\n\
    os.system (\"sudo reboot\")\n\
if Sposob ==\"V\":\n\
    os.system (\"sudo poweroff\") \n\
if Sposob ==\"V\":\n\
    os.system (\"sudo poweroff\")")
    f.close()
    os.system ("chmod +x aktualizacia")
    os.system ("sudo cp aktualizacia /bin/")
    f=open ("zoznam.txt","a")
    f.write ("Zrealizovaná Aktualizácia---Vytvorení Script \"aktualizácia\"\n\n\
    Dalej inštalované: \n")
    f.close
    f=open ("zoznam.txt")
    print f.read ()
    f.close
                                    #               Wine
if Wine == "A":
    print "\n\n                                                      WINE"
    print "sudo apt-get install wine -y -qq"
    os.system ("sudo apt-get install wine -y -qq")
    print "sudo apt-get install winetricks -y -qq"
    os.system ("sudo apt-get install winetricks -y -qq")
    os.system ("clear")
    f=open ("zoznam.txt","a")
    f.write ("Wine\n")
    f.close
    f=open ("zoznam.txt")
    print f.read ()
    f.close
                                    #               Grub

if Grub =="A":
    print "\n\n                                                  GRUB"
    f=open ("repository.txt","a")   
    print "sudo apt-get install grub-customizer -y -qq"
    os.system ("sudo apt-get install grub-customizer -y -qq")
    print "sudo apt-get install burg burg-themes -y -qq"
    os.system ("sudo apt-get install burg burg-themes -y -qq")
    print "sudo burg-install \"(hd0)\""
    os.system ("sudo burg-install \"(hd0)\"")
    print "sudo update-burg"
    os.system ("sudo update-burg")
    print "sudo burg-emu"
    os.system ("sudo burg-emu")
    os.system ("clear")
    f=open ("zoznam.txt","a")
    f.write ("Grub \n")
    f.close
    f=open ("zoznam.txt")
    print f.read ()
    f.close
    
                                    #               Fingerprint
    
if Fingerprint == "A":
    print "\n\n                                                      FINGER PRINT"
    print "sudo apt-get update -qq"
    os.system ("sudo apt-get update -qq")
    print "sudo apt-get install libbsapi policykit-1-fingerprint-gui fingerprint-gui -y -qq"    # ROZDELI DO PRIKAZOV
    os.system ("sudo apt-get install libbsapi")
    os.system ("sudo apt-get install policykit-1-fingerprint-gui -y -qq")
    os.system ("fingerprint-gui -y -qq")   
    os.system ("clear")
    f=open ("zoznam.txt","a")
    f.write ("Finger Print \n")
    f.close
    f=open ("zoznam.txt")
    print f.read ()
    f.close
    
                                        #               Fingerprint
    
if Steam == "A":
    print "\n\n                                                      Steam"
    print "sudo apt-get install steam"
    os.system ("sudo apt-get install steam -y")
    os.system ("clear")
    f=open ("zoznam.txt","a")
    f.write ("Steam\n")
    f.close
    f=open ("zoznam.txt")
    print f.read ()
    f.close
    
                                    #               Wifi

if Wifi == "A":
    print "\n\n                                                      WIFI (libpcap-dev libsqlite3-dev reaver aircrack-ng wireshark )"
    print "sudo apt-get install libpcap-dev libsqlite3-dev reaver aircrack-ng wireshark -y -qq"
    os.system ("sudo apt-get install libpcap-dev libsqlite3-dev reaver aircrack-ng wireshark -y -qq")
    os.system ("clear")
    f=open ("zoznam.txt","a")
    f.write ("WIFI : \n\
            Reaver\n\
            Wireshark\n\
            Aircrack-ng \n")
    f.close
    f=open ("zoznam.txt")
    print f.read ()
    f.close
                                    #               Photorec
    
if Photorec == "A":
    print "\n\n                                                      PHOTOREC"
    print "sudo apt-get install testdisk"
    os.system ("sudo apt-get install testdisk")
    os.system ("clear")
    f=open ("zoznam.txt","a")
    f.write ("Photorec \n")
    f.close
    f=open ("zoznam.txt")
    print f.read ()
    f.close
                                                            
                                    #               konverzia ISO
if KISO == "A":
    print "\n\n                                                      Konverzia ISO"
    print "sudo apt-get install ccd2iso -y -qq"
    os.system ("sudo apt-get install ccd2iso -y -qq")                          #ccd2iso Syntax,,,,, ccd2iso file.img file1.iso
    os.system ("clear")
    f=open ("zoznam.txt","a")
    f.write ("Konverzia ISO \n")
    f.close
    f=open ("zoznam.txt")
    print f.read ()
    f.close
                                    #               Konverzia MP3
if MP3 == "A":
    print "\n\n                                                      Konverzia MP3"
    print "sudo apt-get install soundconverter -y -qq"
    os.system ("sudo apt-get install soundconverter -y -qq")
    os.system ("clear")
    f=open ("zoznam.txt","a")
    f.write ("Konveerzia MP3 \n")
    f.close
    f=open ("zoznam.txt")
    print f.read ()
    f.close
                                    #               Scrennlets
if Scrennlets == "A":
    print "\n\n                                                      SCRENNLETS"
    print "sudo apt-get install screenlets screenlets-pack-all -y -qq"
    os.system ("sudo apt-get install screenlets screenlets-pack-all -y -qq")  
    os.system ("clear")
    f=open ("zoznam.txt","a")
    f.write ("Screan Lets \n")
    f.close
    f=open ("zoznam.txt")
    print f.read ()
    f.close
    
                                    #               Skype
if Skype =="A":
    print "\n\n                                                      SKYPE"
    #print "sudo dpkg --add-architecture i386 -y -qq"
    #os.system ("sudo dpkg --add-architecture i386 -qq")
    #print "sudo add-apt-repository \"deb http://archive.canonical.com/ $(lsb_release -sc) partner\" -y"
    #os.system ("sudo add-apt-repository \"deb http://archive.canonical.com/ $(lsb_release -sc) partner\" -y")
    print "sudo apt-get install skype -y -qq"
    os.system ("sudo apt-get install skype -y -qq")
    os.system ("clear")
    f=open ("zoznam.txt","a")
    f.write ("Skype \n")
    f.close
    f=open ("zoznam.txt")
    print f.read ()
    f.close
    
                                    #               Conky manager
if Conky == "A":
    print "\n\n                                                      CONKY"
    print "sudo apt-get install conky-manager -y -qq"
    os.system ("sudo apt-get install conky-manager -y -qq")
    os.system ("clear")
    f=open ("zoznam.txt","a")
    f.write ("Conky \n")
    f.close
    f=open ("zoznam.txt")
    print f.read ()
    f.close
    
                                    #               Programovacie jazyky 
if Code == "A":
    print "\n\n                                                      PROGRAMOVACIE JAZYKY"
    print "sudo apt-get install spyder codeblocks -y -qq"
    os.system ("sudo apt-get install spyder codeblocks -y -qq")
    print "sudo apt-get install python python-tk idle python-pmw python-imaging -y -qq"
    os.system ("sudo apt-get install python python-tk idle python-pmw python-imaging -y -qq")
    os.system ("clear")
    f=open ("zoznam.txt","a")
    f.write ("Programovacie jazyky:\n\
            Codeblock\n\
            Spyder \n")
    f.close
    f=open ("zoznam.txt")
    print f.read ()
    f.close
    
                                    #               Tweak               

#if Tweak == "A":
    #print "\n\n                                                     TWEAK"
    #print "sudo apt-get install ubuntu-tweak -y -qq"
    #os.system ("sudo apt-get install ubuntu-tweak -y -qq")
    #os.system ("clear")
    #f=open ("zoznam.txt","a")
    #f.write ("Tweak \n")
    #f.close
    #f=open ("zoznam.txt")
    #print f.read ()
    #f.close
    
                                    #               Indykatory

if Indikatory =="A":
    print "\n\n                                                     IDENTIFIKATORY"
    print "sudo apt-get install indicator-synapse -y -qq"
    os.system ("sudo apt-get install indicator-synapse -y -qq")
    print "sudo apt-get install calendar-indicator -y -qq"
    os.system ("sudo apt-get install calendar-indicator -y -qq")
    print "sudo apt-get install indicator-multiload -y -qq"
    os.system ("sudo apt-get install indicator-multiload -y -qq")
    print "sudo apt-get install my-weather-indicator -y -qq"
    os.system ("sudo apt-get install my-weather-indicator -y -qq") 
    print "sudo apt-get install indicator-stickynotes -y -qq"
    os.system ("sudo apt-get install indicator-stickynotes -y -qq")
    print "sudo apt-get install diodon -y -qq"
    os.system ("sudo apt-get install diodon -y -qq")
    print "sudo apt-get install indicator-netspeed -y -qq"
    os.system ("sudo apt-get install indicator-netspeed -y -qq")
    print "sudo apt-get install dconf-editor -y -qq"
    os.system ("sudo apt-get install dconf-editor -y -qq") 
    print "sudo apt-get install indicator-remindor -y -qq"
    os.system ("sudo apt-get install indicator-remindor -y -qq")
    os.system ("clear")
    f=open ("zoznam.txt","a")
    f.write ("Indikatory \n")
    f.close
    f=open ("zoznam.txt")
    print f.read ()
    f.close
    

        
                                    #               Ettercab                
if Ettercab =="A":
    print "\n\n                                                 ETTERCAB"
    print "sudo apt-get install zlib1g zlib1g-dev -y -qq"
    os.system ("sudo apt-get install zlib1g zlib1g-dev -y -qq")
    print "sudo apt-get install build-essential -y -qq"
    os.system ("sudo apt-get install build-essential -y -qq")
    print "sudo apt-get install ettercap -y -qq"
    os.system ("sudo apt-get install ettercap -y -qq")
    print "sudo apt-get install ettercap-graphical -y -qq"
    os.system ("sudo apt-get install ettercap-graphical -y -qq")
    f=open ("zoznam.txt","a")
    f.write ("Ettervab \n")
    f.close
    f=open ("zoznam.txt")
    print f.read ()
    f.close
    
                                    #               Bully
if Bully =="A":
    print "\n\n                                                 BULLY"
    print "wget https://codeload.github.com/Lrs121/bully/zip/master"
    os.system ("wget https://codeload.github.com/Lrs121/bully/zip/master")
    print "unzip master"
    os.system ("unzip master")
    print "sudo apt-get -f install -y -qq"
    os.system ("sudo apt-get -f install -y -qq")
    print "sudo apt-get install libssl-dev -y -qq"
    os.system ("sudo apt-get install libssl-dev -y -qq")
    print "cd bully-master/src/"
    os.system ("cd bully-master/src/")
    print "sudo make"
    os.system ("sudo make")
    print "sudo make install"
    os.system ("sudo make install")
    print "cd ~/"
    os.system ("cd ~/")
    os.system ("clear")
    f=open ("zoznam.txt","a")
    f.write ("Bully \n")
    f.close
    f=open ("zoznam.txt")
    print f.read ()
    f.close
   
                                    #               Slowloris
if Slowloris =="A":
    print "\n\n                                                 SLOWLORIS"
    print "sudo wget https://codeload.github.com/llaera/slowloris.pl/zip/master"
    os.system ("sudo wget https://codeload.github.com/llaera/slowloris.pl/zip/master")
    print "unzip master.1"
    os.system ("unzip master.1")
    os.system ("cd slowloris.pl-master/")
    print "chmod 777 slowloris.pl "
    os.system ("chmod 777 slowloris.pl")
    print "sudo cp slowloris.pl /bin/"
    os.system ("sudo cp slowloris.pl /bin/")
    os.system ("cd ..")
    print "rm -r slowloris.pl-master/"
    os.system ("rm -r slowloris.pl-master/")
    os.system ("clear")
    f=open ("zoznam.txt","a")
    f.write ("Slowloris \n")
    f.close
    f=open ("zoznam.txt")
    print f.read ()
    f.close

                                    #               Record Desktop

if Record =="A":
    print "\n\n                                                 Record Desktop"
    print "sudo apt-get install gtk-recordmydesktop -y"
    os.system ("sudo apt-get install gtk-recordmydesktop -y")
    os.system ("clear")
    f=open ("zoznam.txt","a")
    f.write ("Record Desktop \n")
    f.close
    f=open ("zoznam.txt")
    print f.read ()
    f.close
    
                                    #               Google Earth

if Earth =="A":   
    print "\n\n                                                         GOOGLE EARTH"
    print "sudo apt-get install libfontconfig1:i386 libx11-6:i386 libxrender1:i386 libxext6:i386 libgl1-mesa-glx:i386 libglu1-mesa:i386 libglib2.0-0:i386 libsm6:i386"
    os.system ("sudo apt-get install libfontconfig1:i386 libx11-6:i386 libxrender1:i386 libxext6:i386 libgl1-mesa-glx:i386 libglu1-mesa:i386 libglib2.0-0:i386 libsm6:i386")
    print "wget http://dl.google.com/dl/earth/client/current/google-earth-stable_current_i386.deb"
    os.system ("wget http://dl.google.com/dl/earth/client/current/google-earth-stable_current_i386.deb")
    print "sudo dpkg -i google-earth-stable_current_i386.deb"
    os.system ("sudo dpkg -i google-earth-stable_current_i386.deb")
    print "sudo apt-get -f install -y -qq"
    os.system ("sudo apt-get -f install -y -qq")
    os.system ("clear")
    f=open ("zoznam.txt","a")
    f.write ("Google Earth \n")
    f.close
    f=open ("zoznam.txt")
    print f.read ()
    f.close
   
                                    #               Samba

if Samba =="A":
    print "\n\n                                                         SAMBA"
    print "sudo apt-get install samba -y -qq"
    os.system ("sudo apt-get install samba -y -qq")
    print "sudo apt-get install system-config-samba -y -qq"
    os.system ("sudo apt-get install system-config-samba -y -qq")
    os.system ("clear")
    f=open ("zoznam.txt","a")
    f.write ("Samba \n")
    f.close
    f=open ("zoznam.txt")
    print f.read ()
    f.close
   
                                    #               Youtube-dl

if Youtube =="A":  
    print "\n\n                                                         YOUTUBE DOWNLOADER"
    print "sudo apt-get install youtube-dl -y -qq"
    os.system ("sudo apt-get install youtube-dl -y -qq")
    os.system ("clear")
    f=open ("zoznam.txt","a")
    f.write ("Youtube Downloader \n")
    f.close
    f=open ("zoznam.txt")
    print f.read ()
    f.close
 
                                    #               RAR

if RAR =="A":
    print "\n\n                                                         RAR"
    print "sudo apt-get install rar -y -qq"
    os.system ("sudo apt-get install rar -y -qq")
    os.system ("clear")
    f=open ("zoznam.txt","a")
    f.write ("RAR \n")
    f.close
    f=open ("zoznam.txt")
    print f.read ()
    f.close

                                    #               Gparted

if Gparted =="A":
    print "/n/n                                                         Gpartred"
    print "sudo apt-get install gparted"
    os.system ("sudo apt-get install gparted -y -qq")
    os.system ("clear")
    f=open ("zoznam.txt","a")
    f.write ("Gparted \n")
    f.close
    f=open ("zoznam.txt")
    print f.read ()
    f.close
                                                            
                                    #               Play on linux

if Play_on_Linux =="A":
    print "\n\n                                                         PLAY ON LINUX"
    print "sudo apt-get install playonlinux -y -qq"
    os.system ("sudo apt-get install playonlinux -y -qq")
    os.system ("clear")
    f=open ("zoznam.txt","a")
    f.write ("Play on linux \n")
    f.close
    f=open ("zoznam.txt")
    print f.read ()
    f.close
  
                                    #               Virtual box

if Virtual_box =="A":
    print "\n\n                                                          VIRTUAL BOX"
    print "sudo apt-get install virtualbox -y -qq"
    os.system ("sudo apt-get install virtualbox -y -qq")
    os.system ("clear")
    f=open ("zoznam.txt","a")
    f.write ("Virtual Box \n")
    f.close
    f=open ("zoznam.txt")
    print f.read ()
    f.close
   
                                    #               VLC

if VLC =="A":
    print "\n\n                                                          VLC"
    print "sudo apt-get install vlc -y -qq"
    os.system ("sudo apt-get install vlc -y -qq")
    os.system ("clear")
    f=open ("zoznam.txt","a")
    f.write ("VLC \n")
    f.close
    f=open ("zoznam.txt")
    print f.read ()
    f.close
  
                                      #               K3B

if k3b =="A":
    print "\n\n                                                          K3B"
    print "sudo apt-get install k3b -y -qq"
    os.system ("sudo apt-get install k3b -y -qq")
    print "sudo apt-get install k3b-i18n -y -qq"
    os.system ("sudo apt-get install k3b-i18n -y -qq")
    os.system ("clear")
    f=open ("zoznam.txt","a")
    f.write ("K3B - cz \n")
    f.close
    f=open ("zoznam.txt")
    print f.read ()
    f.close
  
                                    #               Inkscape

if inkscape =="A":
    print "\n\n                                                      INKSCAPE"
    print "sudo apt-get install inkscape -y -qq"
    os.system ("sudo apt-get install inkscape -y -qq")
    os.system ("clear")
    f=open ("zoznam.txt","a")
    f.write ("INKScape \n")
    f.close
    f=open ("zoznam.txt")
    print f.read ()
    f.close
  
                                      #               Unetbootin
if unetbottin =="A":
    print "\n\n                                                      UNETBOTTIN"
    print "sudo apt-get install unetbootin -y -qq"
    os.system ("sudo apt-get install unetbootin -y -qq")
    os.system ("clear")
    f=open ("zoznam.txt","a")
    f.write ("Unetbooting \n")
    f.close
    f=open ("zoznam.txt")
    print f.read ()
    f.close
   
                                    # Synptic

if Synaptic =="A":  
    print "\n\n                                                      SYNAPTIC"
    print "sudo apt-get install synaptic -y -qq"
    os.system ("sudo apt-get install synaptic -y -qq") 
    os.system ("clear")
    f=open ("zoznam.txt","a")
    f.write ("Synaptic \n ")
    f.close
    f=open ("zoznam.txt")
    print f.read ()
    f.close
  
                                    #               Aptitude
if Aptitude =="A":
    print "\n\n                                                      Aptitude"
    print "sudo apt-get install aptitude -y -qq"
    os.system ("sudo apt-get install aptitude -y -qq")
    print "sudo aptitude update -q"
    os.system ("sudo aptitude update -q")
    os.system ("clear")
    f=open ("zoznam.txt","a")
    f.write ("Aptitude \n ")
    f.close
    f=open ("zoznam.txt")
    print f.read ()
    f.close
    
                                     #               Divx-converter
if Divx =="A":
    print "\n\n                                                      DIVX CONVERTER"
    print "wget http://foxoman.googlecode.com/files/divxconverter_2.0.1-1_all.deb"
    os.system ("wget http://foxoman.googlecode.com/files/divxconverter_2.0.1-1_all.deb")
    print "sudo dpkg -i divxconverter_2.0.1-1_all.deb"
    os.system ("sudo dpkg -i divxconverter_2.0.1-1_all.deb")  
    os.system ("clear")
    f=open ("zoznam.txt","a")
    f.write ("Divx converter \n ")
    f.close
    f=open ("zoznam.txt")
    print f.read ()
    f.close
    
                                    #               multisystem 

if multisystem =="A":
    print "\n\n                                                       MULTISYSTEM"
    print "wget http://liveusb.info/multisystem/install-depot-multisystem.sh.tar.bz2"
    os.system ("wget http://liveusb.info/multisystem/install-depot-multisystem.sh.tar.bz2")
    print "tar -xjvf install-depo*"
    os.system ("tar -xjvf install-depot-multisystem.sh")
    print "sudo ./install-depot-multisystem.sh"
    os.system ("sudo ./install-depot-multisystem.sh")
    os.system ("clear")
    f=open ("zoznam.txt","a")
    f.write ("Multisystem \n")
    f.close
    f=open ("zoznam.txt")
    print f.read ()
    f.close 
  
                                    #               Teamviewer

if Teamviewer =="A":
    print "\n\n\n\n                                                  TEAMVIEWER     \n\n\n\n"
    print "wget http://downloadeu1.teamviewer.com/download/teamviewer_linux.deb"
    os.system ("wget http://downloadeu1.teamviewer.com/download/teamviewer_linux.deb")
    print "sudo dpkg --add-architecture i386 -qq"
    os.system ("sudo dpkg --add-architecture i386 -qq")
    print "sudo apt-get update -qq"
    os.system ("sudo apt-get update -qq")
    print "sudo dpkg -i teamviewer_linux.deb -qq"
    os.system ("sudo dpkg -i teamviewer_linux.deb -qq")
    print "sudo apt-get -f install -y -qq"
    os.system ("sudo apt-get -f install -y -qq")
    os.system ("clear")
    f=open ("zoznam.txt","a")
    f.write ("TeamViewer \n ")
    f.close
    f=open ("zoznam.txt")
    print f.read ()
    f.close
   
                                    #               XnViewMP

if XnViewMP =="A":
    print "\n\n                                                       XNVIEWMP"
    print "wget http://download.xnview.com/XnViewMP-linux-x64.deb "
    os.system ("wget http://download.xnview.com/XnViewMP-linux-x64.deb ")
    
    print "sudo dpkg -i XnViewMP-linux-x64.deb -qq"
    os.system ("sudo dpkg -i XnViewMP-linux-x64.deb -qq")
    os.system ("clear")
    f=open ("zoznam.txt","a")
    f.write ("XNViewMP \n ")
    f.close
    f=open ("zoznam.txt")
    print f.read ()
    f.close
 
                                    #               XnConvert

if XnConvert =="A":
    print "\n\n                                                       XNCONVERT"
    print "wget http://download.xnview.com/XnConvert-linux-x64.deb "
    os.system ("wget http://download.xnview.com/XnConvert-linux-x64.deb ")
    print "sudo dpkg -i XnConvert-linux-x64.deb -qq"
    os.system ("sudo dpkg -i XnConvert-linux-x64.deb -qq")
    os.system ("clear")
    f=open ("zoznam.txt","a")
    f.write ("XNConvert \n")
    f.close
    f=open ("zoznam.txt")
    print f.read ()
    f.close
   
                                    #               Subterfuge

if Subterfuge =="A":
    print "\n\n                                                       SUBTERFUGE"
    print "wget https://subterfuge.googlecode.com/files/subterfuge_1.0-1_all.deb "
    os.system ("wget https://subterfuge.googlecode.com/files/subterfuge_1.0-1_all.deb ")
    print "sudo dpkg -i subterfuge_1.0-1_all.deb"
    os.system ("sudo dpkg -i subterfuge_1.0-1_all.deb -y -qq")
    print "sudo apt-get -f install -y -qq"
    os.system ("sudo apt-get -f install -y -qq")
    os.system ("clear")
    f=open ("zoznam.txt","a")
    f.write ("Subterfuge \n")
    f.close
    f=open ("zoznam.txt")
    print f.read ()
    f.close
   
                                    #               Kamery
    
if Kamery =="A":
    print "\n\n                                                       Kamery"
    print "sudo aptitude install gstreamer1.0-libav -y -qq"
    os.system ("sudo aptitude install gstreamer1.0-libav -y -q")
    os.system ("clear")
    f=open ("zoznam.txt","a")
    f.write ("Kamery \n ")
    f.close
    f=open ("zoznam.txt")
    print f.read ()
    f.close
    
                                #               Android-tools
if Android =="A":
    print "\n\n                                                     Android-tools"
    print "sudo apt-get install android-tools-adb"
    os.system ("sudo apt-get install android-tools-adb")
    print "sudo apt-get install android-tools-fastboot"
    os.system ("sudo apt-get install android-tools-fastboot")
    os.system ("clear")
    f=open ("zoznam.txt","a")
    f.write ("Nastroje pre android \n")
    f.close
    f=open ("zoznam.txt")
    print f.read ()
    f.close
    
                                #               Handbrake
if Handbrake =="A":
    print "\n\n                                                     Handbrake"
    print "sudo apt-get install handbrake -y -qq"
    os.system ("sudo apt-get install handbrake -y -qq")
    os.system ("clear")
    f=open ("zoznam.txt","a")
    f.write ("Handbrake\n")
    f.close
    f=open ("zoznam.txt")
    print f.read ()
    f.close
    
                                #               Win USB
if Win_usb =="A":
    print "\n\n                                                     Win USB"
    print "sudo wget https://launchpad.net/~colingille/+archive/freshlight/+files/winusb_1.0.11+saucy1_amd64.deb"
    os.system ("sudo wget https://launchpad.net/~colingille/+archive/freshlight/+files/winusb_1.0.11+saucy1_amd64.deb")
    print "sudo dpkg -i winusb*"
    os.system ("sudo dpkg -i winusb*")
    os.system ("clear")
    f=open ("zoznam.txt","a")
    f.write ("Win USB \n ")
    f.close
    f=open ("zoznam.txt")
    print f.read ()
    f.close
                                                            
                                                                                            #               Flashtools
if Flashtools =="A":
    print "\n\n                                                     Flashtools"
    print "wget https://launchpad.net/~trebelnik-stefina/+archive/myppa/+build/4270030/+files/flashtool-xperia_0.9.10.1-2~raring_all.deb"
    os.system ("wget https://launchpad.net/~trebelnik-stefina/+archive/myppa/+build/4270030/+files/flashtool-xperia_0.9.10.1-2~raring_all.deb")
    print "sudo dpkg -i flashtool-xperia_0.9.10.1-2~raring_all.deb"
    os.system ("sudo dpkg -i flashtool-xperia_0.9.10.1-2~raring_all.deb")
    os.system ("clear")
    f=open ("zoznam.txt","a")
    f.write ("Flash Tools - Xperia \n ")
    f.close
    f=open ("zoznam.txt")
    print f.read ()
    f.close

                                                                                            #               Filezilla
if Filezilla =="A":
    print "\n\n                                                     Filezilla"
    print "sudo apt-get install filezilla -y"
    os.system ("sudo apt-get install filezilla -y")  
    os.system ("clear")
    f=open ("zoznam.txt","a")
    f.write ("Fillezilla \n ")
    f.close
    f=open ("zoznam.txt")
    print f.read ()
    f.close
                                                            
                                                                                             #               Gimp                                                                                                                                                                              #               Filezilla
if Gimp =="A":
    print "\n\n                                                     Gimp"
    print "sudo apt-get install gimp -y"
    os.system ("sudo apt-get install gimp -y")  
    os.system ("clear")
    f=open ("zoznam.txt","a")
    f.write ("Gimp \n ")
    f.close
    f=open ("zoznam.txt")
    print f.read ()
    f.close
                                                            
                                                                                        #adobe flash Player
if adobe=="A":
    print "n/n/                                                     Adobe Flash player n/"
    print "sudo apt-get install flashplugin-installer"
    os.system ("sudo apt-get install flashplugin-installer")
    os.system ("clear")
    f=open ("zoznam.txt","a")
    f.write ("Adobe Flash Player \n ")
    f.close
    f=open ("zoznam.txt")
    print f.read ()
    f.close
                                                            
                                                                                    #TOR
if Tor =="A":
    print "\n\n                                                      TOR / TOR BROWSER"
    print "sudo apt-get install tor -y -qq"
    os.system ("sudo apt-get install tor -y -qq")
    print "sudo apt-get install tor-browser -y -qq"
    os.system ("sudo apt-get install tor-browser -y -qq")
    f=open ("zoznam.txt","a")
    f.write ("TOR \n")
    f.close
    f=open ("zoznam.txt")
    print f.read ()
    f.close
    
    
                                                                                        #Viber
if Viber =="A":
    print "\n\n                                                      Viber"
    print "sudo wget http://download.cdn.viber.com/cdn/desktop/Linux/viber.deb"
    os.system ("sudo wget http://download.cdn.viber.com/cdn/desktop/Linux/viber.deb")
    print "sudo dpkg -i viber.deb"
    os.system ("sudo dpkg -i viber.deb")
    f=open ("zoznam.txt","a")
    f.write ("Viber\n")
    f.close
    f=open ("zoznam.txt")
    print f.read ()
    f.close


                                                                                        #Hlasky
#if Hlasky =="A":
#    print "\n\n                                                      Hlasky"
#    os.system ("cd /var/crash")
#    os.system ("sudo rm  *.crash")
#    f=open ("/etc/default/apport","w")
#    text = """
    # set this to 0 to disable apport, or to 1 to enable it
    # you can temporarily override this with
    # sudo service apport start force_start=1
#    enabled=0
#    """
#    with open(SOUBOR,mode="w") as f:
 #       print(text,and="",file=f)
##########################################################GAMES################################

                                                            #DOOM
if DOOM =="A":
    print "\n\n                                                       Inštalujem DOOM"
    print "sudo apt-get install freedoom -y"
    os.system ("sudo apt-get install freedoom -y")
    os.system ("clear")
    f=open ("zoznam.txt","a")
    f.write ("HRY: \n\
            DOOM\n")
    f.close
    f=open ("zoznam.txt")
    print f.read ()
    f.close

                                                            #Silent Hunter
if Silent_Hunter =="A":
    print "\n\n                                                       Inštalujem Silent Hunter Linux"
    print "sudo add-apt-repository ppa:baegirxx-googlemail/dftd-latest -y"
    os.system ("sudo add-apt-repository ppa:baegirxx-googlemail/dftd-latest -y") 
    print "sudo apt-get install dangerdeep -y -qq"
    os.system ("sudo apt-get install dangerdeep -y -qq")
    os.system ("clear")
    f=open ("zoznam.txt","a")
    f.write ("          Silent Hunter \n ")
    f.close
    f=open ("zoznam.txt")
    print f.read ()
    f.close                                
#########################Záver################################
print "sudo apt-get -f install -y -qq"
os.system ("sudo apt-get -f install -y -qq")
print "sudo apt-get update -qq"
os.system ("sudo apt-get update -qq")
print"sudo apt-get upgrade -qq"
os.system ("sudo apt-get upgrade -qq")
print "sudo apt-get dist-upgrade -qq"
os.system ("sudo apt-get dist-upgrade -qq")
print "sudo apt-get autoremove -y -qq"
os.system ("sudo apt-get autoremove -y -qq")
if rm =="A":   
    print "rm divxconverter_2.0.1-1_all.deb"
    os.system ("rm divxconverter_2.0.1-1_all.deb")
    print "rm google-earth-stable_current_i386.deb"
    os.system ("rm google-earth-stable_current_i386.deb")
    print ("rm winusb*")
    print "rm install-depot-multisystem.sh.tar"
    os.system ("rm install-depot-multisystem.sh.tar")
    os.system ("rm master")
    print"rm subterfuge_1.0-1_all.deb"
    os.system ("rm master.1")
    print "rm -r slowloris.pl-master/"
    os.system ("rm -r slowloris.pl-master/")
    print "rm teamviewer_linux.deb"
    os.system ("rm teamviewer_linux.deb")
    print "rm aktualizacia"
    os.system ("rm aktualizacia")
    os.system ("clear")
    print "rm zoznam.txt"
    f=open ("zoznam.txt","a")
    f.write ("\n\n\ Vytvorené skripty:\n\
                        Aktuailzácia ----- update,upgrade,dist-upgrade,autoremove, reboot\n\
                        Slowloris\n ")
    f.close
    f=open ("zoznam.txt")
    print f.read ()
    f.close
    os.system ("rm zoznam.txt")
    print "rm repository.py"
    os.system ("rm repository.py")
    print "rm XnConvert-linux-x64.deb"
    os.system ("rm XnConvert-linux-x64.deb")
    print "rm XnViewMP-linux-x64.deb"
    os.system ("rm XnViewMP-linux-x64.deb")


print "\n\n\n\n\n\n\n                       Production on PRIWI\n\
                                V prípade problemou pri instalacii nevahajte pisať na\
                                          peterpriwitzer@gmail.com\
                                                                                           Koniec\
                                                                                                   :D "