rates = {
    "USD_IDR": 16000,
    "IDR_USD": 1/16000
}

def convert():
    print("1. USD -> IDR\n2. IDR -> USD")
    c = input("Pilih: ")
    amt = float(input("Jumlah: "))

    if c == "1":
        print("Hasil:", amt * rates["USD_IDR"])
    else:
        print("Hasil:", amt * rates["IDR_USD"])

convert()
