import json
import os
from datetime import datetime, timedelta

DB = "data/habits.json"

def ensure_db():
    os.makedirs("data", exist_ok=True)
    if not os.path.exists(DB):
        with open(DB, "w") as f:
            json.dump({}, f)

def load_db():
    ensure_db()
    with open(DB, "r") as f:
        return json.load(f)

def save_db(db):
    with open(DB, "w") as f:
        json.dump(db, f, indent=4)

def add_habit():
    db = load_db()
    name = input("Nama kebiasaan: ").strip()
    freq = input("Frekuensi target per minggu (angka): ").strip()
    try:
        freq = int(freq)
    except:
        print("Masukkan angka. Default 3.")
        freq = 3
    db[name] = {
        "created": datetime.now().strftime("%Y-%m-%d"),
        "target_per_week": freq,
        "records": []  # list of date strings "YYYY-MM-DD"
    }
    save_db(db)
    print(f"Kebiasaan '{name}' ditambahkan.")

def log_habit():
    db = load_db()
    if not db:
        print("Belum ada kebiasaan. Tambahkan dulu.")
        return
    print("Pilih kebiasaan:")
    keys = list(db.keys())
    for i, k in enumerate(keys, 1):
        print(f"{i}. {k}")
    idx = int(input("Nomor: ")) - 1
    if idx < 0 or idx >= len(keys):
        print("Pilihan salah.")
        return
    habit = keys[idx]
    date = input("Tanggal (YYYY-MM-DD) [enter = hari ini]: ").strip()
    if not date:
        date = datetime.now().strftime("%Y-%m-%d")
    # avoid duplicate
    if date in db[habit]["records"]:
        print("Sudah pernah dicatat untuk tanggal itu.")
    else:
        db[habit]["records"].append(date)
        db[habit]["records"].sort()
        save_db(db)
        print("Tercatat!")

def view_habits():
    db = load_db()
    if not db:
        print("Belum ada kebiasaan.")
        return
    for name, meta in db.items():
        total = len(meta["records"])
        last = meta["records"][-1] if meta["records"] else "—"
        print(f"\n{name} — dibuat: {meta['created']}")
        print(f"Target/minggu: {meta['target_per_week']} | Total catatan: {total} | Terakhir: {last}")
        # ascii sparkline for last 14 hari
        print_ascii_calendar(meta["records"])

def print_ascii_calendar(records, days=14):
    # show last `days` days as █ for done, . for not done, oldest left
    today = datetime.now().date()
    start = today - timedelta(days=days-1)
    row = []
    for i in range(days):
        d = (start + timedelta(days=i)).strftime("%Y-%m-%d")
        row.append("█" if d in records else ".")
    print("".join(row), f" ({days}d)")

def weekly_summary():
    db = load_db()
    week = input("Masukkan minggu (YYYY-WW) [enter = current week]: ").strip()
    if not week:
        # compute current ISO week
        now = datetime.now()
        week = f"{now.year}-{now.isocalendar()[1]:02d}"
    print(f"\nRingkasan minggu {week}:")
    for name, meta in db.items():
        count = 0
        for r in meta["records"]:
            dt = datetime.strptime(r, "%Y-%m-%d")
            wk = f"{dt.year}-{dt.isocalendar()[1]:02d}"
            if wk == week:
                count += 1
        status = "OK" if count >= meta["target_per_week"] else "MISS"
        print(f"- {name}: {count} / {meta['target_per_week']} → {status}")

def delete_habit():
    db = load_db()
    keys = list(db.keys())
    for i, k in enumerate(keys, 1):
        print(f"{i}. {k}")
    idx = int(input("Hapus nomor: ")) - 1
    if 0 <= idx < len(keys):
        key = keys[idx]
        del db[key]
        save_db(db)
        print(f"Kebiasaan '{key}' dihapus.")
    else:
        print("Pilihan salah.")

def menu():
    while True:
        print("""
=== HABIT TRACKER ===
1. Tambah kebiasaan
2. Catat kebiasaan (log)
3. Lihat kebiasaan
4. Ringkasan mingguan
5. Hapus kebiasaan
6. Keluar
""")
        c = input("Pilih: ")
        if c == "1": add_habit()
        elif c == "2": log_habit()
        elif c == "3": view_habits()
        elif c == "4": weekly_summary()
        elif c == "5": delete_habit()
        elif c == "6": break
        else: print("Pilihan tidak valid.")

if __name__ == "__main__":
    menu()
