def bmi():
    h = float(input("Tinggi (m): "))
    w = float(input("Berat (kg): "))
    b = w / (h*h)

    print("BMI:", round(b, 2))
    if b < 18.5: print("Kurus")
    elif b < 25: print("Normal")
    else: print("Berlebih")

bmi()
