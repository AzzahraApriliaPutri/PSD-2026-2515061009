class QueueArray:
    def __init__(self, max_size=10):  
        self.MAXN = max_size
        self.q = [None] * self.MAXN
        self.front_idx = -1
        self.rear_idx = -1
        self.nomor_terakhir = 0  

    def is_empty(self):
        return self.front_idx == -1

    def is_full(self):
        return (self.rear_idx + 1) % self.MAXN == self.front_idx

    def enqueue(self):
        if self.is_full():
            print("❌ Ruang tunggu penuh! Mohon tunggu nasabah lain selesai dilayani.")
            return
        
        self.nomor_terakhir += 1
        kode_antrean = f"B-{self.nomor_terakhir}"
        
        if self.is_empty():
            self.front_idx = 0
            self.rear_idx = 0
        else:
            self.rear_idx = (self.rear_idx + 1) % self.MAXN
            
        self.q[self.rear_idx] = kode_antrean
        print(f"🎫 Tiket dicetak! Nomor {kode_antrean} silakan duduk di ruang tunggu.")

    def dequeue(self):
        if self.is_empty():
            print("📭 Antrean kosong. Seluruh nasabah sudah dilayani.")
            return
            
        nasabah_dilayani = self.q[self.front_idx]
        print(f"🔔 [PANGGILAN]: Nomor antrean {nasabah_dilayani}, silakan menuju ke Teller/CS.")
        
        if self.front_idx == self.rear_idx:
            self.front_idx = -1
            self.rear_idx = -1
        else:
            self.front_idx = (self.front_idx + 1) % self.MAXN

    def peek(self):
        if self.is_empty():
            print("📭 Tidak ada nasabah yang menunggu.")
            return
        print(f"👀 Giliran berikutnya yang akan dipanggil: {self.q[self.front_idx]}")

    def display(self):
        if self.is_empty():
            print("📭 Ruang tunggu kosong.")
            return
        print("📋 Daftar nomor antrean di ruang tunggu: ", end="")
        i = self.front_idx
        while True:
            print(f"[{self.q[i]}]", end=" ")
            if i == self.rear_idx:
                break
            i = (i + 1) % self.MAXN
        print()


def main():
    antrean_bank = QueueArray(max_size=10)
    pilih = 0
    
    while pilih != 5:
        print("\n=== SISTEM ANTREAN BANK ===")
        print("1. Ambil Nomor Antrean (Nasabah Datang)")
        print("2. Panggil Antrean Berikutnya (Oleh Teller/CS)")
        print("3. Cek Nomor yang Akan Dipanggil Berikutnya")
        print("4. Lihat Seluruh Sisa Antrean")
        print("5. Selesai Operasional Bank")
        
        try:
            pilih = int(input("Pilih menu (1-5): "))
        except ValueError:
            print("Input harus berupa angka!")
            continue
            
        if pilih == 1:
            antrean_bank.enqueue()  
        elif pilih == 2:
            antrean_bank.dequeue()
        elif pilih == 3:
            antrean_bank.peek()
        elif pilih == 4:
            antrean_bank.display()
        elif pilih == 5:
            print("Bank ditutup. Sampai jumpa besok!")
        else:
            print("Pilihan menu tidak valid!")


if __name__ == "__main__":
    main()