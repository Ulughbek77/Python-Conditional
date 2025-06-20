parol = input("Parol kiriting: ")

kamida8belgi = len(parol) >= 8

harfbor = False
raqambor = False

for belgi in parol:
    if belgi.isalpha():
        harfbor = True
    if belgi.isdigit():
        raqambor = True

if kamida8belgi and harfbor and raqambor:
    print("Parol qabul qilindi.")
else:
    print("Parol noto'g'ri. Kamida 8 belgi, 1 harf va 1 raqam bo'lishi kerak.")

