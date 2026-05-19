**PROGRAM SIMULASI ANTREAN BANK**

**DESKRIPSI SINGKAT**

Aplikasi Simulasi Manajemen Antrean Bank ini dirancang untuk memodelkan sistem pencetakan tiket otomatis di dunia perbankan secara berbasis teks. Sistem secara otomatis akan menerbitkan nomor urut nasabah baru (B-1, B-2, dst.) ke dalam daftar tunggu saat mereka tiba. Proses pemanggilan oleh Teller atau Customer Service menerapkan aturan prioritas, di mana nasabah yang mengantre paling awal akan dilayani lebih dulu sampai seluruh antrean terselesaikan. 

Struktur data yang digunakan adalah Queue yang mempunya prinsip FIFO (First In First Out) yang sesuai untuk antrean di bank dimana nasabah pertama yang masuk ke antrean akan dilayani terlebih dahulu kemudian nasabah selanjutnya akan dimasukkan ke antrean belakang.

**SOURCE KODE**

<img width="813" height="536" alt="kode 1" src="https://github.com/user-attachments/assets/4a75e976-047b-48a8-90a7-7e28c923a7ed" />

<img width="834" height="513" alt="kode 2" src="https://github.com/user-attachments/assets/6b60cfad-efa2-4765-8455-843921d16460" />

<img width="706" height="518" alt="kode 3" src="https://github.com/user-attachments/assets/aa8b6351-9864-4319-8ce7-e67be3c745e0" />

<img width="600" height="384" alt="kode 4" src="https://github.com/user-attachments/assets/dc9219b4-3df9-41b1-8061-b9887702b37a" />

Baris 1: class QueueArray: $\rightarrow$ Deklarasi kelas bernama QueueArray untuk membuat objek antrean melingkar berbasis array.

Baris 2: def __init__(self, max_size=10): $\rightarrow$ Fungsi constructor yang otomatis berjalan saat objek antrean dibuat. Secara default, batas maksimal antrean diatur sebanyak 10.

Baris 3: self.MAXN = max_size $\rightarrow$ Menyimpan kapasitas maksimal antrean ke dalam variabel variabel objek MAXN.

Baris 4: self.q = [None] * self.MAXN $\rightarrow$ Membuat array (list) kosong sepanjang isi MAXN berisi nilai None sebagai wadah memori antrean.

Baris 5 & 6: self.front_idx = -1 dan self.rear_idx = -1 $\rightarrow$ Mengatur penanda indeks depan (front) dan belakang (rear) ke angka -1, menandakan antrean masih benar-benar kosong.

Baris 7: self.nomor_terakhir = 0 $\rightarrow$ Membuat variabel counter untuk melacak nomor tiket terakhir yang berhasil dicetak.

Baris 9 & 10: def is_empty(self): $\rightarrow$ Fungsi untuk mengecek apakah antrean kosong. Jika front_idx == -1, fungsi akan mengembalikan nilai True.

Baris 12 & 13: def is_full(self): $\rightarrow$ Fungsi untuk mengecek apakah antrean penuh. Menggunakan rumus modulo (rear_idx + 1) % MAXN. Jika hasil rumus tersebut sama dengan posisi front_idx, berarti array sudah melingkar penuh dan mengembalikan nilai True.

Baris 15: def enqueue(self): $\rightarrow$ Fungsi untuk memasukkan nasabah baru ke dalam antrean.

Baris 16–18: Mengecek if self.is_full():. Jika penuh, program mencetak pesan peringatan "Ruang tunggu penuh!..." dan langsung menghentikan fungsi (return) agar data tidak meluber.

Baris 20: self.nomor_terakhir += 1 $\rightarrow$ Nilai counter tiket ditambah 1 (misal dari 0 menjadi 1).

Baris 21: kode_antrean = f"B-{self.nomor_terakhir}" $\rightarrow$ Membuat format string untuk nomor tiket baru (contoh: "B-1").

Baris 23–25: if self.is_empty(): $\rightarrow$ Jika nasabah tersebut adalah orang pertama di antrean yang kosong, posisi indeks front_idx dan rear_idx dipindah bersamaan ke titik awal, yaitu indeks 0.

Baris 26–27: else: $\rightarrow$ Jika antrean sudah ada isinya, posisi indeks belakang (rear_idx) digeser maju satu langkah menggunakan logika melingkar: (rear_idx + 1) % MAXN.

Baris 29: self.q[self.rear_idx] = kode_antrean $\rightarrow$ Memasukkan string kode antrean (misal: "B-1") ke dalam array pada indeks rear_idx yang baru.

Baris 30: Mencetak pemberitahuan ke layar bahwa tiket berhasil dicetak dan nasabah dipersilakan duduk.

Baris 32: def dequeue(self): $\rightarrow$ Fungsi untuk memanggil dan mengeluarkan nasabah di urutan paling depan.

Baris 33–35: Mengecek if self.is_empty():. Jika tidak ada antrean, program menampilkan pesan "Antrean kosong..." dan langsung keluar lewat perintah return.

Baris 37: nasabah_dilayani = self.q[self.front_idx] $\rightarrow$ Mengambil data kode antrean yang berada di posisi paling depan (front_idx) untuk disimpan sementara.

Baris 38: Mencetak suara panggilan ke layar: "[PANGGILAN]: Nomor antrean X, silakan...".

Baris 40–42: if self.front_idx == self.rear_idx: $\rightarrow$ Kondisi jika nomor yang dipanggil adalah satu-satunya orang terakhir di dalam antrean. Jika benar, setelah dia keluar, status antrean diatur kembali ke kondisi kosong awal (front_idx = -1 dan rear_idx = -1).

Baris 43–44: else: $\rightarrow$ Jika masih ada nasabah lain di belakangnya, indeks depan (front_idx) digeser maju satu baris dengan rumus melingkar (front_idx + 1) % MAXN untuk bersiap ke antrean selanjutnya.

Baris 46: def peek(self): $\rightarrow$ Fungsi untuk melihat siapa yang ada di antrean paling depan tanpa memanggilnya keluar.

Baris 47–49: Jika antrean kosong, cetak pemberitahuan dan batalkan perintah (return).

Baris 50: Jika ada, cetak data yang ditunjuk oleh indeks depan: self.q[self.front_idx].

Baris 52: def display(self): $\rightarrow$ Fungsi untuk melihat seluruh daftar nomor yang sedang duduk menunggu di dalam ruang tamu.

Baris 53–55: Jika ruang tunggu kosong (is_empty()), cetak "Ruang tunggu kosong." lalu berhenti.

Baris 56: Mencetak teks judul awal sebelum menampilkan daftar nomor.Baris 57: i = self.front_idx $\rightarrow$ Membuat variabel indeks bantuan bernama i yang nilainya dimulai dari posisi paling depan (front_idx).

Baris 58: while True: $\rightarrow$ Memulai perulangan tanpa batas untuk menelusuri array melingkar.

Baris 59: print(f"[{self.q[i]}]", end=" ") $\rightarrow$ Mencetak kode antrean pada indeks i saat ini ke layar secara horizontal.

Baris 60–61: if i == self.rear_idx: break $\rightarrow$ Titik Henti: Jika indeks i sudah berjalan dan sampai di posisi indeks paling belakang (rear_idx), perulangan dipaksa berhenti karena semua data sudah tercetak.

Baris 62: i = (i + 1) % self.MAXN $\rightarrow$ Jika belum sampai belakang, indeks bantuan i digeser maju satu langkah secara melingkar untuk membaca data berikutnya pada perulangan selanjutnya.

Baris 63: print() $\rightarrow$ Mencetak baris baru di akhir agar tampilan menu berikutnya rapi.

Baris 66: def main(): $\rightarrow$ Fungsi utama yang mengendalikan alur interaksi program dengan pengguna.

Baris 67: antrean_bank = QueueArray(max_size=10) $\rightarrow$ Membuat objek tiruan sistem bernama antrean_bank dengan kapasitas 10 slot.

Baris 68: pilih = 0 $\rightarrow$ Menyiapkan variabel pilihan menu awal.

Baris 70: while pilih != 5: $\rightarrow$ Selama pengguna tidak memilih angka 5, aplikasi akan terus berputar menampilkan menu.

Baris 71–76: Perintah print(...) berturut-turut untuk mencetak visual antarmuka pilihan menu 1 sampai 5 ke layar monitor.

Baris 78–79: try: pilih = int(input(...)) $\rightarrow$ Blok pengaman untuk membaca input angka dari pengguna dan menyimpannya ke variabel pilih.

Baris 80–82: except ValueError: ... continue $\rightarrow$ Jika pengguna salah mengetik (misal mengetik huruf/simbol), program tidak akan eror/keluar, melainkan memunculkan teks "Input harus berupa angka!" dan langsung melompat kembali ke awal perulangan menu.

Baris 84–85: if pilih == 1: $\rightarrow$ Jika menekan angka 1, sistem menjalankan fungsi antrean_bank.enqueue() (menambah nasabah baru).

Baris 86–87: elif pilih == 2: $\rightarrow$ Jika menekan angka 2, sistem menjalankan fungsi antrean_bank.dequeue() (teller memanggil nasabah depan).

Baris 88–89: elif pilih == 3: $\rightarrow$ Jika menekan angka 3, sistem menjalankan fungsi antrean_bank.peek() (melihat target panggilan selanjutnya).

Baris 90–91: elif pilih == 4: $\rightarrow$ Jika menekan angka 4, sistem menjalankan fungsi antrean_bank.display() (menampilkan semua nomor di ruang tunggu).

Baris 92–93: elif pilih == 5: $\rightarrow$ Jika menekan angka 5, kondisi perulangan while menjadi salah, program mencetak "Bank ditutup..." dan keluar dari perulangan.

Baris 94–95: else: print(...) $\rightarrow$ Menangani kasus jika pengguna memasukkan angka di luar 1-5 (misal mengetik angka 9), maka sistem memunculkan pesan "Pilihan menu tidak valid!".

Baris 98–99: if __name__ == "__main__": main() $\rightarrow$ Struktur standar Python untuk memastikan bahwa fungsi main() di atas langsung dieksekusi secara otomatis saat file script ini dijalankan.


**OUTPUT**

<img width="640" height="600" alt="output 1" src="https://github.com/user-attachments/assets/03bac765-7e84-44dd-b798-b3e19269c064" />

<img width="576" height="162" alt="output 2" src="https://github.com/user-attachments/assets/f328e3e2-3717-4a60-90b0-134ad62874a2" />

<img width="594" height="171" alt="output 3" src="https://github.com/user-attachments/assets/49cbca31-111a-445b-8d48-4771ed2f9c10" />

Output diatas adalah bentuk antrean di bank, dimana user akan memilih menu 1 untuk menginputkan nasabah yang akan masuk di bank. Didalam program user memasukkan 3 orang kedalam antrean yang memiliki nomer antrean [B-1, B-2, B-3].
Kemudian teller memanggil antrean pertama (B-1) dan orang tersebut menuju ke teller untuk dilayani, saat kondisi ini antrean no B-1 sudah keluar dari daftar ruang tunggu atau daftar antrean dan tersisa antrean B-2 dan B-3.
Selanjutnya user bisa mengecek sisa orang yang masih di dalam antrean untuk dipanggil giliran berikutnya. Maka dilayar akan kelihatan antrean B-2 siap-siap giliran berikutnya untuk dilayani

https://youtu.be/3DzkGHMJV2M?si=mYZUBgXpmwmQ0G4T
