# Deklarasi array untuk menyimpan angka
angka = []

# Meminta input penguna
for i in range(5):
    elemen = int(input(f"Masukan angka ke-{i+1}: "))
    angka.append(elelmen)

# Menghitung frekuensi kemunculan
frekuensi = {}
for elemen in angka:
    if elemen in frekuensi:
        frekuensi[elemen] += 1
    else:
        frekuensi[elemen] = 1

# Menampilkan hasil
for elemen, jumlah in frekuensi.items():
    print(f"Angka {elemen} muncul sebanyak {jumlah} kali.")