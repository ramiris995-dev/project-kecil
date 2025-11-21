import random
import string
import re

def generate_password(length):
    chars = string.ascii_letters + string.digits + string.punctuation
    return "".join(random.choice(chars) for _ in range(length))

def check_strength(password):
    score = 0

    if len(password) >= 8: score += 1
    if re.search(r"[A-Z]", password): score += 1
    if re.search(r"[a-z]", password): score += 1
    if re.search(r"[0-9]", password): score += 1
    if re.search(r"[!@#$%^&*()_+=\-{};:'\",.<>/?]", password): score += 1

    levels = {
        1: "Very Weak",
        2: "Weak",
        3: "Medium",
        4: "Strong",
        5: "Very Strong"
    }

    return levels.get(score, "Unknown")

def menu():
    while True:
        print("\n=== PASSWORD TOOL ===")
        print("1. Generate Password")
        print("2. Check Password Strength")
        print("3. Keluar")

        choice = input("Pilih menu: ")

        if choice == "1":
            length = int(input("Panjang password: "))
            pwd = generate_password(length)
            print("Password:", pwd)

        elif choice == "2":
            pwd = input("Masukkan password: ")
            print("Strength:", check_strength(pwd))

        elif choice == "3":
            break

        else:
            print("Pilihan tidak valid!")

if __name__ == "__main__":
    menu()
