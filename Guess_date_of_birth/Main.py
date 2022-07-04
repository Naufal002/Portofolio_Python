#Library
import os 
os.system('cls')
import datetime as dt
import calendar as kalender


def header():
    print(f"{'Tebak umur kamu':^40}")
    print(f"{'Menggunakan Python':^40}")
    print(f"{'-'*40:^40}")


while True:
    header()

    #DateTime
    hari_ini = dt.date.today()
    print("\n")
    print(hari_ini, "\n")
    print("="*22)
    print(f"hari ini adalah: {hari_ini:%A}\n")

    #Kalender
    year = 2021
    month = 1
    print(kalender.month(year, month))

    #Tanggal Lahir
    print("="*22)
    tanggal = int(input("Tanggal: "))
    bulan = int(input("Bulan: ")) # Masukkan bulan menggunakan tipe data INT misalnya januari berarti bulan 01
    tahun = int(input("Tahun: "))

    print("="*22)

    tanggal_lahir = dt.date(tahun, bulan, tanggal)
    print(f"Tanggal lahir Anda: {tanggal_lahir}")
    print(f"Anda lahir pada hari: {tanggal_lahir:%A}")

    umur_hari = hari_ini - tanggal_lahir
    umur_tahun = umur_hari.days // 365
    print(f"Umur anda adalah: {umur_tahun} tahun")
    print("="*22)
    
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