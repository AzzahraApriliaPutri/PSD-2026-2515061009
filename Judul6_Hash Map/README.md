**Program Pengecekan Motor di Parkiran**

**Deskripsi Singkat**

Program ini adalah simulasi database kendaraan berbasis Hash Table berukuran 10 slot yang berfungsi menyimpan dan mencari data plat nomor berdasarkan kunci angka.

Struktur data ini menggunakan fungsi hash modulo untuk menentukan posisi indeks data secara cepat. Jika terjadi bentrokan indeks (collision), metode Open Addressing dengan Linear Probing akan mencari slot terdekat berikutnya secara berurutan. Keandalan sistem ini didukung oleh Manajemen Status Slot (EMPTY, OCCUPIED, DELETED) yang menjaga agar alur pencarian data tidak terputus saat ada data yang dihapus. Di akhir program, mekanisme ini langsung diuji melalui penginputan empat data motor serta simulasi pencarian kuncinya.

Source Kode

<img width="684" height="582" alt="kode 1" src="https://github.com/user-attachments/assets/e0f855eb-aa89-4b1b-af6d-8e6c728f6c43" />

<img width="722" height="518" alt="kode 2" src="https://github.com/user-attachments/assets/9a424a0f-3d45-4c00-ba0b-c791eafc422d" />

<img width="733" height="507" alt="kode 3" src="https://github.com/user-attachments/assets/4760a5eb-f870-4581-8f24-d8e75a28492b" />

<img width="638" height="480" alt="kode 4" src="https://github.com/user-attachments/assets/cf08263e-67b8-4dcd-91ed-38908282d914" />

# Baris 1: Membuat class bernama SlotState untuk mendefinisikan status setiap slot di Hash Table.
class SlotState:
# Baris 2: Konstanta EMPTY (0) menandakan slot benar-benar kosong sejak awal (belum pernah diisi).
EMPTY = 0
# Baris 3: Konstanta OCCUPIED (1) menandakan slot sedang terisi oleh data aktif.
OCCUPIED = 1
# Baris 4: Konstanta DELETED (2) menandakan data di slot ini sudah dihapus (penting untuk kelanjutan Linear Probing).
DELETED = 2


# Baris 7: Membuat class bernama Entry untuk merepresentasikan satu baris/kotak data di dalam tabel.
class Entry:
# Baris 8: Fungsi konstruktor (__init__) untuk menginisialisasi objek Entry baru.
def __init__(self):
# Baris 9: Atribut key diset None (kosong), nantinya akan menyimpan angka plat motor.
self.key = None
# Baris 10: Atribut value diset None (kosong), nantinya akan menyimpan teks detail kendaraan.
self.value = None
# Baris 11: Atribut state diset SlotState.EMPTY, artinya saat baru dibuat status slot adalah KOSONG.
self.state = SlotState.EMPTY


# Baris 14: Membuat class utama bernama HashMapOpenAddressing untuk mengatur manajemen struktur data Hash Map.
class HashMapOpenAddressing:
# Baris 15: Fungsi konstruktor (__init__) untuk membuat objek Hash Map dengan ukuran default 10.
def __init__(self, size=10):
# Baris 16: Menyimpan kapasitas ukuran tabel ke dalam variabel objek self.SIZE.
self.SIZE = size
# Baris 17: Membuat list bernama self.table berisi sekumpulan objek Entry sebanyak ukuran self.SIZE.
self.table = [Entry() for _ in range(self.SIZE)]

# Baris 19: Membuat fungsi hash bernama hash_function untuk menentukan posisi indeks berdasarkan key.
def hash_function(self, key):
# Baris 20-21: Menghitung nilai indeks menggunakan rumus modulo (%) agar hasilnya selalu pas di dalam rentang ukuran tabel.
return (key % self.SIZE + self.SIZE) % self.SIZE

# Baris 23: Membuat fungsi insert untuk memasukkan data baru (key dan value) ke dalam Hash Table.
def insert(self, key, value):
# Baris 24: Mencari indeks awal untuk key tersebut menggunakan fungsi hash.
idx = self.hash_function(key)
# Baris 25: Variabel first_deleted diset -1 untuk mencatat lokasi slot berstatus DELETED pertama yang dilewati.
first_deleted = -1
# Baris 26: Melakukan perulangan (looping) maksimal sebanyak ukuran tabel untuk mencari slot kosong.
for step in range(self.SIZE):
# Baris 27: Menghitung indeks baru (i) menggunakan metode Linear Probing jika terjadi tabrakan data (collision).
i = (idx + step) % self.SIZE
# Baris 28: Mengecek jika slot pada indeks i berstatus TERISI (OCCUPIED).
if self.table[i].state == SlotState.OCCUPIED:
# Baris 29: Mengecek jika key yang ada di slot tersebut sama dengan key baru yang ingin dimasukkan.
if self.table[i].key == key:
# Baris 30: Memperbarui (update) value lama dengan value baru karena key-nya sama.
self.table[i].value = value
# Baris 31: Mengembalikan nilai True untuk menandakan proses pembaruan data berhasil.
return True
# Baris 32: Mengecek jika slot pada indeks i ternyata berstatus DIHAPUS (DELETED).
elif self.table[i].state == SlotState.DELETED:
# Baris 33: Jika ini adalah slot DELETED pertama yang ditemui, catat indeksnya ke variabel first_deleted.
if first_deleted == -1:
# Baris 34: Menyimpan nilai indeks i ke variabel first_deleted.
first_deleted = i
# Baris 35: Blok else ini berjalan jika menemukan slot yang benar-benar KOSONG (EMPTY).
else:
# Baris 36: Mengecek jika di sepanjang jalan tadi program sempat menemukan slot DELETED.
if first_deleted != -1:
# Baris 37: Mengalihkan target penyimpanan data ke indeks slot DELETED pertama tadi agar hemat ruang.
i = first_deleted
# Baris 38: Mengisi atribut key pada slot indeks i dengan key baru.
self.table[i].key = key
# Baris 39: Mengisi atribut value pada slot indeks i dengan value baru.
self.table[i].value = value
# Baris 40: Mengubah status slot tersebut menjadi TERISI (OCCUPIED).
self.table[i].state = SlotState.OCCUPIED
# Baris 41: Mengembalikan nilai True untuk menandakan proses input data baru sukses.
return True
# Baris 42: Mengecek di luar loop, jika tabel penuh tapi sempat menemukan slot DELETED yang tersisa.
if first_deleted != -1:
# Baris 43: Mengisi key baru ke slot DELETED tersebut.
self.table[first_deleted].key = key
# Baris 44: Mengisi value baru ke slot DELETED tersebut.
self.table[first_deleted].value = value
# Baris 45: Mengubah status slot DELETED tersebut menjadi TERISI (OCCUPIED).
self.table[first_deleted].state = SlotState.OCCUPIED
# Baris 46: Mengembalikan nilai True untuk menandakan proses berhasil.
return True
# Baris 47: Mengembalikan nilai False jika tabel benar-benar penuh total dan tidak ada slot kosong sama sekali.
return False

# Baris 49: Membuat fungsi search untuk mencari data kendaraan berdasarkan key.
def search(self, key):
# Baris 50: Menghitung nilai indeks awal target menggunakan fungsi hash.
idx = self.hash_function(key)
# Baris 51: Melakukan perulangan untuk memeriksa slot satu per satu dari indeks awal.
for step in range(self.SIZE):
# Baris 52: Menghitung indeks pergeseran (Linear Probing).
i = (idx + step) % self.SIZE
# Baris 53: Jika bertemu slot yang berstatus EMPTY, pencarian langsung dihentikan.
if self.table[i].state == SlotState.EMPTY:
# Baris 54: Mengembalikan nilai None karena data pasti tidak ada di dalam tabel.
return None
# Baris 55: Jika slot berstatus TERISI dan key di dalam slot tersebut cocok dengan key yang dicari.
if self.table[i].state == SlotState.OCCUPIED and self.table[i].key == key:
# Baris 56: Mengembalikan objek Entry lengkap (berisi key, value, state) karena data ditemukan.
return self.table[i]
# Baris 57: Mengembalikan None jika loop selesai dan seluruh isi tabel sudah diperiksa tetapi tidak ketemu.
return None

# Baris 59: Membuat fungsi remove_key untuk menghapus data kendaraan berdasarkan key.
def remove_key(self, key):
# Baris 60: Memanggil fungsi search() untuk memeriksa apakah data tersebut terdaftar di tabel.
entry = self.search(key)
# Baris 61: Jika hasil pencarian bernilai None (data tidak ditemukan).
if entry is None:
# Baris 62: Mengembalikan nilai False karena proses penghapusan gagal akibat data tidak ada.
return False
# Baris 63: Jika ketemu, ubah status slot data tersebut menjadi DIHAPUS (DELETED).
entry.state = SlotState.DELETED
# Baris 64: Mengembalikan nilai True tanda penghapusan data berhasil dilakukan.
return True

# Baris 66: Membuat fungsi display untuk mencetak visualisasi isi tabel ke terminal.
def display(self):
# Baris 67: Mencetak teks judul tabel ke layar monitor.
print("\nIsi Hash Table (Data Kendaraan):")
# Baris 68: Melakukan perulangan untuk mencetak semua isi slot dari indeks 0 sampai maksimal.
for i in range(self.SIZE):
# Baris 69: Mencetak nomor indeks slot di awal baris tanpa membuat baris baru.
print(f"{i}: ", end="")
# Baris 70: Jika status slot pada indeks i adalah EMPTY.
if self.table[i].state == SlotState.EMPTY:
# Baris 71: Mencetak tulisan "EMPTY".
print("EMPTY")
# Baris 72: Jika status slot pada indeks i adalah DELETED.
elif self.table[i].state == SlotState.DELETED:
# Baris 73: Mencetak tulisan "DELETED".
print("DELETED")
# Baris 74: Blok else dijalankan jika status slot terisi data aktif.
else:
# Baris 75: Mencetak informasi key angka dan teks value kendaraan yang disimpan.
print(f"(Key Angka: {self.table[i].key}, Info: {self.table[i].value})")

# Baris 77: Membuat fungsi helper cek_plat untuk mempermudah cetak teks hasil pencarian bagi user.
def cek_plat(self, kode_plat):
# Baris 78: Memanggil fungsi search() untuk mencari data kendaraan berdasarkan kode_plat.
hasil = self.search(kode_plat)
# Baris 79: Jika objek data kendaraan berhasil ditemukan (bukan None).
if hasil is not None:
# Baris 80: Mencetak pesan sukses beserta nilai/value dari kendaraan tersebut.
print(f"Data ditemukan -> {hasil.value}")
# Baris 81: Blok else berjalan jika pencarian menghasilkan nilai None.
else:
# Baris 82: Mencetak pesan informasi bahwa data plat motor tidak ditemukan.
print("Data plat motor tidak ditemukan!")


# Baris 85: Membuat fungsi main sebagai titik awal jalannya eksekusi program.
def main():
# Baris 86: Membuat objek bernama data_motor dengan kapasitas ukuran tabel sebanyak 10 slot.
data_motor = HashMapOpenAddressing(size=10)

# Baris 88: Memasukkan data kendaraan pertama dengan key 18 (masuk ke indeks 8 karena 18 % 10 = 8).
data_motor.insert(18, "BD 1234 XI (Honda Beat - Wijayanti)") 
# Baris 89: Memasukkan data kendaraan kedua dengan key 15 (masuk ke indeks 5 karena 15 % 10 = 5).
data_motor.insert(15, "DB 8888 XY (Yamaha NMax - Mutiara)") 
# Baris 90: Memasukkan data kendaraan ketiga dengan key 33 (masuk ke indeks 3 karena 33 % 10 = 3).
data_motor.insert(33, "BE 4571 XA (Suzuki Nex - Kirani)")
# Baris 91: Memasukkan data kendaraan keempat dengan key 49 (masuk ke indeks 9 karena 49 % 10 = 9).
data_motor.insert(49, "F 2026 FG (Vespa Sprint - Arutala)")

# Baris 93: Memanggil fungsi display untuk menampilkan kondisi tabel saat ini ke layar terminal.
data_motor.display()
# Baris 94: Mencetak garis pembatas sebanyak 50 karakter untuk merapikan tampilan log.
print("-" * 50)

# Baris 96: Mencetak teks pemberitahuan pencarian untuk data key angka 18.
print("\n[Mencari Plat Motor dengan angka 18]")
# Baris 97: Memanggil fungsi cek_plat untuk memproses dan mencetak hasil pencarian key angka 18.
data_motor.cek_plat(18)

# Baris 99: Mencetak teks pemberitahuan pencarian untuk data key angka 33.
print("\n[Mencari Plat Motor dengan angka 33]")
# Baris 100: Memanggil fungsi cek_plat untuk memproses dan mencetak hasil pencarian key angka 33.
data_motor.cek_plat(33)

# Baris 102: Mencetak teks pemberitahuan pencarian untuk data key angka 49.
print("\n[Mencari Plat Motor dengan angka (49)]")
# Baris 103: Memanggil fungsi cek_plat untuk memproses dan mencetak hasil pencarian key angka 49.
data_motor.cek_plat(49)


# Baris 106: Struktur kendali standard Python untuk memastikan fungsi main() hanya berjalan jika file ini dieksekusi secara langsung.
if __name__ == "__main__":
# Baris 107: Memanggil dan menjalankan fungsi main().
main()












