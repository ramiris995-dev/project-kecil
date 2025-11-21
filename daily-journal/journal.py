import json, os
from datetime import datetime

DB = "data/journal.json"

def ensure():
    os.makedirs("data", exist_ok=True)
    if not os.path.exists(DB):
        json.dump([], open(DB, "w"))

def add_entry():
    ensure()
    entries = json.load(open(DB))
    title = input("Judul: ")
    body = input("Isi jurnal (satu baris): ")
    tags = input("Tags (pisah koma): ").split(",")
    entry = {
        "title": title,
        "body": body,
        "tags": [t.strip() for t in tags if t.strip()],
        "created": datetime.now().strftime("%Y-%m-%d %H:%M")
    }
    entries.append(entry)
    json.dump(entries, open(DB, "w"), indent=4)
    print("Entry ditambahkan.")

def list_entries():
    ensure()
    entries = json.load(open(DB))
    for i, e in enumerate(entries, 1):
        print(f"{i}. {e['created']} | {e['title']} | tags: {e['tags']}")

def search_entries():
    q = input("Cari (kata di judul/body/tags): ").lower()
    entries = json.load(open(DB))
    for e in entries:
        if q in e["title"].lower() or q in e["body"].lower() or q in " ".join(e["tags"]).lower():
            print(f"- {e['created']} | {e['title']}\n  {e['body']}\n  tags: {e['tags']}")

def export_markdown():
    ensure()
    entries = json.load(open(DB))
    fname = input("Nama file markdown (default journal.md): ").strip() or "journal.md"
    with open(fname, "w") as f:
        for e in entries:
            f.write(f"## {e['title']} — {e['created']}\n\n")
            f.write(e['body'] + "\n\n")
            if e['tags']:
                f.write("Tags: " + ", ".join(e['tags']) + "\n\n")
            f.write("---\n\n")
    print("Diexport:", fname)

def menu():
    while True:
        print("""
=== DAILY JOURNAL ===
1. Tambah entry
2. List entries
3. Cari entry
4. Export ke markdown
5. Keluar
""")
        c = input("Pilih: ")
        if c == "1": add_entry()
        elif c == "2": list_entries()
        elif c == "3": search_entries()
        elif c == "4": export_markdown()
        elif c == "5": break

if __name__ == "__main__":
    menu()
