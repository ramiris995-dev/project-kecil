import json, os, random

DB = "data/cards.json"

def load():
    if not os.path.exists(DB):
        return []
    return json.load(open(DB))

def save(d):
    json.dump(d, open(DB, "w"), indent=4)

def add_card():
    cards = load()
    q = input("Pertanyaan: ")
    a = input("Jawaban: ")
    cards.append({"q": q, "a": a})
    save(cards)
    print("Kartu ditambahkan.\n")

def quiz():
    cards = load()
    if not cards:
        print("Belum ada kartu.")
        return

    random.shuffle(cards)
    score = 0

    for c in cards:
        print("\nQ:", c["q"])
        ans = input("Jawab: ")
        if ans.lower() == c["a"].lower():
            print("Benar!")
            score += 1
        else:
            print("Salah. Jawaban:", c["a"])

    print(f"\nSkor: {score}/{len(cards)}")

def menu():
    while True:
        print("""
1. Tambah Flashcard
2. Mulai Quiz
3. Keluar
""")
        c = input("Pilih: ")
        if c == "1": add_card()
        elif c == "2": quiz()
        else: break

menu()
