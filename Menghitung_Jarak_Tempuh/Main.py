# Import OS from package python
import os 
os.system('cls')

'''
    S = V x T
'''
    # FUNTION HERE 
# ============================================
    # Header
def header():
    print(f"{'Menghitung Jarak Tempuh':^40}")
    print(f"{'Menggunakan PYTHON':^40}")
    print(f"{'-'*18 :^40}")

    # Input User
def input_user():
    v = int(input("Enter VELOCITY (km/h): "))
    t = int(input("Enter TIME (h): "))
    return v,t

    # Count
def count(kecepatan: int, waktu: int)-> int:
    return (kecepatan*waktu)
    
# ==========================================

# to call funtion and input conditional
while True:
    header()

    VELOCITY,TIME = input_user()
    HASIL = count(VELOCITY,TIME)

    print('='*17)
    print(f"Distance: {HASIL}")
    

    print("\n")
    print("© 2022 Naufal Rizqi Ilham Gibran")
    isLanjut = str(input("Lanjut (y/n): "))

    # Conditional
    if isLanjut == 'n' or isLanjut == 'N':
        break


    elif isLanjut == 'y' or isLanjut == 'Y':
        print("\n")
        continue


    else:
        print("--Command Failed--")
        break