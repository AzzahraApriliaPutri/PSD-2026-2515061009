**Program Mencari Harga Barang di Toko**

**Deskripsi Singkat**

Program ini dirancang sebagai sistem pencarian harga pada katalog produk secara digital. Tujuannya adalah untuk membantu pengguna menemukan posisi atau urutan suatu harga barang di dalam daftar yang sudah tersusun rapi. Dengan sistem ini, proses pengecekan harga menjadi jauh lebih cepat dibandingkan harus melihat satu per satu dari awal sampai akhir.

Algoritme yang digunakan dalam kode ini adalah Binary Search (Pencarian Biner). Algoritma ini bekerja dengan langsung mengecek nilai tengah. Jika harga target lebih besar, ia membuang separuh data bagian kiri (murah). Jika lebih kecil, ia membuang separuh data bagian kanan (mahal).


Source Kode

<img width="825" height="540" alt="kode 1 rara" src="https://github.com/user-attachments/assets/619c721b-42b0-45f1-a588-26eb90f3572b" />

<img width="855" height="515" alt="kode 2 rara" src="https://github.com/user-attachments/assets/306246b1-4ecd-40d1-a3ab-ddbcf3eebfd3" />

<img width="782" height="322" alt="Screenshot 2026-05-12 161010" src="https://github.com/user-attachments/assets/e5b470b3-6443-4386-bd30-342c3936fc8f" />

def cari_harga_barang(daftar_harga, n, harga_target):
Mendefinisikan fungsi dengan tiga input: daftar harga (list), jumlah barang (n), dan harga yang ingin dicari (target).

l = 0 dan r = n - 1
Menentukan batas pencarian. l (left) dimulai dari indeks awal, dan r (right) di indeks terakhir.

posisi = -1
Menyiapkan variabel untuk menyimpan hasil. Nilai -1 adalah standar untuk menandakan "belum ditemukan".

while l <= r:
Looping akan terus berjalan selama area pencarian masih ada (batas kiri belum melewati batas kanan).

m = l + (r - l) // 2
Mencari titik tengah (median). Rumus ini digunakan untuk membagi dua daftar harga agar pencarian lebih cepat

if daftar_harga[m] == harga_target:
Kondisi ideal: jika harga di titik tengah pas dengan harga yang dicari, simpan posisinya dan hentikan pencarian (break).

elif daftar_harga[m] < harga_target:
Jika harga di tengah lebih kecil dari target, berarti harga target ada di area yang lebih mahal (sebelah kanan). Maka, batas kiri (l) digeser melewati tengah.

else:
Jika harga di tengah lebih besar dari target, berarti target ada di area yang lebih murah (sebelah kiri). Maka, batas kanan (r) digeser ke sebelum tengah.

return posisi
Mengirimkan hasil akhir (indeks atau -1) kembali ke pemanggil fungsi.

try...except ValueError
Digunakan untuk menangkap error jika pengguna memasukkan huruf, padahal program meminta angka. Ini mencegah program crash.

n = int(input("Masukkan jumlah produk dalam katalog: "))
Mengambil data berapa banyak barang yang akan dimasukkan ke katalog.

for i in range(n):
Melakukan perulangan sebanyak jumlah produk yang ditentukan sebelumnya.

if i > 0 and harga < harga_produk[i-1]:
Logika Krusial: Karena Binary Search wajib menggunakan data terurut, baris ini memastikan pengguna tidak memasukkan harga yang lebih murah dari harga sebelumnya (memaksa input tetap menaik).

harga_produk.append(harga)
Memasukkan harga yang sudah valid ke dalam daftar katalog.

target = int(input("\nMasukkan harga yang ingin dicari: Rp"))
Menanyakan harga barang yang ingin dicari oleh pembeli/pengguna.

hasil = cari_harga_barang(harga_produk, n, target)
Memanggil fungsi utama tadi dan mengirimkan data katalog untuk diproses.

print(f"\nSelesai: Harga Rp{target} ditemukan pada katalog urutan ke-{hasil + 1}.")
Menampilkan lokasi barang. Kita menggunakan + 1 karena manusia menghitung mulai dari 1, sedangkan komputer mulai dari 0.


**Output**

<img width="530" height="365" alt="output rara" src="https://github.com/user-attachments/assets/88a9524f-e10d-43f6-aae5-1c0f93780a73" />

Berdasarkan output program ini adalah user akan diminta untuk input katalog. Di dalam program menginputkan 5 data harga barang yang disusun dari harga terkecil. Kemudian user memasukkan harga yang akan di cek posisinya yaitu =  37000
Maka Algoritme tidak mengecek satu per satu dari awal, melainkan membelah daftar menjadi dua bagian:

Langkah 1 (Mengecek Tengah):

Program langsung melihat ke indeks 2 (nilai tengah), yaitu Rp29.000.

Logika: Karena Rp29.000 lebih kecil dari Rp37.000, program menyimpulkan bahwa target tidak mungkin ada di sebelah kiri. Maka, program mengabaikan harga Rp13.000 dan Rp15.000.

Langkah 2 (Mengecek Sisa Kanan):

Program fokus ke sisi kanan dan mengecek indeks 3, yaitu Rp37.000.

Logika: Nilai ditemukan karena Rp37.000 sama dengan target.

Hasil Akhir : Program melaporkan bahwa harga ditemukan pada urutan ke-4.


