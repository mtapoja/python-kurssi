#!/usr/bin/python3

# Kysy Fibonaccin sarjan pituus
lukumaara = int(input("Kuinka monta Fibonaccin lukua laitetaan: "))

print("Fiboja %d\n" % lukumaara)

eded_fibo = 0
ed_fibo = 1
fibo = 1

print(ed_fibo)

while (lukumaara > 1):
    print(fibo)
    lukumaara = lukumaara - 1
    eded_fibo = ed_fibo
    ed_fibo = fibo
    fibo = eded_fibo + ed_fibo
