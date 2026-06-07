class SlotState:
    EMPTY = 0
    OCCUPIED = 1
    DELETED = 2


class Entry:
    def __init__(self):
        self.key = None
        self.value = None
        self.state = SlotState.EMPTY


class HashMapOpenAddressing:
    def __init__(self, size=10):
        self.SIZE = size
        self.table = [Entry() for _ in range(self.SIZE)]

    def hash_function(self, key):
        return (key % self.SIZE + self.SIZE) % self.SIZE

    def insert(self, key, value):
        idx = self.hash_function(key)
        first_deleted = -1
        for step in range(self.SIZE):
            i = (idx + step) % self.SIZE
            if self.table[i].state == SlotState.OCCUPIED:
                if self.table[i].key == key:
                    self.table[i].value = value
                    return True
            elif self.table[i].state == SlotState.DELETED:
                if first_deleted == -1:
                    first_deleted = i
            else:
                if first_deleted != -1:
                    i = first_deleted
                self.table[i].key = key
                self.table[i].value = value
                self.table[i].state = SlotState.OCCUPIED
                return True
        if first_deleted != -1:
            self.table[first_deleted].key = key
            self.table[first_deleted].value = value
            self.table[first_deleted].state = SlotState.OCCUPIED
            return True
        return False

    def search(self, key):
        idx = self.hash_function(key)
        for step in range(self.SIZE):
            i = (idx + step) % self.SIZE
            if self.table[i].state == SlotState.EMPTY:
                return None
            if self.table[i].state == SlotState.OCCUPIED and self.table[i].key == key:
                return self.table[i]
        return None

    def remove_key(self, key):
        entry = self.search(key)
        if entry is None:
            return False
        entry.state = SlotState.DELETED
        return True

    def display(self):
        print("\nIsi Hash Table (Data Kendaraan):")
        for i in range(self.SIZE):
            print(f"{i}: ", end="")
            if self.table[i].state == SlotState.EMPTY:
                print("EMPTY")
            elif self.table[i].state == SlotState.DELETED:
                print("DELETED")
            else:
                print(f"(Key Angka: {self.table[i].key}, Info: {self.table[i].value})")


    def cek_plat(self, kode_plat):
        hasil = self.search(kode_plat)
        if hasil is not None:
            print(f"Data ditemukan -> {hasil.value}")
        else:
            print("Data plat motor tidak ditemukan!")


def main():
    data_motor = HashMapOpenAddressing(size=10)
    
    data_motor.insert(18, "BD 1234 XI (Honda Beat - Wijayanti)")  
    data_motor.insert(15, "DB 8888 XY (Yamaha NMax - Mutiara)")  
    data_motor.insert(33, "BE 4571 XA (Suzuki Nex - Kirani)")
    data_motor.insert(49, "F 2026 FG (Vespa Sprint - Arutala)")
    
    data_motor.display()
    print("-" * 50)

    print("\n[Mencari Plat Motor dengan angka 18]")
    data_motor.cek_plat(18)

    print("\n[Mencari Plat Motor dengan angka 33]")
    data_motor.cek_plat(33)

    print("\n[Mencari Plat Motor dengan angka (49)]")
    data_motor.cek_plat(49)


if __name__ == "__main__":
    main()