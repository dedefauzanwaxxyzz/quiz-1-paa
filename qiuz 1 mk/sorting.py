import time

# Pengurutan dengan Bubble Sort
def pengurutan_bubble(data):
    n = len(data)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if data[j] > data[j + 1]:  # Mengurutkan secara ascending
                data[j], data[j + 1] = data[j + 1], data[j]
    return data

# Pengurutan dengan Quick Sort
def pengurutan_quick(data):
    if len(data) <= 1:
        return data
    pivot = data[len(data) // 2]
    kiri = [x for x in data if x < pivot]
    tengah = [x for x in data if x == pivot]
    kanan = [x for x in data if x > pivot]
    return pengurutan_quick(kiri) + tengah + pengurutan_quick(kanan)

# Fungsi untuk mengukur waktu eksekusi program
def ukur_waktu(fungsi_pengurutan, data):
    waktu_mulai = time.time()
    data_terurut = fungsi_pengurutan(data)
    waktu_selesai = time.time()
    return data_terurut, waktu_selesai - waktu_mulai

# Analisis efisiensi
def analisis_efisiensi(label, waktu_bubble, waktu_quick):
    if waktu_bubble < waktu_quick:
        efisien = "Bubble Sort lebih efisien untuk " + label
    elif waktu_quick < waktu_bubble:
        efisien = "Quick Sort lebih efisien untuk " + label
    else:
        efisien = "Kedua metode sama efisien untuk " + label
    return efisien

# Data input untuk Kelas A dan Kelas B
kelas_a = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
kelas_b = [0, 1, 2, 3, 4, 8, 7, 6, 5]

# Mengukur dan menampilkan hasil
for label, data in [("Kelas A", kelas_a), ("Kelas B", kelas_b)]:
    hasil_bubble, waktu_bubble = ukur_waktu(pengurutan_bubble, data[:])  # Salin data agar tidak terpengaruh
    hasil_quick, waktu_quick = ukur_waktu(pengurutan_quick, data[:])    

    # Cetak hasil
    print(f"{label}:")
    print(f"  Data Asli: {data}")
    print(f"  Hasil Bubble Sort: {hasil_bubble}")
    print(f"  Waktu Bubble Sort: {waktu_bubble:.8f} detik")
    print(f"  Hasil Quick Sort: {hasil_quick}")
    print(f"  Waktu Quick Sort: {waktu_quick:.8f} detik")
    
    # Cetak analisis efisiensi
    print(f"  Analisis: {analisis_efisiensi(label, waktu_bubble, waktu_quick)}\n")