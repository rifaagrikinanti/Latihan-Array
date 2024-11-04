# Deklarasi matriks pertama dan kedua
matriks1 = []
matriks2 = []

# Meminta input untuk matriks pertama
print("Masukan elemen untuk matriks pertama:")
for i in range(2):
    baris = []
    for j in range(2):
        nilai = int(input(f"Masukan elemen baris {i+1}, kolom {j+1}: "))
        baris.append(nilai)
    matriks1.append(baris)

# Meminta input untuk metriks kedua
print("\nMasukan elemen untuk metriks kedua:")
for i in range(2):
    baris = []
    for j in range(2):
        nilai = int(input(f"Masukan elemen baris {i+1}, kolom {j+1}: "))
        baris.append(nilai)
    matriks2.append(baris)

# Penjualan matriks
hasil = []
for i in range(2):
    baris = []
    for j in range(2):
        baris.append(matriks1[i][j] + matriks2[i][j])
    hasil.append(baris)

# Menampilkan hasil penjumlahan
print("\nHasil penjumlahan matriks:")
for baris in hasil:
    print(baris)