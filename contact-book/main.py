import json
import os

FILE = "contacts.json"

def load():
    if not os.path.exists(FILE):
        return []
    return json.load(open(FILE))

def save(c):
    json.dump(c, open(FILE, "w"), indent=4)

def menu():
    contacts = load()
    while True:
        print("\n1. Lihat\n2. Tambah\n3. Cari\n4. Keluar")
        c = input("Pilih: ")

        if c == "1":
            for d in contacts:
                print(d["name"], "-", d["phone"])

        elif c == "2":
            name = input("Nama: ")
            phone = input("Telp: ")
            contacts.append({"name": name, "phone": phone})
            save(contacts)

        elif c == "3":
            q = input("Cari nama: ")
            for d in contacts:
                if q.lower() in d["name"].lower():
                    print(d["name"], "-", d["phone"])

        else:
            break

menu()
