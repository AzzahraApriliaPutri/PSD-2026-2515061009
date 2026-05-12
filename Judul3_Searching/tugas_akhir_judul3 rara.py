def cari_harga_barang(daftar_harga, n, harga_target):
    l = 0
    r = n - 1
    posisi = -1
    
    print(f"\n--- Memulai Pencarian Harga: Rp{harga_target} ---")
    
    while l <= r:
        m = l + (r - l) // 2
        print(f"Mengecek harga di indeks {m}: Rp{daftar_harga[m]}")
        
        if daftar_harga[m] == harga_target:
            posisi = m
            break
        elif daftar_harga[m] < harga_target:
            print(f"Rp{daftar_harga[m]} terlalu murah, mencari ke rentang harga lebih tinggi.")
            l = m + 1
        else:
            print(f"Rp{daftar_harga[m]} terlalu mahal, mencari ke rentang harga lebih rendah.")
            r = m - 1
            
    return posisi

def main():
    print("=== SISTEM PENCARIAN HARGA KATALOG (BINARY SEARCH) ===")
    try:
        n = int(input("Masukkan jumlah produk dalam katalog: "))
    except ValueError:
        print("Error: Harap masukkan angka untuk jumlah produk!")
        return

    harga_produk = []
    print(f"\nMasukkan {n} harga produk (HARUS BERURUTAN dari termurah):")
    for i in range(n):
        while True:
            try:
                harga = int(input(f"Harga produk ke-{i+1}: Rp"))
                if i > 0 and harga < harga_produk[i-1]:
                    print(f"Peringatan: Harga harus lebih besar atau sama dengan Rp{harga_produk[i-1]}!")
                    continue
                harga_produk.append(harga)
                break
            except ValueError:
                print("Input tidak valid! Masukkan angka harga saja.")

    print(f"\nKatalog Harga Saat Ini: {harga_produk}")

    while True:
        try:
            target = int(input("\nMasukkan harga yang ingin dicari: Rp"))
            break
        except ValueError:
            print("Input tidak valid!")

    hasil = cari_harga_barang(harga_produk, n, target)

    if hasil != -1:
        print(f"\nSelesai: Harga Rp{target} ditemukan pada katalog urutan ke-{hasil + 1}.")
    else:
        print(f"\nSelesai: Harga Rp{target} tidak tersedia dalam katalog kami.")

if __name__ == "__main__":
    main()