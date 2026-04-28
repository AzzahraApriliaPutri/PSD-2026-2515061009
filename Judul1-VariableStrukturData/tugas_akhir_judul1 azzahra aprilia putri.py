class Pasien:
    def __init__(self, nama):
        self.nama = nama
        self.next = None

class AntreanKlinik:
    def __init__(self):
        self.front = None  # Penunjuk pasien di depan
        self.rear = None   # Penunjuk pasien di belakang

    # Tambah antrean (Enqueue) di akhir list
    def tambah_pasien(self, nama):
        baru = Pasien(nama)
        if self.rear is None:
            self.front = self.rear = baru
        else:
            self.rear.next = baru
            self.rear = baru
        print(f"Pasien '{nama}' masuk antrean.")

    # Panggil pasien (Dequeue) di awal list
    def panggil_pasien(self):
        if self.front is None:
            print("Antrean kosong!")
            return
        
        terpanggil = self.front.nama
        self.front = self.front.next
        
        if self.front is None:
            self.rear = None
        
        print(f"Memanggil pasien: {terpanggil}")

    # Tampilkan seluruh antrean
    def lihat_antrean(self):
        if self.front is None:
            print("Antrean Kosong.")
            return
        
        print("Urutan Antrean: ", end="")
        temp = self.front
        while temp:
            print(temp.nama, end=" -> ")
            temp = temp.next
        print("Selesai")

# Contoh Penggunaan
klinik = AntreanKlinik()
klinik.tambah_pasien("Andi")
klinik.tambah_pasien("Budi")
klinik.tambah_pasien("Cici")

klinik.lihat_antrean()

klinik.panggil_pasien()
klinik.lihat_antrean()