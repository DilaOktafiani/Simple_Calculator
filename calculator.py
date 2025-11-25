def tambah (a, b):
    return a + b

def kurang (a, b):
    return a - b

def kali (a, b):
    return a * b

def bagi (a, b):
    return a / b

print("===========================")
print("==== Simple Kalkulator ====")
print("===========================\n")

print("Pilih Operasi: ")
print("1. Penjumlahan")
print("2. Pengurangan")
print("3. Perkalian")
print("4. Pembagian\n")

pilihan = input("Masukkan Pilihan Operasi (1/2/3/4): ")
angka1 = float (input("Masukkan Angka Pertama: "))
angka2 = float (input("Masukkan Angka Kedua: "))

if pilihan == "1":
    print("\nHasil: ", tambah(angka1, angka2))

elif pilihan == "2":
    print("\nHasil: ", kurang(angka1, angka2))

elif pilihan == "3":
    print("\nHasil: ", kali(angka1, angka2))

elif pilihan == "4":
    if angka2 != 0:
        print("\nHasil: ", bagi(angka1, angka2))
    else:
        print("\nERROR: Tidak bisa membagi dengan NOL!")

else:
    print("\nPilihan Operasi Tidak Valid!")

