import json, os, time, csv
from datetime import datetime

DB = "data/sessions.json"

def ensure():
    os.makedirs("data", exist_ok=True)
    if not os.path.exists(DB):
        with open(DB, "w") as f:
            json.dump([], f)

def load():
    ensure()
    return json.load(open(DB))

def save(sessions):
    json.dump(sessions, open(DB, "w"), indent=4)

def start_session():
    sessions = load()
    task = input("Nama task: ").strip()
    note = input("Catatan (opsional): ").strip()
    start = datetime.now().isoformat()
    session = {"task": task, "note": note, "start": start, "end": None, "duration_sec": None}
    sessions.append(session)
    save(sessions)
    print("Session dimulai. Catatan disimpan (tutup dengan 'stop session').")

def stop_session():
    sessions = load()
    # find latest open session
    open_sessions = [s for s in sessions if s["end"] is None]
    if not open_sessions:
        print("Tidak ada session yang sedang berjalan.")
        return
    last = open_sessions[-1]
    last["end"] = datetime.now().isoformat()
    start = datetime.fromisoformat(last["start"])
    end = datetime.fromisoformat(last["end"])
    last["duration_sec"] = int((end - start).total_seconds())
    save(sessions)
    print(f"Session '{last['task']}' dihentikan. Durasi: {last['duration_sec']} detik.")

def list_sessions():
    sessions = load()
    if not sessions:
        print("Belum ada sesi.")
        return
    for i, s in enumerate(sessions, 1):
        start = s["start"]
        end = s["end"] or "—"
        dur = s["duration_sec"] or "—"
        print(f"{i}. {s['task']} | {start} → {end} | dur: {dur} | note: {s['note']}")

def export_csv():
    sessions = load()
    if not sessions:
        print("Tidak ada data.")
        return
    fname = input("Nama file CSV (default sessions.csv): ").strip() or "sessions.csv"
    with open(fname, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["task", "note", "start", "end", "duration_sec"])
        w.writeheader()
        for s in sessions:
            w.writerow(s)
    print(f"Diexport ke {fname}")

def menu():
    while True:
        print("""
=== TIME TRACKER ===
1. Mulai session
2. Hentikan session
3. List sessions
4. Export CSV
5. Keluar
""")
        c = input("Pilih: ")
        if c == "1": start_session()
        elif c == "2": stop_session()
        elif c == "3": list_sessions()
        elif c == "4": export_csv()
        elif c == "5": break
        else: print("Pilihan salah.")

if __name__ == "__main__":
    menu()
