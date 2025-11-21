import json, os
from datetime import datetime, timedelta

DB = "data/tasks.json"

def ensure():
    os.makedirs("data", exist_ok=True)
    if not os.path.exists(DB):
        json.dump([], open(DB, "w"))

def load():
    ensure()
    return json.load(open(DB))

def save(tasks):
    json.dump(tasks, open(DB, "w"), indent=4)

def add_task():
    tasks = load()
    title = input("Judul tugas: ")
    due = input("Deadline (YYYY-MM-DD) [optional]: ").strip()
    priority = input("Prioritas (low/med/high): ").strip().lower() or "med"
    tasks.append({
        "title": title,
        "due": due or None,
        "priority": priority,
        "done": False,
        "created": datetime.now().strftime("%Y-%m-%d")
    })
    save(tasks)
    print("Tugas ditambahkan.")

def list_tasks(show_all=False):
    tasks = load()
    if not tasks:
        print("Tidak ada tugas.")
        return
    for i, t in enumerate(sorted(tasks, key=lambda x: (x["done"], x["due"] or "9999-99-99")), 1):
        status = "✔" if t["done"] else "✘"
        due = t["due"] or "—"
        print(f"{i}. [{status}] {t['title']} | due: {due} | prio: {t['priority']}")

def mark_done():
    tasks = load()
    list_tasks()
    idx = int(input("Tandai selesai nomor: ")) - 1
    tasks[idx]["done"] = True
    save(tasks)
    print("Ditandai selesai.")

def upcoming(days=3):
    tasks = load()
    today = datetime.now().date()
    end = today + timedelta(days=days)
    print(f"Upcoming {days} hari:")
    for t in tasks:
        if t["due"]:
            d = datetime.strptime(t["due"], "%Y-%m-%d").date()
            if today <= d <= end and not t["done"]:
                print(f"- {t['title']} due {t['due']} (prio {t['priority']})")

def remove_task():
    tasks = load()
    list_tasks()
    idx = int(input("Hapus nomor: ")) - 1
    popped = tasks.pop(idx)
    save(tasks)
    print("Dihapus:", popped["title"])

def menu():
    while True:
        print("""
=== STUDY PLANNER ===
1. Tambah tugas
2. List tugas
3. Tandai selesai
4. Upcoming (3 hari)
5. Hapus tugas
6. Keluar
""")
        c = input("Pilih: ")
        if c == "1": add_task()
        elif c == "2": list_tasks()
        elif c == "3": mark_done()
        elif c == "4": upcoming()
        elif c == "5": remove_task()
        elif c == "6": break

if __name__ == "__main__":
    menu()
