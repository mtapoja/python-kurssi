#!/usr/bin/python3

# Kysy nimet
etunimi = input("Anna etunimesi: ")
sukunimi = input("Anna sukunimesi: ")

print("Koko nimesi on %s %s\n\n" % (etunimi, sukunimi))

print("Etunimesi pituus on:  %d" % len(etunimi))
print("Sukunimesi pituus on: %d" % len(sukunimi))
print("Nimessäsi on %d kirjainta" % (len(etunimi) + len(sukunimi)))

print("-- sen pituinen se --")
