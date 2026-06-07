**Program Pengecekan Motor di Parkiran**

**Deskripsi Singkat**

Program ini adalah simulasi database kendaraan berbasis Hash Table berukuran 10 slot yang berfungsi menyimpan dan mencari data plat nomor berdasarkan kunci angka.

Struktur data ini menggunakan fungsi hash modulo untuk menentukan posisi indeks data secara cepat. Jika terjadi bentrokan indeks (collision), metode Open Addressing dengan Linear Probing akan mencari slot terdekat berikutnya secara berurutan. Keandalan sistem ini didukung oleh Manajemen Status Slot (EMPTY, OCCUPIED, DELETED) yang menjaga agar alur pencarian data tidak terputus saat ada data yang dihapus. Di akhir program, mekanisme ini langsung diuji melalui penginputan empat data motor serta simulasi pencarian kuncinya.

Source Kode

<img width="684" height="582" alt="kode 1" src="https://github.com/user-attachments/assets/e0f855eb-aa89-4b1b-af6d-8e6c728f6c43" />

<img width="722" height="518" alt="kode 2" src="https://github.com/user-attachments/assets/9a424a0f-3d45-4c00-ba0b-c791eafc422d" />

<img width="733" height="507" alt="kode 3" src="https://github.com/user-attachments/assets/4760a5eb-f870-4581-8f24-d8e75a28492b" />

<img width="638" height="480" alt="kode 4" src="https://github.com/user-attachments/assets/cf08263e-67b8-4dcd-91ed-38908282d914" />
