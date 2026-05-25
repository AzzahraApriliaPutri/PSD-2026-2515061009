class Node:
    def __init__(self, key, nama_tugas, deskripsi):
        self.key = key  
        self.nama_tugas = nama_tugas
        self.deskripsi = deskripsi
        self.left = None
        self.right = None


class BSTLanjut:
    def __init__(self):
        self.root = None

    def insert_node(self, root, key, nama_tugas, deskripsi):
        if root is None:
            return Node(key, nama_tugas, deskripsi)
        if key < root.key:
            root.left = self.insert_node(root.left, key, nama_tugas, deskripsi)
        elif key > root.key:
            root.right = self.insert_node(root.right, key, nama_tugas, deskripsi)
        else:
            print(f"\n[Peringatan] ID Prioritas {key} sudah digunakan oleh tugas lain!")
        return root

    def insert(self, key, nama_tugas, deskripsi):
        self.root = self.insert_node(self.root, key, nama_tugas, deskripsi)

    def find_min_node(self, root):
        current = root
        while current is not None and current.left is not None:
            current = current.left
        return current

    def delete_node(self, root, key):
        if root is None:
            return None
        if key < root.key:
            root.left = self.delete_node(root.left, key)
        elif key > root.key:
            root.right = self.delete_node(root.right, key)
        else:
            if root.left is None and root.right is None:
                return None
            elif root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            else:
                successor = self.find_min_node(root.right)
                root.key = successor.key
                root.nama_tugas = successor.nama_tugas
                root.deskripsi = successor.deskripsi
                root.right = self.delete_node(root.right, successor.key)
        return root

    def delete(self, key):
        self.root = self.delete_node(self.root, key)

    def height(self, root):
        if root is None:
            return -1
        height_left = self.height(root.left)
        height_right = self.height(root.right)
        return 1 + max(height_left, height_right)

    def level_order(self, root):
        if root is None:
            print("(kosong)")
            return
        queue = []
        queue.append(root)
        while len(queue) > 0:
            current = queue.pop(0)
            print(f"[{current.key}: {current.nama_tugas}]", end=" ")
            if current.left is not None:
                queue.append(current.left)
            if current.right is not None:
                queue.append(current.right)
        print()

    def inorder_tugas(self, root):
        if root:
            self.inorder_tugas(root.left)
            print(f"| Prio: {root.key:<3} | {root.nama_tugas:<20} | {root.deskripsi:<30} |")
            self.inorder_tugas(root.right)

    def find_successor(self, root, key):
        current = root
        successor = None
        while current is not None:
            if key < current.key:
                successor = current
                current = current.left
            elif key > current.key:
                current = current.right
            else:
                break
        if current is None:
            return None, False
        if current.right is not None:
            successor = self.find_min_node(current.right)
        if successor is None:
            return None, False
        return successor, True

    def find_predecessor(self, root, key):
        current = root
        predecessor = None
        while current is not None:
            if key > current.key:
                predecessor = current
                current = current.right
            elif key < current.key:
                current = current.left
            else:
                break
        if current is None:
            return None, False
        if current.left is not None:
            temp = current.left
            while temp.right is not None:
                temp = temp.right
            predecessor = temp
        if predecessor is None:
            return None, False
        return predecessor, True


def main():
    bst = BSTLanjut()
    
    bst.insert(5, "Belajar Ujian", "Bab 1 sampai 5 matematika")
    bst.insert(3, "Beli Susu", "Titipan Ibu di minimarket")
    bst.insert(8, "Project Akhir", "Coding modul BST Aplikasi")

    pilih = 0
    while pilih != 7:
        print("\n=======================================================")
        print("          APLIKASI MANAJEMEN TUGAS (BST)               ")
        print("=======================================================")
        print("1. Tambah Tugas Baru (Insert)")
        print("2. Selesaikan / Hapus Tugas (Delete)")
        print("3. Lihat Daftar Semua Tugas (Urutan Prioritas)")
        print("4. Struktur Kedalaman Pohon Tugas (Height & Level-Order)")
        print("5. Cari Tugas Mendesak Berikutnya (Successor)")
        print("6. Cari Tugas Santai Sebelumnya (Predecessor)")
        print("7. Keluar")
        print("-------------------------------------------------------")
        
        try:
            pilih = int(input("Pilih Menu (1-7): "))
        except ValueError:
            print("Input tidak valid! Masukkan angka.")
            continue
            
        if pilih == 1:
            try:
                prio = int(input("Masukkan ID Prioritas (Angka, misal 1=Mendesak, 10=Santai): "))
                nama = input("Masukkan Nama Tugas: ")
                deskripsi = input("Masukkan Deskripsi Tugas: ")
                bst.insert(prio, nama, deskripsi)
                print(f"\n[Sukses] Tugas '{nama}' berhasil ditambahkan ke daftar!")
            except ValueError:
                print("Input tidak valid! Prioritas harus berupa angka.")
                
        elif pilih == 2:
            try:
                prio = int(input("Masukkan ID Prioritas tugas yang telah selesai/dihapus: "))
                bst.delete(prio)
                print(f"\n[Sukses] Tugas dengan prioritas {prio} berhasil dihapus.")
            except ValueError:
                print("Input tidak valid!")
                
        elif pilih == 3:
            print("\n================== DAFTAR TUGAS AKTIF ==================")
            if bst.root is None:
                print(" Tidak ada tugas saat ini. Bersih!")
            else:
                print(f"| {'ID':<9} | {'Nama Tugas':<20} | {'Deskripsi':<30} |")
                print("-" * 68)
                bst.inorder_tugas(bst.root)
            print("========================================================")
            
        elif pilih == 4:
            print(f"\nTinggi Struktur Pohon Tugas (Height): {bst.height(bst.root)}")
            print("Struktur Penyelusuran (Level-order): ", end="")
            bst.level_order(bst.root)
            
        elif pilih == 5:
            try:
                x = int(input("Cari tugas yang tingkat urgensinya di bawah ID Prioritas: "))
                node_ans, found = bst.find_successor(bst.root, x)
                if found:
                    print(f"\nTugas pengganti terdekat berikutnya:")
                    print(f"-> ID Prioritas: {node_ans.key}")
                    print(f"-> Nama Tugas  : {node_ans.nama_tugas}")
                else:
                    print("\nTidak ada tugas berikutnya (Ini adalah tugas dengan prioritas paling bawah).")
            except ValueError:
                print("Input tidak valid!")
                
        elif pilih == 6:
            try:
                x = int(input("Cari tugas yang tingkat urgensinya di atas ID Prioritas: "))
                node_ans, found = bst.find_predecessor(bst.root, x)
                if found:
                    print(f"\nTugas lebih penting sebelumnya:")
                    print(f"-> ID Prioritas: {node_ans.key}")
                    print(f"-> Nama Tugas  : {node_ans.nama_tugas}")
                else:
                    print("\nTidak ada tugas sebelumnya (Ini sudah merupakan tugas paling prioritas/penting).")
            except ValueError:
                print("Input tidak valid!")
                
        elif pilih == 7:
            print("\nTerima kasih telah menggunakan aplikasi manajemen tugas!")
        else:
            print("Pilihan menu tidak tersedia!")


if __name__ == "__main__":
    main()