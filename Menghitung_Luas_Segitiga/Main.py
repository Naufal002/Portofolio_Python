# Import OS from package python
import os
os.system('cls')

   
    # HEADER
def header():
    '''HEADER HERE'''
    print(f"{'Menghitung luas segitiga menggunakan python':^40}")
    print(f"{'-'*40:^40}")
    

    # INPUT USER
def input_user():
    '''INPUT USER HERE'''
        # Input Alas
    a = float(input("Masukkan Alas: "))

        # Input Tinggi
    t = float(input("Masukkan tinggi: "))
    return a,t

    # COUNT HERE
def count(alas: int, tinggi: int)-> int:
    var = alas*tinggi
    return(1/2 * var)



while True:
    header()

    ALAS,TINGGI = input_user()

    total = count(ALAS,TINGGI)
    print(f"Luas Segitiga adalah: {total}")


    print("\n")
    print("© 2022 Naufal Rizqi Ilham Gibran")
    isLanjut = str(input("Lanjut (y/n): "))

    if isLanjut == 'n' or isLanjut == 'n':
        break

    
    elif isLanjut == 'y' or isLanjut == 'Y':
        print("\n")
        continue


    else:
        print("--Command Failed!--")
        break




''' 

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

'''
