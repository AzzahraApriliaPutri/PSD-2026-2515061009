**Program Pengurutan No Jersey Pemain Bola**

**Deskripsi**

Program ini dibuat untuk mengurutkan no jersey pemain bola menggunakan ascending. Data diurutkan dari nilai terkecil ke nilai terbesar

Program ini dibuat menggunakan struktur data Insertion Sort yang cara kerjanya membandingkan satu elemen dimulai dari elemen kedua pada indeks 1 dengan elemen sebelumnya yang sudah dianggap terurut.

**Source Kode**

<img width="514" height="412" alt="kode 1" src="https://github.com/user-attachments/assets/aefe73d1-bf2b-4efc-ab4a-4f5d2f3c0c02" />

<img width="340" height="131" alt="kode 2" src="https://github.com/user-attachments/assets/59e14c25-da16-44d0-94f3-63752da6b6f8" />
def insertion_sort(arr, n):
Mendefinisikan fungsi pengurutan yang menerima dua parameter: arr (list angka) dan n (jumlah elemen).

for i in range(1, n):
Melakukan perulangan mulai dari indeks ke-1 hingga elemen terakhir ($n-1$). Indeks ke-0 dianggap sudah "terurut" di awal.

temp = arr[i]
Menyimpan nilai elemen saat ini ke dalam variabel sementara (temp) agar tidak hilang saat proses pergeseran angka lain.

j = i - 1
Menentukan titik awal pembandingan, yaitu satu posisi tepat di sebelah kiri elemen temp.  

while j >= 0 and arr[j] > temp:
Syarat perulangan untuk mencari posisi yang tepat bagi temp. Selama indeks j belum mencapai batas kiri dan nilai di arr[j] lebih besar dari temp, maka pergeseran dilakukan.

arr[j + 1] = arr[j]
Menggeser elemen yang lebih besar ke arah kanan (satu posisi ke depan).  j -= 1
Mengurangi indeks j untuk membandingkan temp dengan elemen berikutnya di sebelah kiri. 

arr[j + 1] = temp
Setelah posisi yang tepat ditemukan (ketika arr[j] tidak lagi lebih besar dari temp), nilai temp dimasukkan ke posisi j + 1.  

2. Fungsi main()Fungsi utama yang mengatur alur input/output program.  try: n = int(input(...))
Meminta input jumlah pemain dan mengubahnya menjadi tipe data integer.

 except ValueError:
Menangkap kesalahan jika pengguna memasukkan karakter non-angka, lalu menghentikan program dengan pesan error.  

arr = []
Inisialisasi list kosong untuk menampung angka-angka jersey yang akan dimasukkan. 

for i in range(n):
Melakukan perulangan sebanyak n kali untuk mengambil input setiap nomor jersey.  

while True: ... except ValueError:
Validasi input di dalam loop agar jika pengguna salah memasukkan data, program akan meminta ulang input untuk indeks tersebut hingga benar.  

arr.append(angka_jersey)
Memasukkan angka jersey yang valid ke dalam list arr. 

print(f"Umur sebelum diurutkan: {arr}")
Menampilkan kondisi list asli sebelum diproses oleh algoritma.

insertion_sort(arr, n)
Memanggil fungsi pengurutan yang telah dibuat sebelumnya. 

for i in range(n): print(arr[i], end=" ")
Mencetak setiap elemen list yang kini sudah terurut secara mendatar.  

if __name__ == "__main__": main()
Memastikan bahwa fungsi main() hanya akan dijalankan jika file ini dieksekusi secara langsung sebagai program utama,










