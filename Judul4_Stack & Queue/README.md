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

















**OUTPUT**

<img width="640" height="600" alt="output 1" src="https://github.com/user-attachments/assets/03bac765-7e84-44dd-b798-b3e19269c064" />

<img width="576" height="162" alt="output 2" src="https://github.com/user-attachments/assets/f328e3e2-3717-4a60-90b0-134ad62874a2" />

<img width="594" height="171" alt="output 3" src="https://github.com/user-attachments/assets/49cbca31-111a-445b-8d48-4771ed2f9c10" />


