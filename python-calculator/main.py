def calc():
    while True:
        print("\n=== KALKULATOR ===")
        print("1. Tambah\n2. Kurang\n3. Kali\n4. Bagi\n5. Keluar")
        c = input("Pilih: ")

        if c == "5":
            break

        a = float(input("Angka 1: "))
        b = float(input("Angka 2: "))

        if c == "1": print("Hasil:", a + b)
        elif c == "2": print("Hasil:", a - b)
        elif c == "3": print("Hasil:", a * b)
        elif c == "4":
            if b == 0: print("Tidak bisa bagi 0")
            else: print("Hasil:", a / b)

calc()
