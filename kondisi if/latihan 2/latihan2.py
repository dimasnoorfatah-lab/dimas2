# Program Mengurutkan Data dari Terkecil ke Terbesar

print("Program Mengurutkan Data")

# Input tiga bilangan (bisa ditambah jika mau)
bil1 = int(input("Bilangan ke-1 : "))
bil2 = int(input("Bilangan ke-2 :  "))
bil3 = int(input("Bilangan ke-3 :  "))

# Masukkan bilangan ke dalam list
bilangan = [bil1, bil2, bil3]

# Urutkan dari yang terkecil ke terbesar
bilangan.sort()

# Tampilkan hasil urutan
print("Urutan bilangan mulai dari terkecil:", *bilangan)
# program selesai 
# latihan2.py
