#!/usr/bin/python3

# Sijoita muuttujiin arvot: etunimet on listamuuttuja, sukunimi on
# merkkijonomuuttuja
etunimet = ["Marjo", "Mika", "Ursula", "Urho"]
sukunimi = "Tapojärvi"

# Tee toisto for-lauseella ja merkkijonoilla
for yksi_nimi in etunimet:
    print("nimi: %s %s" % (yksi_nimi, sukunimi))

print("-- loppu --")
