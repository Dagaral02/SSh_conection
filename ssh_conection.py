#!/usr/bin/env python3

import subprocess
import os

me = subprocess.getoutput("whoami")
me = me.strip()

print("Hola,vamos a hacer una conexion remota para ejecutar los comandos que desees")

print("1. Ejecutar un comando") 
print("2. Copiar un archivo ")

op = input("Que desea realizar: ")

if(op == '1'):
    user = input("Dinos el usuario del equipo: ")
    ip = input("Dinos la ip del servidor: ")
    puerto = input("Dinos el puerto: ")
    command = input("Que comando quieres realizar: ")

    print("Va a realizarlo por Key o por contraseña")
    print("1. Key")
    print("2. Contraseña")

    key = input("Respuesta: ")

    if(key == '1'):
        sshcopy = input("Importante esta copiada tu clave publica en el servidor Usuario: ")
        if(sshcopy == 'si'):
            lugarpriv =input ("Indica la ruta completa donde se encuentra la Key: " ) 
            os.system(f"ssh -i {lugarpriv} -p {puerto} {user}@{ip} {command}")
        elif(sshcopy == 'no'):
            lugarpub =input ("Indica la ruta completa donde se encuentra la Key: ")
            os.system(f"ssh-copy-id -f -i {lugarpub} {user}@{ip}")
            lugarpriv =input ("Indica la ruta completa donde se encuentra la Key: " )
            os.system(f"ssh -i {lugarpriv} -p {puerto} {user}@{ip} {command}") 
    elif(key == '2'):
        os.system(f"ssh {user}@{ip} {command}")
elif(op == '2'):
    
    user = input("Dinos el usuario del equipo: ")
    ip = input("Dinos la ip del servidor: ")

    sshcopy = input("Importante esta copiada tu clave publica en el servidor, ¡Usuario!: ")

    if(sshcopy == 'si'):
        ls = input('Quieres hacer un ls en .ssh por si no te acuerdas de la Key: ')
        if(ls == 'si'):
            os.system(f'ls /home/{me}/.ssh')
            lugarpriv =input ("Indica la ruta completa donde se encuentra la Key: " )
            archcp = input ('Cual es la ruta incluida el archibo que quieres copiar: ')
            wherecp = input ('Donde quieres poner el archivo que quieres copiar (pon la ruta entera): ')
            os.system(f"scp -i {lugarpriv} {archcp} {user}@{ip}:{wherecp}")
        elif(ls == 'no'):
            lugarpriv =input ("Indica la ruta completa donde se encuentra la Key: " )
            archcp = input ('Cual es la ruta incluida el archibo que quieres copiar: ')
            wherecp = input ('Donde quieres poner el archivo que quieres copiar (pon l aruta entera): ')
            os.system(f"scp -i {lugarpriv} {archcp} {user}@{ip}:{wherecp}") 
    elif(sshcopy == 'no'): 
        ls = input('Quieres hacer un ls en .ssh por si no te acuerdas de la Key: ')
        if(ls == 'si'):
            os.system(f'ls /home/{me}/.ssh')
            lugarpub =input ("Indica la ruta completa donde se encuentra la Key: ")
            os.system(f"ssh-copy-id -f -i {lugarpub} {user}@{ip}")
            lugarpriv =input ("Indica la ruta completa donde se encuentra la Key: " )
            archcp = input ('Cual es la ruta incluida el archibo que quieres copiar: ')
            wherecp = input ('Donde quieres poner el archivo que quieres copiar (pon l aruta entera): ')
            os.system(f"scp -i {lugarpriv} {archcp} {user}@{ip}:{wherecp}")
        elif(ls == 'no'):
            lugarpriv =input ("Indica la ruta completa donde se encuentra la Key: " )
            archcp = input ('Cual es la ruta incluida el archibo que quieres copiar: ')
            wherecp = input ('Donde quieres poner el archivo que quieres copiar (pon l aruta entera): ')
            os.system(f"scp -i {lugarpriv} {archcp} {user}@{ip}:{wherecp}")
    