def insertion_sort(arr, n): 
    for i in range(1, n): 
        temp = arr[i] 
        j = i - 1 
        while j >= 0 and arr[j] > temp: 
            arr[j + 1] = arr[j] 
            j -= 1 
        arr[j + 1] = temp 
 
 
def main(): 
    try: 
        n = int(input("Masukkan jumlah pemain bola: ")) 
    except ValueError: 
        print("Input tidak valid!") 
        return 
    arr = [] 
    print("Masukkan angka jersey:") 
    for i in range(n): 
        while True: 
            try: 
                angka_jersey = int(input()) 
                arr.append(angka_jersey) 
                break 
            except ValueError: 
                print("Input tidak valid, silakan masukkan angka!") 
    print(f"Jersey sebelum diurutkan: {arr}") 
    insertion_sort(arr, n) 
    print("Jersey setelah diurutkan (Insertion Sort):", end=" ") 
    for i in range(n): 
        print(arr[i], end=" ") 
    print() 
 
 
if __name__ == "__main__": 
    main()