import json, os, datetime

DB = "data/notes.json"

def load_notes():
    if not os.path.exists(DB):
        return []
    with open(DB, "r") as f:
        return json.load(f)

def save_notes(notes):
    with open(DB, "w") as f:
        json.dump(notes, f, indent=4)

def add_note():
    notes = load_notes()
    title = input("Judul: ")
    content = input("Isi catatan: ")
    created = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    notes.append({"title": title, "content": content, "created": created})
    save_notes(notes)
    print("Catatan ditambahkan.")

def list_notes():
    notes = load_notes()
    print("\n=== DAFTAR CATATAN ===")
    for i, n in enumerate(notes, 1):
        print(f"{i}. {n['title']} ({n['created']})")
    print()

def search_notes():
    q = input("Cari judul: ").lower()
    notes = load_notes()
    results = [n for n in notes if q in n["title"].lower()]
    if not results:
        print("Tidak ditemukan.")
        return
    for n in results:
        print("\nJudul:", n["title"])
        print("Isi:", n["content"])
        print("Tanggal:", n["created"])

def delete_note():
    notes = load_notes()
    list_notes()
    idx = int(input("Hapus nomor: ")) - 1
    notes.pop(idx)
    save_notes(notes)
    print("Catatan dihapus.")

def menu():
    while True:
        print("""
1. Lihat Catatan
2. Tambah Catatan
3. Cari Catatan
4. Hapus Catatan
5. Keluar
""")
        c = input("Pilih: ")
        if c == "1": list_notes()
        elif c == "2": add_note()
        elif c == "3": search_notes()
        elif c == "4": delete_note()
        elif c == "5": break
        else: print("Pilihan tidak valid.")

menu()
