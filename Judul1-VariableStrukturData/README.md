**Sistem Manajemen Antrean Pasien Klinik**

**Deskripsi Singkat**

Program ini dirancang untuk mensimulasikan sistem antrean pada sebuah klinik kesehatan. Algoritma yang diterapkan adalah **Linked List** dengan prinsip **Queue (FIFO - First In, First Out)**.

Dalam program ini, setiap pasien direpresentasikan sebagai sebuah **Node**. Penggunaan Linked List memungkinkan penambahan pasien baru di akhir antrean (**Enqueue**) dan pemanggilan pasien di depan antrean (**Dequeue**) dilakukan dengan efisien secara dinamis tanpa batas ukuran array statis. Pasien yang pertama kali masuk ke sistem akan menjadi yang pertama kali dilayani oleh dokter.

**Source Code**

<img width="442" height="360" alt="kode1" src="https://github.com/user-attachments/assets/2a7f7669-39c1-46ac-9a31-b90dc316dda9" />
<img width="413" height="387" alt="kode 2" src="https://github.com/user-attachments/assets/dda474fe-3ff4-4edb-8feb-0df8be7b379a" />
<img width="220" height="100" alt="kode 3" src="https://github.com/user-attachments/assets/f02fa3c5-cece-4c38-99a0-3277c693c2cf" />

class Pasien: ( Mendeklarasikan kelas bernama Pasien yang berfungsi sebagai Node dalam Linked List).

def_init_(self, nama): (Metode inisialisasi yang otomatis berjalan saat objek pasien baru dibuat).

self.nama = nama: (Atribut untuk menyimpan data berupa nama pasien).

self.next = None (Atribut pointer yang awalnya bernilai kosong (None), digunakan untuk menyambungkan ke pasien berikutnya).

class AntreanKlinik: (Mendeklarasikan kelas untuk mengelola antrean).

def __init__(self): (Saat objek klinik dibuat, antrean diatur agar kosong di awal).

self.front = None: Pointer yang menunjuk ke pasien paling depan (yang akan dilayani pertama kali).

self.rear = None: Pointer yang menunjuk ke pasien paling belakang (yang baru saja bergabung)

baru = Pasien(nama): Membuat objek pasien baru berdasarkan input nama.

if self.rear is None:: Memeriksa apakah antrean saat ini kosong.

self.front = self.rear = baru: Jika kosong, maka pasien baru ini menjadi pasien pertama sekaligus terakhir dalam sistem.

else:: Jika sudah ada pasien lain:

self.rear.next = baru: Pasien yang sebelumnya di posisi paling belakang diarahkan untuk menunjuk ke pasien baru tersebut.

self.rear = baru: Status pasien terakhir (rear) kini diperbarui ke pasien yang baru datang tersebut.

print(...): Memberikan konfirmasi visual bahwa pasien telah berhasil masuk ke sistem.

if self.front is None:: Memeriksa apakah antrean kosong sebelum melakukan pemanggilan.

terpanggil = self.front.nama: Menyimpan nama pasien terdepan ke dalam variabel agar bisa dicetak nantinya.

self.front = self.front.next: Memindahkan pointer front ke pasien di urutan kedua. Pasien pertama secara otomatis terhapus dari akses antrean.

if self.front is None: self.rear = None: Jika setelah dipanggil antrean menjadi kosong, pastikan pointer belakang (rear) juga dikosongkan.

print(...): Menampilkan nama pasien yang sedang dipanggil ke ruang dokter.

if self.front is None:: Jika front masih None, berarti tidak ada data untuk ditampilkan.

temp = self.front: Membuat variabel bantuan temp untuk mulai menelusuri dari posisi terdepan.

while temp:: Melakukan perulangan selama temp belum mencapai ujung akhir antrean (None).

print(temp.nama, end=" -> "): Mencetak nama pasien yang sedang ditunjuk oleh temp.

temp = temp.next: Menggeser penunjuk temp ke pasien berikutnya untuk iterasi selanjutnya.

klinik = AntreanKlinik(): Membuat satu instansi sistem kl

tambah_pasien(...): Memasukkan Andi, Budi, dan Cici secara berurutan.

panggil_pasien(): Menghapus Andi (paling depan), sehingga Budi sekarang menjadi orang terdepan di antrean.

**Output**

<img width="309" height="81" alt="output kode" src="https://github.com/user-attachments/assets/244ba949-8538-4ac0-bdf4-bd22d9bd11fe" />

Output dari kodingan diatas adalah Pendaftaran Pasien (Enqueue): Saat Andi, Budi, dan Cici datang mendaftar, sistem memasukkan mereka secara berurutan ke dalam "gerbong" antrean. Karena sistem ini mendahulukan yang datang pertama (FIFO), Andi otomatis berada di barisan paling depan, sementara Cici berada di posisi paling belakang.

Cek Antrean Awal: Ketika kita melihat daftar antrean, program menelusuri dari depan ke belakang. Hasilnya menunjukkan urutan yang benar: Andi adalah orang pertama, diikuti Budi, dan Cici sebagai yang terakhir.

Pemanggilan Pasien (Dequeue): Saat dokter memanggil pasien, sistem secara otomatis menunjuk Andi karena dia yang datang paling awal. Begitu Andi masuk ke ruang dokter, namanya langsung dihapus dari daftar tunggu.

Kondisi Antrean Terbaru: Setelah Andi keluar dari daftar, posisi "paling depan" kini berpindah ke Budi. Jika dokter memanggil lagi, maka Budi-lah yang akan masuk selanjutnya, sementara Cici tetap menunggu di urutan belakang.

https://youtu.be/vIKVmloxOl4?si=qH60n2occm84cotd







