def daftar_barang():
    print("------------------------------")
    print("|NO| NAMA BARANG  |   HARGA  |")
    print("------------------------------")
    print("|1 |MIE INSTAN    |Rp.5.000  |")
    print("|2 |BERAS         |Rp.50.000 |")
    print("|3 |SAUS TOMAT    |Rp.15.000 |")
    print("|4 |KECAP MANIS   |Rp.7.000  |")
    print("|5 |TEPUNG TERIGU |Rp.11.000 |")
    print("|6 |SABUN MANDI   |Rp.6.000  |")
    print("|7 |SHAMPOO       |Rp.4.000  |")
    print("|8 |LILIN         |Rp.10.000 |")
    print("|9 |GULA AREN     |Rp.13.000 |")
    print("|10|PASTA GIGI    |Rp.8.000  |")
    print("------------------------------")

import csv

def beli():
    daftar_barang()
    
    total_pembelian = 0

    while True:
        nomor_barang = int(input("Masukkan nomor barang yang ingin dibeli: "))
        
        if nomor_barang < 1 or nomor_barang > 10:
            print("Nomor barang tidak valid. Silakan coba lagi.")
            continue

        with open('Tugas Akhir semester 2/project/kasir.csv', mode='r') as file:
            reader = csv.reader(file)
            header = next(reader)

            for row in reader:
                if int(row[0]) == nomor_barang:
                    menu = row[1]
                    harga_awal = int(row[2])
                    break

        jumlah_barang = int(input(f"Masukkan jumlah {menu}: "))
        total_harga = jumlah_barang * harga_awal
        total_pembelian += total_harga

        print(f"{menu}, {jumlah_barang} buah, Rp.{total_harga}")

        lanjut_belanja = input("Apakah ingin membeli lagi? (y/t): ")
        if lanjut_belanja != 'y':
            print(f"Total Pembelian: Rp.{total_pembelian}")
            while True:
                bayar = int(input("Masukan Pembayaran Anda :"))
                if bayar >= total_pembelian:
                    kembalian = bayar - total_pembelian
                    print(f"Kembalian Anda Sebesar Rp.{kembalian}")
                    break
                elif bayar == total_pembelian:
                    print("Uang yang anda bayar Pas, Tidak ada Kembalian!")
                    break
                else:
                    print("Uang anda bayar kurang ,Silakan masukkan jumlah uang yang mencukupi.")
            break

beli()
