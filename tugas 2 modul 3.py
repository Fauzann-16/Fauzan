# Input nilai ujian dan absensi
nilai_ujian = float(input("Masukkan Nilai Ujian: "))
absensi = float(input("Masukkan Persentase Absensi: "))

# Memeriksa kelulusan berdasarkan nilai ujian
if nilai_ujian >= 75:
    # Jika nilai ujian >= 75, periksa absensi
    if absensi >= 75:
        print("Mahasiswa dinyatakan Lulus.")
    else:
        print("Mahasiswa dinyatakan Tidak Lulus karena absensi kurang dari 75%.")
elif 60 <= nilai_ujian < 75:
    # Jika nilai ujian antara 60 dan 75, periksa absensi
    if absensi >= 75:
        print("Mahasiswa dinyatakan Lulus dengan catatan.")
    else:
        print("Mahasiswa dinyatakan Tidak Lulus karena nilai dan absensi tidak memenuhi syarat.")
else:
    # Jika nilai ujian < 60
    print("Mahasiswa dinyatakan Tidak Lulus karena nilai ujian kurang dari 60.")