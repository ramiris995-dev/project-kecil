import os
import shutil

FILE_TYPES = {
    "Images": ["jpg", "jpeg", "png", "gif", "webp"],
    "Documents": ["pdf", "docx", "txt", "xlsx", "pptx"],
    "Videos": ["mp4", "mkv", "mov"],
    "Music": ["mp3", "wav"],
    "Archives": ["zip", "rar", "7z"],
}

def organize(folder):
    if not os.path.exists(folder):
        print("Folder tidak ditemukan!")
        return
    
    for filename in os.listdir(folder):
        path = os.path.join(folder, filename)
        if os.path.isfile(path):
            ext = filename.split(".")[-1].lower()

            for category, extensions in FILE_TYPES.items():
                if ext in extensions:
                    category_folder = os.path.join(folder, category)
                    os.makedirs(category_folder, exist_ok=True)
                    shutil.move(path, os.path.join(category_folder, filename))
                    break

    print("File berhasil diorganisir!")

if __name__ == "__main__":
    folder = input("Masukkan path folder: ")
    organize(folder)
