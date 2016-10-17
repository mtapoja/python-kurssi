# Kappale 4.1.2

pienet_aakkoset = "abcdefghijklmnopqrstuvwxyzåäö"

isot_aakkoset = ""
aakkosarvo = 65
skandiarvot = [197, 196, 214]

# Kirjaimet A..Z
while (aakkosarvo < 91):
    isot_aakkoset = isot_aakkoset + chr(aakkosarvo)
    aakkosarvo = aakkosarvo + 1

# Kirjaimet Å, Ä, Ö
for aakkosarvo in skandiarvot:
	isot_aakkoset = isot_aakkoset + chr(aakkosarvo)

print(pienet_aakkoset)
print(isot_aakkoset)
