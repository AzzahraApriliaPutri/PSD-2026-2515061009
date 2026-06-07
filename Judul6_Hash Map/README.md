**Program Pengecekan Motor di Parkiran**

**Deskripsi Singkat**

Program ini adalah simulasi database kendaraan berbasis Hash Table berukuran 10 slot yang berfungsi menyimpan dan mencari data plat nomor berdasarkan kunci angka.

Struktur data ini menggunakan fungsi hash modulo untuk menentukan posisi indeks data secara cepat. Jika terjadi bentrokan indeks (collision), metode Open Addressing dengan Linear Probing akan mencari slot terdekat berikutnya secara berurutan. Keandalan sistem ini didukung oleh Manajemen Status Slot (EMPTY, OCCUPIED, DELETED) yang menjaga agar alur pencarian data tidak terputus saat ada data yang dihapus. Di akhir program, mekanisme ini langsung diuji melalui penginputan empat data motor serta simulasi pencarian kuncinya.

Source Kode

<img width="684" height="557" alt="603924826-e0f855eb-aa89-4b1b-af6d-8e6c728f6c43" src="https://github.com/user-attachments/assets/1ed1e198-b010-4f40-a7e0-5dab400a7695" />

<img width="722" height="518" alt="kode 2" src="https://github.com/user-attachments/assets/9a424a0f-3d45-4c00-ba0b-c791eafc422d" />

<img width="733" height="507" alt="kode 3" src="https://github.com/user-attachments/assets/4760a5eb-f870-4581-8f24-d8e75a28492b" />

<img width="638" height="480" alt="kode 4" src="https://github.com/user-attachments/assets/cf08263e-67b8-4dcd-91ed-38908282d914" />

class SlotState:
Baris 1 Membuat class bernama SlotState untuk mendefinisikan status setiap slot di Hash Table.

EMPTY = 0
Baris 2 Konstanta EMPTY (0) menandakan slot benar-benar kosong sejak awal (belum pernah diisi).

OCCUPIED = 1
Baris 3 Konstanta OCCUPIED (1) menandakan slot sedang terisi oleh data aktif.

DELETED = 2
Baris 4 Konstanta DELETED (2) menandakan data di slot ini sudah dihapus (penting untuk kelanjutan Linear Probing).

class Entry:
Baris 7 Membuat class bernama Entry untuk merepresentasikan satu baris atau kotak data di dalam tabel.

def init(self):
Baris 8 Fungsi konstruktor untuk menginisialisasi objek Entry baru.

self.key = None
Baris 9 Atribut key diset None (kosong), nantinya akan menyimpan angka plat motor.

self.value = None
Baris 10 Atribut value diset None (kosong), nantinya akan menyimpan teks detail kendaraan.

self.state = SlotState.EMPTY
Baris 11 Atribut state diset SlotState.EMPTY, artinya saat baru dibuat status slot adalah KOSONG.

class HashMapOpenAddressing:
Baris 14 Membuat class utama bernama HashMapOpenAddressing untuk mengatur manajemen struktur data Hash Map.

def init(self, size=10):
Baris 15 Fungsi konstruktor untuk membuat objek Hash Map dengan ukuran default 10.

self.SIZE = size
Baris 16 Menyimpan kapasitas ukuran tabel ke dalam variabel objek self.SIZE.

self.table = [Entry() for _ in range(self.SIZE)]
Baris 17 Membuat list bernama self.table berisi sekumpulan objek Entry sebanyak ukuran self.SIZE.

def hash_function(self, key):
Baris 19 Membuat fungsi hash bernama hash_function untuk menentukan posisi indeks berdasarkan key.

return (key % self.SIZE + self.SIZE) % self.SIZE
Baris 20 dan 21 Menghitung nilai indeks menggunakan rumus modulo (%) agar hasilnya selalu pas di dalam rentang ukuran tabel.

def insert(self, key, value):
Baris 23 Membuat fungsi insert untuk memasukkan data baru (key dan value) ke dalam Hash Table.

idx = self.hash_function(key)
Baris 24 Mencari indeks awal untuk key tersebut menggunakan fungsi hash.

first_deleted = -1
Baris 25 Variabel first_deleted diset minus 1 untuk mencatat lokasi slot berstatus DELETED pertama yang dilewati.

for step in range(self.SIZE):
Baris 26 Melakukan perulangan (looping) maksimal sebanyak ukuran tabel untuk mencari slot kosong.

i = (idx + step) % self.SIZE
Baris 27 Menghitung indeks baru (i) menggunakan metode Linear Probing jika terjadi tabrakan data (collision).

if self.table[i].state == SlotState.OCCUPIED:
Baris 28 Mengecek jika slot pada indeks i berstatus TERISI (OCCUPIED).

if self.table[i].key == key:
Baris 29 Mengecek jika key yang ada di slot tersebut sama dengan key baru yang ingin dimasukkan.

self.table[i].value = value
Baris 30 Memperbarui (update) value lama dengan value baru karena key-nya sama.

return True
Baris 31 Mengembalikan nilai True untuk menandakan proses pembaruan data berhasil.

elif self.table[i].state == SlotState.DELETED:
Baris 32 Mengecek jika slot pada indeks i ternyata berstatus DIHAPUS (DELETED).

if first_deleted == -1:
Baris 33 Jika ini adalah slot DELETED pertama yang ditemui, catat indeksnya ke variabel first_deleted.

first_deleted = i
Baris 34 Menyimpan nilai indeks i ke variabel first_deleted.

else:
Baris 35 Blok else ini berjalan jika menemukan slot yang benar-benar KOSONG (EMPTY).

if first_deleted != -1:
Baris 36 Mengecek jika di sepanjang jalan tadi program sempat menemukan slot DELETED.

i = first_deleted
Baris 37 Mengalihkan target penyimpanan data ke indeks slot DELETED pertama tadi agar hemat ruang.

self.table[i].key = key
Baris 38 Mengisi atribut key pada slot indeks i dengan key baru.

self.table[i].value = value
Baris 39 Mengisi atribut value pada slot indeks i dengan value baru.

self.table[i].state = SlotState.OCCUPIED
Baris 40 Mengubah status slot tersebut menjadi TERISI (OCCUPIED).

return True
Baris 41 Mengembalikan nilai True untuk menandakan proses input data baru sukses.

if first_deleted != -1:
Baris 42 Mengecek di luar loop, jika tabel penuh tapi sempat menemukan slot DELETED yang tersisa.

self.table[first_deleted].key = key
Baris 43 Mengisi key baru ke slot DELETED tersebut.

self.table[first_deleted].value = value
Baris 44 Mengisi value baru ke slot DELETED tersebut.

self.table[first_deleted].state = SlotState.OCCUPIED
Baris 45 Mengubah status slot DELETED tersebut menjadi TERISI (OCCUPIED).

return True
Baris 46 Mengembalikan nilai True untuk menandakan proses berhasil.

return False
Baris 47 Mengembalikan nilai False jika tabel benar-benar penuh total dan tidak ada slot kosong sama sekali.

def search(self, key):
Baris 49 Membuat fungsi search untuk mencari data kendaraan berdasarkan key.

idx = self.hash_function(key)
Baris 50 Menghitung nilai indeks awal target menggunakan fungsi hash.

for step in range(self.SIZE):
Baris 51 Melakukan perulangan untuk memeriksa slot satu per satu dari indeks awal.

i = (idx + step) % self.SIZE
Baris 52 Menghitung indeks pergeseran (Linear Probing).

if self.table[i].state == SlotState.EMPTY:
Baris 53 Jika bertemu slot yang berstatus EMPTY, pencarian langsung dihentikan.

return None
Baris 54 Mengembalikan nilai None karena data pasti tidak ada di dalam tabel.

if self.table[i].state == SlotState.OCCUPIED and self.table[i].key == key:
Baris 55 Jika slot berstatus TERISI dan key di dalam slot tersebut cocok dengan key yang dicari.

return self.table[i]
Baris 56 Mengembalikan objek Entry lengkap (berisi key, value, state) karena data ditemukan.

return None
Baris 57 Mengembalikan None jika loop selesai dan seluruh isi tabel sudah diperiksa tetapi tidak ketemu.

def remove_key(self, key):
Baris 59 Membuat fungsi remove_key untuk menghapus data kendaraan berdasarkan key.

entry = self.search(key)
Baris 60 Memanggil fungsi search() untuk memeriksa apakah data tersebut terdaftar di tabel.

if entry is None:
Baris 61 Jika hasil pencarian bernilai None (data tidak ditemukan).

return False
Baris 62 Mengembalikan nilai False karena proses penghapusan gagal akibat data tidak ada.

entry.state = SlotState.DELETED
Baris 63 Jika ketemu, ubah status slot data tersebut menjadi DIHAPUS (DELETED).

return True
Baris 64 Mengembalikan nilai True tanda penghapusan data berhasil dilakukan.

def display(self):
Baris 66 Membuat fungsi display untuk mencetak visualisasi isi tabel ke terminal.

print("\nIsi Hash Table (Data Kendaraan):")
Baris 67 Mencetak teks judul tabel ke layar monitor.

for i in range(self.SIZE):
Baris 68 Melakukan perulangan untuk mencetak semua isi slot dari indeks 0 sampai maksimal.

print(f"{i}: ", end="")
Baris 69 Mencetak nomor indeks slot di awal baris tanpa membuat baris baru.

if self.table[i].state == SlotState.EMPTY:
Baris 70 Jika status slot pada indeks i adalah EMPTY.

print("EMPTY")
Baris 71 Mencetak tulisan "EMPTY".

elif self.table[i].state == SlotState.DELETED:
Baris 72 Jika status slot pada indeks i adalah DELETED.

print("DELETED")
Baris 73 Mencetak tulisan "DELETED".

else:
Baris 74 Blok else dijalankan jika status slot terisi data aktif.

print(f"(Key Angka: {self.table[i].key}, Info: {self.table[i].value})")
Baris 75 Mencetak informasi key angka dan teks value kendaraan yang disimpan.

def cek_plat(self, kode_plat):
Baris 77 Membuat fungsi helper cek_plat untuk mempermudah cetak teks hasil pencarian bagi user.

hasil = self.search(kode_plat)
Baris 78 Memanggil fungsi search() untuk mencari data kendaraan berdasarkan kode_plat.

if hasil is not None:
Baris 79 Jika objek data kendaraan berhasil ditemukan (bukan None).

print(f"Data ditemukan -> {hasil.value}")
Baris 80 Mencetak pesan sukses beserta nilai atau value dari kendaraan tersebut.

else:
Baris 81 Blok else berjalan jika pencarian menghasilkan nilai None.

print("Data plat motor tidak ditemukan!")
Baris 82 Mencetak pesan informasi bahwa data plat motor tidak ditemukan.

def main():
Baris 85 Membuat fungsi main sebagai titik awal jalannya eksekusi program.

data_motor = HashMapOpenAddressing(size=10)
Baris 86 Membuat objek bernama data_motor dengan kapasitas ukuran tabel sebanyak 10 slot.

data_motor.insert(18, "BD 1234 XI (Honda Beat - Wijayanti)")
Baris 88 Memasukkan data kendaraan pertama dengan key 18 (masuk ke indeks 8 karena 18 modulo 10 adalah 8).

data_motor.insert(15, "DB 8888 XY (Yamaha NMax - Mutiara)")
Baris 89 Memasukkan data kendaraan kedua dengan key 15 (masuk ke indeks 5 karena 15 modulo 10 adalah 5).

data_motor.insert(33, "BE 4571 XA (Suzuki Nex - Kirani)")
Baris 90 Memasukkan data kendaraan ketiga dengan key 33 (masuk ke indeks 3 karena 33 modulo 10 adalah 3).

data_motor.insert(49, "F 2026 FG (Vespa Sprint - Arutala)")
Baris 91 Memasukkan data kendaraan keempat dengan key 49 (masuk ke indeks 9 karena 49 modulo 10 adalah 9).

data_motor.display()
Baris 93 Memanggil fungsi display untuk menampilkan kondisi tabel saat ini ke layar terminal.

print("-" * 50)
Baris 94 Mencetak garis pembatas sebanyak 50 karakter untuk merapikan tampilan log.

print("\n[Mencari Plat Motor dengan angka 18]")
Baris 96 Mencetak teks pemberitahuan pencarian untuk data key angka 18.

data_motor.cek_plat(18)
Baris 97 Memanggil fungsi cek_plat untuk memproses dan mencetak hasil pencarian key angka 18.

print("\n[Mencari Plat Motor dengan angka 33]")
Baris 99 Mencetak teks pemberitahuan pencarian untuk data key angka 33.

data_motor.cek_plat(33)
Baris 100 Memanggil fungsi cek_plat untuk memproses dan mencetak hasil pencarian key angka 33.

print("\n[Mencari Plat Motor dengan angka (49)]")
Baris 102 Mencetak teks pemberitahuan pencarian untuk data key angka 49.

data_motor.cek_plat(49)
Baris 103 Memanggil fungsi cek_plat untuk memproses dan mencetak hasil pencarian key angka 49.

if name == "main":
Baris 106 Struktur kendali standard Python untuk memastikan fungsi main() hanya berjalan jika file ini dieksekusi secara langsung.

main()
Baris 107 Memanggil dan menjalankan fungsi main().


**Output**

<img width="800" height="373" alt="604071344-72fbe42a-f774-4ff5-969b-71fb563ea51e" src="https://github.com/user-attachments/assets/82ebac5f-4ec6-414b-bcf8-b9b2754c5173" />


Program ini mengimplementasikan struktur data Hash Map dengan metode Open Addressing dan Linear Probing untuk mengelola data kendaraan berdasarkan angka plat nomor mereka. Proses kerja seluruh sistem ini mengalir melalui tiga tahapan utama, yaitu inisialisasi tabel, penyimpanan data, dan pencarian data.

Tahap pertama adalah pembuatan struktur tabel penyimpanan. Saat program utama dijalankan, sebuah objek bernama data motor dibuat dengan kapasitas maksimal 10 slot ruang kosong. Setiap slot di dalam tabel ini memiliki objek penampung tersendiri yang sejak awal diberi status EMPTY atau benar-benar kosong karena belum pernah diisi data apa pun.

Tahap kedua adalah proses memasukkan data kendaraan ke dalam tabel menggunakan fungsi hash. Ketika data kendaraan seperti angka kunci 18 dimasukkan, sistem tidak menaruhnya secara acak, melainkan menghitung posisi indeksnya menggunakan rumus modulo dengan ukuran tabel, yaitu 18 modulo 10 yang menghasilkan indeks 8. Karena slot indeks 8 masih kosong, data langsung disimpan di sana dan status slotnya berubah menjadi OCCUPIED atau terisi. Proses serupa terjadi pada angka kunci 15 yang menempati indeks 5, angka kunci 33 yang menempati indeks 3, dan angka kunci 49 yang menempati indeks 9. Jika seandainya terjadi bentrokan atau dua kunci menghasilkan indeks yang sama, fungsi Linear Probing akan otomatis bergerak maju satu demi satu slot ke depan untuk mencari tempat terdekat yang masih kosong atau berstatus DELETED.

Program mencetak seluruh kondisi slot dari indeks 0 hingga 9 ke layar terminal, di mana slot nomor 3, 5, 8, dan 9 sukses menampilkan detail kendaraan, sementara slot lainnya tetap tertulis EMPTY. Setelah itu, fungsi pencarian diuji untuk menemukan kembali data kendaraan dari angka kunci 18, 33, dan 49. Sistem langsung melompat menuju indeks hasil perhitungan rumus hash masing-masing kunci tersebut. Karena status slot di indeks target tersebut terisi dan angka kuncinya cocok, program berhasil menemukan dan menampilkan informasi lengkap kendaraan secara instan tanpa perlu membuang waktu memeriksa isi tabel satu per satu dari awal.

