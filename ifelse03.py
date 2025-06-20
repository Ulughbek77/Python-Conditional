import os

fayl_nomi = input("Fayl nomini kiriting: ")

if os.path.exists(fayl_nomi):
    print(f"{fayl_nomi} fayli mavjud")
else:
    print(f"{fayl_nomi} fayli mavjud emas")
