**Program Pengurutan No Jersey Pemain Bola**

**Deskripsi**

Program ini dibuat untuk mengurutkan no jersey pemain bola menggunakan ascending. Data diurutkan dari nilai terkecil ke nilai terbesar

Program ini dibuat menggunakan struktur data Insertion Sort yang cara kerjanya membandingkan satu elemen dimulai dari elemen kedua pada indeks 1 dengan elemen sebelumnya yang sudah dianggap terurut.

**Source Kode**

<img width="510" height="415" alt="kode 1" src="https://github.com/user-attachments/assets/1f6baf8f-3dfc-43ae-a4cd-4be1fb88f21f" />

<img width="351" height="126" alt="kode 2" src="https://github.com/user-attachments/assets/7d4576e8-9979-4142-b962-8cbfe4f5f5af" />

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
Memastikan bahwa fungsi main() hanya akan dijalankan jika file ini dieksekusi secara langsung sebagai program utama.

**Output**

<img width="369" height="120" alt="output 1" src="https://github.com/user-attachments/assets/26b151a9-7ee7-4782-8e9b-72c78f37862f" />

Pengguna memasukkan angka 5, sehingga program akan meminta 5 data angka jersey. Kemudian, Pengguna memasukkan angka secara manual satu per satu: 08, 11, 19, 23, dan 01. Saat di tampilkan, Program menampilkan list asli sesuai urutan input pengguna, yaitu [8, 11, 19, 23, 1].

Algoritma bekerja dengan mengambil angka (seperti 1) dan menyisipkannya ke posisi yang benar dengan membandingkannya dengan angka di sebelah kiri.  
Hasil Akhir: Program mencetak hasil akhir yang sudah terurut dari angka terkecil ke terbesar: 1 8 11 19 23

https://youtu.be/Rq2jS10msSg?feature=shared











