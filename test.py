import os 
os.system('cls')

# Input Alas
alas = float(input("Masukkan Alas: "))

# Input Tinggi
tinggi = float(input("Masukkan tinggi: "))

# Count
luas = (alas*tinggi)
ct = 1/2 * luas
print('Luas Segitiga adalah %0.2f' %ct)