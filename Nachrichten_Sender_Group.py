#Import
import pywhatkit
import PySimpleGUI as sg
import keyboard
import time
import os
import sys

Id: str

#Variabeln
sg.theme("DarkTeal4")
tastatur = keyboard

#Das die .txt File gelöscht wird
if os.path.exists("pywhatkit_dbs.txt"):
    os.remove("pywhatkit_dbs.txt")

def FirstUse():
    global Id
    if os.path.exists("Group_Id.txt"):
        with open("Group_Id.txt", "r") as o:   
            Id = o.read()
            o.close()
        print("Die Id: " + Id)
        Ans = input("Möchtest du die Id benutzen (Ja/Nein): ")
        if "Ja" in Ans:
            os.system("cls")
            main()
        elif "Nein" in Ans:
            Id = input("Die Gruppenid: ")
            with open("Group_Id.txt", "w") as o:
                o.write(Id)
                o.close()
            os.system("cls")
            main()
        else:
            sg.Popup("Keine richtige Angabe!")
            os.system("cls")
    else:
        Id = input("Die Gruppenid: ")
        with open("Group_Id.txt", "w") as o:
            o.write(Id)
            o.close()
        os.system("cls")
        main()


def main():
    #Das eigentliche Script
    print('Hast du dein Handy schon mit Whatsapp Web verbunden. Wenn Nein drück strg und c')
    time.sleep(2)
    message = str(input('Die Nachricht: '))
    h = int(input('Zu welcher Stunde soll die Nachricht ankommen: '))
    m = int(input('Zu welcher Minute soll die Nachricht ankommen: '))
    pywhatkit.sendwhatmsg_to_group(idd, message, h, m)
    time.sleep(1)
    sg.Popup("Done!")
    tastatur.press_and_release("ctrl+w")
try: 
    if __name__ == "__main__":
        FirstUse()
        #Das die .txt File gelöscht wird
        if os.path.exists("pywhatkit_dbs.txt"):
            os.remove("pywhatkit_dbs.txt")
    else:
        sg.Popup("ERROR!")
except KeyboardInterrupt:
    sg.Popup("Unterbrochen!")
    os.system("cls")