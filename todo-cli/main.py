import json
import os

DATA_FILE = "tasks.json"

def load_tasks():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r") as f:
        return json.load(f)

def save_tasks(tasks):
    with open(DATA_FILE, "w") as f:
        json.dump(tasks, f, indent=4)

def show_tasks():
    tasks = load_tasks()
    if not tasks:
        print("Belum ada tugas.")
        return
    print("\nDaftar Tugas:")
    for i, task in enumerate(tasks, start=1):
        status = "✔" if task["done"] else "✘"
        print(f"{i}. [{status}] {task['title']}")
    print()

def add_task(title):
    tasks = load_tasks()
    tasks.append({"title": title, "done": False})
    save_tasks(tasks)
    print(f"Tugas '{title}' ditambahkan!")

def mark_done(index):
    tasks = load_tasks()
    if 0 <= index < len(tasks):
        tasks[index]["done"] = True
        save_tasks(tasks)
        print("Tugas ditandai selesai!")
    else:
        print("Index tidak valid!")

def delete_task(index):
    tasks = load_tasks()
    if 0 <= index < len(tasks):
        removed = tasks.pop(index)
        save_tasks(tasks)
        print(f"Tugas '{removed['title']}' dihapus!")
    else:
        print("Index tidak valid!")

def menu():
    while True:
        print("\n=== TO-DO LIST CLI ===")
        print("1. Lihat tugas")
        print("2. Tambah tugas")
        print("3. Tandai selesai")
        print("4. Hapus tugas")
        print("5. Keluar")
        
        choice = input("Pilih menu: ")

        if choice == "1":
            show_tasks()
        elif choice == "2":
            title = input("Judul tugas: ")
            add_task(title)
        elif choice == "3":
            idx = int(input("Nomor tugas: ")) - 1
            mark_done(idx)
        elif choice == "4":
            idx = int(input("Nomor tugas: ")) - 1
            delete_task(idx)
        elif choice == "5":
            break
        else:
            print("Pilihan salah!")

if __name__ == "__main__":
    menu()
