weather = {
    "jakarta": "Hujan",
    "bandung": "Cerah",
    "surabaya": "Mendung"
}

city = input("Kota: ").lower()
print("Cuaca:", weather.get(city, "Tidak diketahui"))
