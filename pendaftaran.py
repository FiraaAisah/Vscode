nama = input("Nama: ")
tempat_lahir = input("Tempat Lahir: ")
tanggal_lahir = int(input("Tanggal Lahir (contoh: 23): "))
tahun_lahir = int(input("Tahun Lahir (contoh: 2000): "))
nilai_english = int(input("Nilai Bahasa Inggris: "))
nilai_mtk = int(input("Nilai Matematika: "))
nilai_indonesia = int(input("Nilai Bahasa Indonesia: "))
jenis_kelamin = input("Jenis Kelamin (Laki-laki/Perempuan): ")

rata_nilai = (nilai_english + nilai_mtk + nilai_indonesia) / 3

from datetime import date
today = date.today()
usia = today.year - tahun_lahir

if rata_nilai >= 80:
    if jenis_kelamin.lower() == "laki-laki":
        jurusan = "Teknik Informatika"
    elif jenis_kelamin.lower() == "perempuan":
        jurusan = "Sistem Informasi"
else:
    jurusan = "DKV"

if rata_nilai >= 80 and usia < 25:
    print("Selamat! Anda diterima di jurusan", jurusan)
else:
    print("Maaf, Anda tidak memenuhi syarat untuk pendaftaran.")

