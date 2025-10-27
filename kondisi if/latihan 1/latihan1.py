print("Menentukan angka terbesar dari empat angka yang diinputkan.")

a = int(input("Angka pertama: "))
b = int(input("Angka kedua: "))
c = int(input("Angka ketiga: "))
d = int(input("Angka keempat: "))

angkaTerbesar = a
if b > angkaTerbesar:
    angkaTerbesar = b
if c > angkaTerbesar:
    angkaTerbesar = c
if d > angkaTerbesar:
    angkaTerbesar = d

print("Angka", angkaTerbesar, "adalah yang terbesar dari keempat angka tersebut.")