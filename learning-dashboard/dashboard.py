import json, os
from datetime import datetime

DB = "data/topics.json"

def ensure():
    os.makedirs("data", exist_ok=True)
    if not os.path.exists(DB):
        json.dump([], open(DB, "w"))

def load():
    ensure()
    return json.load(open(DB))

def save(t):
    json.dump(t, open(DB, "w"), indent=4)

def add_topic():
    topics = load()
    name = input("Topik: ")
    difficulty = input("Tingkat (easy/medium/hard): ")
    total_steps = int(input("Total langkah/bab: "))
    topics.append({
        "name": name,
        "difficulty": difficulty,
        "total_steps": total_steps,
        "completed_steps": 0,
        "started": datetime.now().strftime("%Y-%m-%d")
    })
    save(topics)
    print("Topik ditambahkan.")

def mark_step():
    topics = load()
    for i, t in enumerate(topics, 1):
        print(f"{i}. {t['name']} ({t['completed_steps']}/{t['total_steps']})")
    idx = int(input("Pilih topik: ")) - 1
    steps = int(input("Tambah berapa langkah?: "))
    topics[idx]["completed_steps"] = min(topics[idx]["total_steps"], topics[idx]["completed_steps"] + steps)
    save(topics)
    print("Diupdate.")

def show_dashboard():
    topics = load()
    for t in topics:
        pct = int((t["completed_steps"] / t["total_steps"]) * 100) if t["total_steps"] else 0
        bar = progress_bar(pct)
        print(f"{t['name']} [{bar}] {pct}% ({t['completed_steps']}/{t['total_steps']})")

def progress_bar(pct, width=30):
    filled = int(width * pct / 100)
    return "#" * filled + "-" * (width - filled)

def remove_topic():
    topics = load()
    for i, t in enumerate(topics, 1):
        print(f"{i}. {t['name']}")
    idx = int(input("Hapus nomor: ")) - 1
    topics.pop(idx)
    save(topics)
    print("Terhapus.")

def menu():
    while True:
        print("""
=== LEARNING DASHBOARD ===
1. Tambah topik
2. Tandai progress
3. Tampilkan dashboard
4. Hapus topik
5. Keluar
""")
        c = input("Pilih: ")
        if c == "1": add_topic()
        elif c == "2": mark_step()
        elif c == "3": show_dashboard()
        elif c == "4": remove_topic()
        elif c == "5": break

if __name__ == "__main__":
    menu()
