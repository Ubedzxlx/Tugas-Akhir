import csv

def soal_pilihan_ganda():
    nilai = 0
    nomer_soal = 1

    with open('Tugas Akhir semester 2/project/soal.csv', mode='r') as buat_soal:
        csvFile = csv.reader(buat_soal)
        next(csvFile)  # Skip header

        for line in csvFile:
            soal = line[1]
            pilihan = line[2:5]
            jawaban_benar = line[5]

            print(f"Soal ke-{nomer_soal} : {soal}")
            print(f"A. {pilihan[0]}")
            print(f"B. {pilihan[1]}")
            print(f"C. {pilihan[2]}")

            jawaban_user = input("Jawaban Anda (A/B/C) : ").upper()

            if jawaban_user == jawaban_benar:
                nilai += 10
                print("Jawaban benar!")
            else:
                print("Jawaban salah!")
                
            # nomor soal untuk soal berikutnya    
            nomer_soal +=1

    print(f"Nilai akhir Anda: {nilai}")

soal_pilihan_ganda()
