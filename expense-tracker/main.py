import json, os, datetime

DB = "data/expenses.json"

def load():
    if not os.path.exists(DB):
        return []
    return json.load(open(DB))

def save(data):
    json.dump(data, open(DB, "w"), indent=4)

def add_expense():
    data = load()
    amount = float(input("Jumlah (Rp): "))
    category = input("Kategori (makan, transport, dll): ")
    note = input("Catatan: ")
    date = datetime.datetime.now().strftime("%Y-%m-%d")

    data.append({
        "amount": amount,
        "category": category,
        "note": note,
        "date": date
    })

    save(data)
    print("Pengeluaran ditambahkan.\n")

def summary():
    data = load()
    total = sum(d["amount"] for d in data)
    print(f"Total Pengeluaran: Rp {total:,.0f}\n")

def monthly_report():
    data = load()
    month = input("Masukkan bulan (YYYY-MM): ")
    filtered = [d for d in data if d["date"].startswith(month)]

    if not filtered:
        print("Tidak ada data.")
        return

    print(f"\n=== Laporan {month} ===")
    for d in filtered:
        print(f"- {d['date']}: Rp{d['amount']} ({d['category']}) - {d['note']}")

def menu():
    while True:
        print("""
1. Tambah Pengeluaran
2. Total Pengeluaran
3. Laporan Bulanan
4. Keluar
""")
        c = input("Pilih: ")
        if c == "1": add_expense()
        elif c == "2": summary()
        elif c == "3": monthly_report()
        elif c == "4": break

menu()
