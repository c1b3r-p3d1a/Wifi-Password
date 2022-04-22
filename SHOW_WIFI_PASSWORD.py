import os
import subprocess
import time

def _header_():
	print (r"""
    cccc   i   bbbb    eeeeee   rrrrrrr
   cc      i   b   b   eeeeee   rr   rrr
   cc      i   b b     eee      rrrrrrr     ------   P3d1A
   cc      i   b   b   eeeeee   rr rrrr
    cccc   i   bbbb    eeeeee   rr  rrr                                                                   """)

_header_()
print("\n")

data = subprocess.check_output(['netsh', 'wlan', 'show', 'profile']).decode('utf-8').split('\n')
profiles = [i.split(":")[1][1:-1] for i in data if "Perfil de todos los usuarios" in i]

print("{:<30}| {:<}".format("RED WIFI", "CONTRASEÑA", "SEGURIDAD"))

for i in profiles:
    results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key=clear']).decode('utf-8', 'ignore').split('\n')
    results = [a.split(":")[1][1:-1] for a in results if "Contenido de la clave" in a]
    try:
        print("{:<30}| {:<}".format(i, results[0]))
    except IndexError:
        print("{:<30}| {:<}".format(1, ""))
input('[+] Presione cualquier tecla para salir...')
print('[-] Saliendo...')
time.sleep(.5)