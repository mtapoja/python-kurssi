# Kappale 5.1.1

teksti = "merkkijono"
kokonaisluku = 123
liukuluku = 3.141592653
onkoTotta = True

print("Tekstimuuttujan arvo on " + str(teksti))
print("Kokonaislukumuuttujan arvo on " + str(kokonaisluku))
print("Liukulukumuuttujan arvo on " + str(liukuluku))
print("Totuusarvomuuttujan arvo on " + str(onkoTotta))

# Parempi tapa printata
print("\nParempi tapa:")
print("Tekstimuuttujan arvo on %s" % teksti)
print("Kokonaislukumuuttujan arvo on %i" % kokonaisluku)
print("Liukulukumuuttujan arvo on %.6f" % liukuluku)
print("Totuusarvomuuttujan arvo on %s" % str(onkoTotta))

# Uusin tapa printata: https://www.python.org/dev/peps/pep-3101/
print("\nUusin tapa:")
print("Tekstimuuttujan arvo on {0}".format(teksti))
print("Kokonaislukumuuttujan arvo on {0}".format(kokonaisluku))
print("Liukulukumuuttujan arvo on {0}".format(liukuluku))
print("Totuusarvomuuttujan arvo on {0}".format(onkoTotta))
print("\nYhdellä rivillä: txt={0}, kok={1}, liuku={2} ja totuus={3}"
      .format(teksti, kokonaisluku, liukuluku, onkoTotta))
