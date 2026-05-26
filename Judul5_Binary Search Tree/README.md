**Aplikasi Manajemen Tugas (Task Management)**

**Deskripsi Singkat**
Program ini adalah sebuah Aplikasi Manajemen Tugas (Task Management) berbasis CLI (Command Line Interface). Aplikasi ini berfungsi untuk mencatat, mengelola, dan melacak daftar tugas berdasarkan tingkat urgensi atau prioritas tertentu yang direpresentasikan dalam bentuk angka (ID Prioritas).
Struktur data utama yang digunakan dalam program ini adalah Binary Search Tree (BST) atau Pohon Pencarian Biner.

**Source Kode**

<img width="565" height="417" alt="kode1" src="https://github.com/user-attachments/assets/616ed12b-ddb3-4679-a906-9dbc4481c464" />

<img width="502" height="387" alt="kode 2" src="https://github.com/user-attachments/assets/77ae6e93-64e9-4746-9007-bd8905278a1e" />

<img width="594" height="400" alt="kode 3" src="https://github.com/user-attachments/assets/5d10d524-7ab4-4feb-9a9e-1a5459fe8bad" />

<img width="593" height="385" alt="kode 4" src="https://github.com/user-attachments/assets/86f75b27-5c95-4933-9072-c956f47c0429" />

<img width="513" height="371" alt="kode 5" src="https://github.com/user-attachments/assets/012cdcf0-8c1d-4352-82bb-43fa7ad8e158" />

<img width="646" height="396" alt="kode 6" src="https://github.com/user-attachments/assets/8e5f2081-12e1-4b33-b900-e5b91f13ab5f" />

<img width="701" height="402" alt="kode 7" src="https://github.com/user-attachments/assets/407c41d1-3ea5-46fb-a258-2123bf9bbef4" />

<img width="750" height="383" alt="kode 8" src="https://github.com/user-attachments/assets/2c73b40f-5075-4d38-9c47-e77a5f1b71a5" />

<img width="313" height="87" alt="kode 9" src="https://github.com/user-attachments/assets/b93d2fa9-0bae-43d1-853d-efe7cf786579" />

class Node:: Mendefinisikan cetak biru (blueprint) untuk setiap node di dalam pohon.

def __init__(self, key, nama_tugas, deskripsi):: Konstruktor untuk menginisialisasi objek node baru saat dibuat.

self.key = key: Menyimpan kunci penentu posisi node (di sini bertindak sebagai ID Prioritas).

self.nama_tugas = nama_tugas: Menyimpan string nama tugas.

self.deskripsi = deskripsi: Menyimpan string detail deskripsi tugas.

self.left = None: Mengatur penunjuk (pointer) ke anak sebelah kiri ke None (kosong) saat pertama dibuat.

self.right = None: Mengatur penunjuk ke anak sebelah kanan ke None (kosong) saat pertama dibuat.

class BSTLanjut:: Mendefinisikan struktur utama untuk Binary Search Tree.

def __init__(self):: Konstruktor untuk membuat pohon baru.

self.root = None: Mengatur akar utama (root) pohon menjadi kosong saat pohon pertama kali dibuat.

def insert_node(self, root, key, nama_tugas, deskripsi): Fungsi helper rekursif untuk mencari posisi kosong bagi node baru.

if root is None:: Jika posisi saat ini kosong (atau pohon masih kosong), buat node baru di posisi tersebut.

return Node(key, nama_tugas, deskripsi): Mengembalikan objek node baru yang berhasil dibuat ke pemanggil fungsi.

if key < root.key:: Jika key baru lebih kecil dari key node saat ini, arahkan pencarian ke cabang kiri.

root.left = self.insert_node(root.left, key, nama_tugas, deskripsi): Memperbarui hubungan anak kiri setelah fungsi rekursif selesai menempatkan node baru.

elif key > root.key: : Jika key baru lebih besar dari key node saat ini, arahkan pencarian ke cabang kanan.

root.right = self.insert_node(root.right, key, nama_tugas, deskripsi)
: Memperbarui hubungan anak kanan setelah fungsi rekursif selesai menempatkan node baru.

else:: Berjalan jika key baru sama dengan key yang sudah ada di pohon (duplikat tidak diizinkan).

print(f"\n[Peringatan] ID Prioritas {key} sudah digunakan oleh tugas lain!"): Menampilkan pesan kesalahan penolakan data duplikat.

return root: Mengembalikan node saat ini tanpa perubahan struktur untuk mempertahankan pohon.

def insert(self, key, nama_tugas, deskripsi): Fungsi publik yang dipanggil pengguna untuk menambah tugas.

self.root = self.insert_node(self.root, key, nama_tugas, deskripsi): Memulai proses rekursif dari akar utama (self.root) dan memperbarui akar jika pohon awalnya kosong.

def find_min_node(self, root):
Fungsi pembantu untuk mencari node dengan nilai terkecil pada suatu cabang pohon.

current = root
Memulai pelacakan dari titik node yang diberikan.

while current is not None and current.left is not None:
Selama node tersebut punya cabang di sebelah kiri, program akan terus bergerak ke kiri.

current = current.left
Menggeser posisi pelacakan ke node sebelah kiri.

return current
Mengembalikan node paling kiri yang otomatis memegang nilai terkecil.

def delete_node(self, root, key):
Fungsi internal rekursif untuk mencari dan menghapus node berdasarkan key.

if root is None:
Jika pohon kosong atau ID tugas tidak ditemukan setelah dicari ke seluruh cabang, kembalikan None.

return None
Keluar dari fungsi karena tidak ada data yang bisa dihapus.

if key < root.key:
Jika ID yang mau dihapus lebih kecil dari ID node saat ini, maka target ada di cabang kiri.

root.left = self.delete_node(root.left, key)
Masuk ke cabang kiri untuk melanjutkan proses pencarian hapus.

elif key > root.key:
Jika ID yang mau dihapus lebih besar dari ID node saat ini, maka target ada di cabang kanan.

root.right = self.delete_node(root.right, key)
Masuk ke cabang kanan untuk melanjutkan proses pencarian hapus.

else:
Blok ini berjalan jika ID target sudah ditemukan cocok (key == root.key).

if root.left is None and root.right is None:
Kondisi 1: Jika node target tidak punya anak sama sekali (node daun/paling ujung).

return None
Menghapus node tersebut dengan cara mengembalikan nilai kosong ke atasnya.

elif root.left is None:
Kondisi 2a: Jika node target hanya punya anak di sebelah kanan.

return root.right
Menggantikan posisi node yang dihapus dengan node anak kanannya tersebut.

elif root.right is None:
Kondisi 2b: Jika node target hanya punya anak di sebelah kiri.

return root.left
Menggantikan posisi node yang dihapus dengan node anak kirinya tersebut.

else:
Kondisi 3: Jika node target memiliki dua anak (kiri dan kanan).

successor = self.find_min_node(root.right)
Mencari nilai terkecil di sub-pohon cabang kanan untuk dijadikan penerus.

root.key = successor.key
Menimpa ID node saat ini dengan ID milik penerus (successor).

root.nama_tugas = successor.nama_tugas
Menimpa nama tugas saat ini dengan nama tugas milik penerus.

root.deskripsi = successor.deskripsi
Menimpa deskripsi tugas saat ini dengan deskripsi milik penerus.

root.right = self.delete_node(root.right, successor.key)
Menghapus node penerus yang asli di cabang kanan karena datanya sudah aman disalin ke atas.

return root
Mengembalikan struktur pohon yang telah diperbarui setelah proses penghapusan.

def delete(self, key):
Fungsi publik yang dipanggil pengguna untuk menghapus tugas.

self.root = self.delete_node(self.root, key)
Memulai proses pencarian dan penghapusan data dari titik root

def height(self, root):Fungsi untuk menghitung tinggi atau level kedalaman pohon tugas.

if root is None:Jika titik pohon kosong, kembalikan nilai -1 (pohon kosong tidak memiliki tinggi).

return -1Dasar pengembalian nilai untuk perhitungan tinggi rekursif.

height_left = self.height(root.left)Menghitung tinggi cabang sebelah kiri secara rekursif.

height_right = self.height(root.right)Menghitung tinggi cabang sebelah kanan secara rekursif.

return 1 + max(height_left, height_right)Mengambil nilai tertinggi di antara cabang kiri atau kanan, lalu ditambah 1 (dihitung bersama node induknya).

def level_order(self, root):Menampilkan struktur pohon secara mendatar, level demi level dari atas ke bawah.

if root is None:Jika pohonnya kosong, tampilkan teks khusus lalu keluar dari fungsi.

print("(kosong)")Mencetak tanda bahwa tidak ada isi pohon untuk penelusuran level-order.

return (Keluar dari metode level_order.)
queue = []Membuat sebuah list kosong yang difungsikan sebagai antrean penelusuran.

queue.append(root)Memasukkan node akar (root) sebagai antrean pertama yang akan diperiksa.

while len(queue) > 0:Melakukan perulangan selama masih ada node di dalam antrean.

current = queue.pop(0)Mengambil dan mengeluarkan elemen pertama dari antrean untuk diproses saat ini.

print(f"[{current.key}: {current.nama_tugas}]", end=" ")Mencetak data ID prioritas dan nama tugas node tersebut ke samping dalam satu baris.

if current.left is not None:Jika node yang sedang diproses punya anak kiri, masukkan anak kiri itu ke dalam antrean.

queue.append(current.left)Memasukkan anak kiri ke baris belakang antrean.

if current.right is not None:Jika node yang sedang diproses punya anak kanan, masukkan anak kanan itu ke dalam antrean.

queue.append(current.right)Memasukkan anak kanan ke baris belakang antrean.

print()Mencetak baris baru setelah seluruh tingkatan level-order selesai ditampilkan.

def inorder_tugas(self, root):Fungsi penelusuran In-Order (Kiri $\rightarrow$ Akar $\rightarrow$ Kanan) untuk mengurutkan tugas dari angka ID terkecil ke terbesar.

if root:Jika node saat ini ada (tidak kosong), jalankan proses di bawahnya.

self.inorder_tugas(root.left)Berjalan masuk terus ke cabang kiri terlebih dahulu secara rekursif.

print(f"| Prio: {root.key:<3} | {root.nama_tugas:<20} | {root.deskripsi:<30} |")Mencetak data tugas saat ini dengan format tabel yang rapi rata kiri.

self.inorder_tugas(root.right)Berjalan masuk ke cabang sebelah kanan secara rekursif.

def find_successor(self, root, key):
Mencari node yang nilainya satu tingkat di atas key yang diinput.

current = root dan successor = None
Mengatur penunjuk posisi awal dari root dan menyiapkan wadah penampung hasil sebagai kosong.

while current is not None:
Melakukan perulangan selama jalur pencarian pohon belum habis.

if key < current.key:
Jika nilai target lebih kecil dari node saat ini, berarti node saat ini berpotensi menjadi calon penerus (successor).

successor = current
Menyimpan node saat ini sebagai kandidat penerus sementara.

current = current.left
Belok ke kiri untuk mencari apakah ada angka lain yang lebih mendekati target.

elif key > current.key:
Jika nilai target lebih besar dari node saat ini, otomatis calon penerus ada di kanan.

current = current.right
Ganti posisi pelacakan langsung ke cabang kanan.

else:
Jika nilai key yang dicari pas ditemukan di dalam pohon.

break
Hentikan perulangan karena node target sudah ditemukan posisinya.

if current is None:
Jika setelah dicari ternyata ID tugas utama yang dimasukkan user tidak ada di pohon.

return None, False
Mengembalikan nilai kosong dan status False (data tidak ditemukan).

if current.right is not None:
Jika node target ditemukan dan dia memiliki cabang sebelah kanan.

successor = self.find_min_node(current.right)
Penerus pastinya adalah nilai paling terkecil yang ada di sub-pohon cabang kanannya tersebut.

if successor is None:
Jika variabel successor tetap kosong (tidak ada angka yang lebih besar dari target di dalam pohon).

return None, False
Mengembalikan nilai kosong dengan status gagal/tidak ada.

return successor, True
Mengembalikan objek node penerus yang sukses ditemukan beserta status True.

def find_predecessor(self, root, key):
Mencari node yang nilainya satu tingkat di bawah key yang diinput (tugas yang sedikit lebih penting). Logikanya berkebalikan dari fungsi successor.

if key > current.key:
Jika target lebih besar, node saat ini disimpan sebagai calon pendahulu (predecessor).

predecessor = current dan current = current.right
Menyimpan kandidat sementara lalu bergerak mencari ke cabang kanan.

elif key < current.key: dan current = current.left
Jika target lebih kecil, langsung belok mencari ke cabang kiri.

if current.left is not None:
Jika node target punya cabang kiri, cari nilai paling besar di sub-pohon kiri tersebut.

temp = current.left dan perulangan while temp.right is not None:
Bergeser ke kiri sekali, lalu telusuri cabang kanan sedalam-dalamnya hingga mentok untuk mendapatkan nilai maksimum di sisi kiri tersebut.

def main():
Deklarasi fungsi utama program.

bst = BSTLanjut()
Membuat satu objek pohon kosong baru bernama bst.

bst.insert(5, "Belajar Ujian", ...) sampai baris ke-126
Memasukkan 3 data tugas bawaan ke dalam sistem pohon saat aplikasi baru dibuka sebagai contoh awal.

pilih = 0
Inisialisasi variabel pilihan menu dengan angka awal 0.

while pilih != 7:
Aplikasi akan terus berulang memunculkan menu teks selama pengguna tidak mengetikkan angka 7.

print(...) (Baris 129 - 139)
Mencetak teks judul aplikasi beserta pilihan menu nomor 1 sampai 7 ke layar terminal.

try: dan pilih = int(input(...))
Mengamankan input pilihan menu agar langsung diubah ke bentuk angka integer.

except ValueError:
Menangkap kesalahan jika pengguna mengetik huruf pada menu pilihan angka.

print("Input tidak valid! Masukkan angka.") dan continue
Menampilkan pesan peringatan lalu langsung melompat kembali ke atas menampilkan menu lagi.

if pilih == 1:
Blok eksekusi jika pengguna ingin menambah tugas baru. Meminta input ID Prioritas, Nama Tugas, dan Deskripsi, lalu mengeksekusi perintah bst.insert(prio, nama, deskripsi).

elif pilih == 2:
Blok eksekusi untuk menyelesaikan tugas. Meminta input angka ID tugas, lalu memanggil fungsi bst.delete(prio).

elif pilih == 3:
Blok eksekusi untuk melihat seluruh tugas aktif. Jika akar pohon kosong (bst.root is None), tampilkan pesan bersih. Jika ada, cetak kepala tabel dan panggil fungsi bst.inorder_tugas(bst.root).

elif pilih == 4:
Menampilkan tinggi kedalaman struktur pohon lewat bst.height(bst.root) dan urutan visual datanya lewat fungsi bst.level_order(bst.root).

elif pilih == 5:
Meminta input angka ID, lalu memanggil fungsi bst.find_successor. Jika statusnya ketemu (found), cetak nama tugas berikutnya.

elif pilih == 6:
Meminta input angka ID, lalu memanggil fungsi bst.find_predecessor untuk mencetak tugas yang urgensinya tepat di atas input tersebut.

elif pilih == 7:
Mencetak teks ucapan terima kasih karena perulangan while akan langsung berhenti setelah baris ini selesai.

else: print("Pilihan menu tidak tersedia!")
Menangani kasus jika pengguna memasukkan angka integer di luar angka 1-7 (misal menginput angka 9).

if __name__ == "__main__": main()
Sistem dasar Python untuk otomatis memicu dan menjalankan fungsi main() saat file skrip ini dieksekusi di terminal komputer.

**Output**

<img width="444" height="235" alt="output1" src="https://github.com/user-attachments/assets/991977fa-58a6-4a6e-9a23-948e024781e5" />

<img width="461" height="199" alt="output2" src="https://github.com/user-attachments/assets/3ca5b37d-69f7-486e-b7e6-7c8118474b9b" />

<img width="487" height="283" alt="output3" src="https://github.com/user-attachments/assets/75657cfb-7988-488e-8b61-ecee9cab839a" />

<img width="516" height="221" alt="output4" src="https://github.com/user-attachments/assets/f5b61cc9-baae-4d76-9f54-0ea436077023" />

<img width="385" height="226" alt="output5" src="https://github.com/user-attachments/assets/4ff5179f-5401-4990-a1bf-5476bed23afa" />

<img width="432" height="233" alt="output6" src="https://github.com/user-attachments/assets/e239d819-81a9-4745-810a-ab9590d4434c" />

<img width="355" height="191" alt="output7" src="https://github.com/user-attachments/assets/e60c932d-174a-4f67-a14d-7a8e3c8fe9bf" />


pengguna mengetik angka 1. Saat program meminta input, pengguna memasukkan angka 2 untuk ID prioritas, mengetik "Matematika Diskrit" sebagai nama tugas, dan "Tugas Grap" untuk deskripsinya.

pengguna mengetik angka 2 untuk memilih menu penyelesaian/penghapusan tugas. Saat program meminta ID, pengguna mengetik angka 2 (tugas yang baru saja dimasukkan tadi pun langsung terhapus).

pengguna mengetik angka 3 pada pilihan menu. Program langsung menampilkan tabel berisi sisa tugas yang masih aktif dan menyusunnya rapi berurutan berdasarkan nomor ID-nya.

Pengguna kemudian mengetik angka 4 untuk melihat bagaimana komputer menyusun tugas-tugas tersebut di latar belakang. Terminal pun menampilkan tinggi pohon dan urutan data secara mendatar.

Pengguna mengetik angka 5 untuk melakukan pencarian otomatis. Saat diminta memasukkan batas ID prioritas, pengguna mengetik angka 3. Komputer lalu memunculkan nama tugas berikutnya yang memiliki prioritas di bawah angka tersebut.

Pengguna mengetik angka 6 untuk mencoba fitur pencarian kebalikan. Saat diminta memasukkan ID prioritas, pengguna mengetik angka 5. Komputer langsung menampilkan nama tugas yang posisinya lebih penting atau berada di atas angka tersebut.

Keluar dari Aplikasi Terakhir, setelah selesai mencoba semua fitur, pengguna mengetik angka 7 pada terminal. Langkah ini menghentikan perulangan menu dan menutup aplikasi secara keseluruhan.

https://youtu.be/upjsxqBDLKA?si=bFkvTj7cWw-Q4WBx
