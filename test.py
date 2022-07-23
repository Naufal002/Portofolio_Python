import os  
os.system('cls')


angka = int(20)

def fnc(ubah_angka):
    global angka
    angka = ubah_angka

    return angka

fnc(10)
print(angka)