#!/usr/bin/python3

# http://planzero.org/blog/2012/01/26/system_uptime_in_python,_a_better_way
import os
from datetime import timedelta

print("Tämä on pääohjelma. Yksinkertainen, luokaton, suoraviivainen.")

# Tarkista järjestelmän uptime, eli kauanko järjestelmä on ollut pystyssä
print('\nUptime /proc/uptime -tiedostosta:')
with open('/proc/uptime',  'r') as tiedosto:
    uptime_sekunnit = float(tiedosto.readline().split()[0])
    uptime_merkkijono = str(timedelta(seconds = uptime_sekunnit))

print(uptime_merkkijono)

# Järjestelmän uptime käyttäen uptime-komentoa
print('\nUptime, käyttäen uptime-komentoa:')
os.system('uptime')
