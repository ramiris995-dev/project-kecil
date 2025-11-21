import time
import os

def countdown(minutes):
    seconds = minutes * 60
    while seconds:
        mins = seconds // 60
        secs = seconds % 60
        print(f"{mins:02d}:{secs:02d}", end="\r")
        time.sleep(1)
        seconds -= 1

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def pomodoro(work=25, rest=5):
    clear()
    print("Fokus mulai!")
    countdown(work)
    print("\nIstirahat!")
    countdown(rest)
    print("\nSesi selesai!")

def menu():
    while True:
        print("\n1. Mulai Pomodoro (25/5)\n2. Custom\n3. Keluar")
        c = input("Pilih: ")
        if c == "1":
            pomodoro()
        elif c == "2":
            w = int(input("Fokus (menit): "))
            r = int(input("Istirahat (menit): "))
            pomodoro(w, r)
        else:
            break

menu()
