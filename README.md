NAMA:DEDE FAUZAN
NIM:f5512089

analisis quiz 2
Pendekatan naif seperti **Bubble Sort** memiliki **best case** ketika data sudah terurut sepenuhnya. Namun, meskipun tidak ada elemen yang perlu ditukar, algoritma tetap menjalankan semua iterasi untuk memastikan urutan data, sehingga kompleksitas waktu tetap **O(n²)**. Ini menunjukkan bahwa Bubble Sort kurang efisien bahkan dalam best case, karena tidak memiliki mekanisme untuk mendeteksi bahwa array sudah terurut dan menghentikan proses lebih awal.
Pendekatan **conquer**, seperti pada **Merge Sort**, memiliki kompleksitas waktu **O(n log n)** di semua kasus, termasuk best case. Pada **best case** (ketika data sudah terurut), algoritma tetap membagi array menjadi sub-array kecil hingga elemen tunggal, lalu menggabungkannya kembali dalam urutan yang benar. Karena proses pembagian dan penggabungan tidak dipengaruhi oleh urutan awal data, waktu eksekusi tetap konsisten. Keunggulan metode conquer adalah efisiensinya yang tinggi untuk dataset besar, meskipun memerlukan ruang memori tambahan untuk penggabungan.
