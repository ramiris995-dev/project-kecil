import os, json, time
from datetime import datetime

META = ".notes_meta.json"
NOTES_DIR = "notes"

def ensure():
    os.makedirs(NOTES_DIR, exist_ok=True)
    if not os.path.exists(os.path.join(NOTES_DIR, META)):
        with open(os.path.join(NOTES_DIR, META), "w") as f:
            json.dump({}, f)

def load_meta():
    ensure()
    with open(os.path.join(NOTES_DIR, META), "r") as f:
        return json.load(f)

def save_meta(meta):
    with open(os.path.join(NOTES_DIR, META), "w") as f:
        json.dump(meta, f, indent=4)

def add_note():
    title = input("Judul: ").strip()
    slug = title.lower().replace(" ", "-")
    fname = f"{slug}.md"
    path = os.path.join(NOTES_DIR, fname)
    content = input("Isi catatan (satu baris, enter untuk selesai):\n")
    with open(path, "w") as f:
        f.write(content + "\n")
    meta = load_meta()
    meta[fname] = {"title": title, "tags": [], "updated": datetime.now().isoformat()}
    save_meta(meta)
    print("Catatan dibuat:", path)

def tag_note():
    meta = load_meta()
    files = list(meta.keys())
    for i, f in enumerate(files, 1):
        print(f"{i}. {meta[f]['title']} ({f})")
    idx = int(input("Pilih file: ")) - 1
    tags = input("Masukkan tag (pisah koma): ").split(",")
    meta[files[idx]]["tags"] = [t.strip() for t in tags if t.strip()]
    meta[files[idx]]["updated"] = datetime.now().isoformat()
    save_meta(meta)
    print("Tag disimpan.")

def search_tag():
    meta = load_meta()
    q = input("Cari tag: ").strip().lower()
    results = [k for k,v in meta.items() if q in " ".join(v.get("tags", [])).lower()]
    if not results:
        print("Tidak ada.")
        return
    for r in results:
        print(r, "→", meta[r])

def list_notes():
    meta = load_meta()
    for f, m in meta.items():
        print(f"{m['title']} | tags: {m.get('tags', [])} | updated: {m['updated']}")

def menu():
    while True:
        print("""
=== MINI NOTES SYNC ===
1. Tambah note
2. Tag note
3. Cari tag
4. List notes
5. Keluar
""")
        c = input("Pilih: ")
        if c == "1": add_note()
        elif c == "2": tag_note()
        elif c == "3": search_tag()
        elif c == "4": list_notes()
        elif c == "5": break

if __name__ == "__main__":
    menu()
