jenis_kelamin = input("Jenis Kelamin (Laki-laki/Perempuan): ")
berat_badan = int(input("Berat Badan (kg): "))
tinggi_badan = int(input("Tinggi Badan (cm): "))
usia = int(input("Usia: "))
nilai_akademis = int(input("Nilai Akademis: "))
memiliki_skill = input("Apakah Anda memiliki skill menembak, memanah, atau berkuda? (Ya/Tidak): ")
memiliki_cacat_tubuh = input("Apakah Anda memiliki anggota tubuh yang cacat? (Ya/Tidak): ")

kelayakan = False

if memiliki_cacat_tubuh.lower() == "tidak":
    if jenis_kelamin.lower() == "perempuan":
        if 45 <= berat_badan <= 50 and tinggi_badan >= 165 and usia < 20:
            kelayakan = True
    elif jenis_kelamin.lower() == "laki-laki":
        if berat_badan <= 70 and tinggi_badan >= 170 and usia <= 25:
            kelayakan = True
    else:  
        if nilai_akademis >= 90 and usia < 30:
            kelayakan = True
    if memiliki_skill.lower() == "ya":
        kelayakan = True

if kelayakan:
    print("Selamat! Anda layak menjadi anggota Organisasi X.")
else:
    print("Maaf, Anda tidak memenuhi kriteria untuk menjadi anggota Organisasi X.")
