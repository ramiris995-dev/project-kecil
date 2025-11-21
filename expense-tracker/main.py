import json
import os
from datetime import datetime

DATA_FILE = "data.json"

def load_data():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r") as f:
        return json.load(f)

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

def add_transaction(type_, amount, note):
    data = load_data()
    transaction = {
        "type": type_,
        "amount": amount,
        "note": note,
        "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    data.append(transaction)
    save_data(data)
    print("Transaksi berhasil ditambahkan!")

def view_transactions():
    data = load_data()
    if not data:
        print("Belum ada transaksi.")
        return

    print("\n=== Daftar Transaksi ===")
    for i, t in enumerate(data, 1):
        print(f"{i}. {t['date']} | {t['type']} | {t['amount']} | {t['note']}")
    print()

def calculate_balance():
    data = load_data()
    income = sum(t["amount"] for t in data if t["type"] == "income")
    expense = sum(t["amount"] for t in data if t["type"] == "expense")
    balance = income - expense

    print(f"\nTotal Pemasukan: {income}")
    print(f"Total Pengeluaran: {expense}")
    print(f"Saldo: {balance}\n")

def menu():
    while True:
        print("\n=== EXPENSE TRACKER ===")
        print("1. Lihat transaksi")
        print("2. Tambah pemasukan")
        print("3. Tambah pengeluaran")
        print("4. Lihat saldo")
        print("5. Keluar")

        choice = input("Pilih menu: ")

        if choice == "1":
            view_transactions()
        elif choice == "2":
            amount = float(input("Jumlah pemasukan: "))
            note = input("Catatan: ")
            add_transaction("income", amount, note)
        elif choice == "3":
            amount = float(input("Jumlah pengeluaran: "))
            note = input("Catatan: ")
            add_transaction("expense", amount, note)
        elif choice == "4":
            calculate_balance()
        elif choice == "5":
            break
        else:
            print("Pilihan tidak valid!")

if __name__ == "__main__":
    menu()
