import json, os
from datetime import datetime

DB = "data/books.json"

def ensure():
    os.makedirs("data", exist_ok=True)
    if not os.path.exists(DB):
        with open(DB, "w") as f:
            json.dump([], f)

def load():
    ensure()
    return json.load(open(DB))

def save(books):
    json.dump(books, open(DB, "w"), indent=4)

def add_book():
    books = load()
    title = input("Judul buku: ")
    author = input("Penulis: ")
    total_pages = int(input("Total halaman: "))
    books.append({
        "title": title,
        "author": author,
        "total_pages": total_pages,
        "pages_read": 0,
        "started_at": datetime.now().strftime("%Y-%m-%d"),
        "finished_at": None,
        "rating": None
    })
    save(books)
    print("Buku ditambahkan.")

def update_progress():
    books = load()
    if not books:
        print("Belum ada buku.")
        return
    for i, b in enumerate(books, 1):
        print(f"{i}. {b['title']} ({b['pages_read']}/{b['total_pages']})")
    idx = int(input("Pilih buku: ")) - 1
    pages = int(input("Tambahkan halaman dibaca (angka): "))
    books[idx]["pages_read"] = min(books[idx]["total_pages"], books[idx]["pages_read"] + pages)
    if books[idx]["pages_read"] >= books[idx]["total_pages"]:
        books[idx]["finished_at"] = datetime.now().strftime("%Y-%m-%d")
        print("Selamat, buku selesai dibaca!")
        rating = input("Beri rating (1-5) [opsional]: ").strip()
        if rating:
            books[idx]["rating"] = int(rating)
    save(books)

def list_books():
    books = load()
    for b in books:
        status = "Finished" if b["finished_at"] else "Reading"
        est = None
        if b["pages_read"] > 0 and not b["finished_at"]:
            # naive estimate: assume 50 pages/day (for example)
            left = b["total_pages"] - b["pages_read"]
            est = f"{(left // 50) + 1} days (est)"
        print(f"- {b['title']} by {b['author']} | {b['pages_read']}/{b['total_pages']} | {status} {est or ''}")

def remove_book():
    books = load()
    for i, b in enumerate(books, 1):
        print(f"{i}. {b['title']}")
    idx = int(input("Hapus nomor: ")) - 1
    books.pop(idx)
    save(books)
    print("Terhapus.")

def menu():
    while True:
        print("""
=== BOOK TRACKER ===
1. Tambah buku
2. Update progress
3. List buku
4. Hapus buku
5. Keluar
""")
        c = input("Pilih: ")
        if c == "1": add_book()
        elif c == "2": update_progress()
        elif c == "3": list_books()
        elif c == "4": remove_book()
        elif c == "5": break

if __name__ == "__main__":
    menu()
