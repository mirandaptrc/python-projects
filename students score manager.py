
students = {
    "Nadya": [95, 100, 97],
    "Keita": [88, 90, 85]
}

def add_student(name):
    if name in students:
        print("Siswa sudah ada!")
    else:
        students[name] = []
        print("Siswa", name, "berhasil ditambah!")

def add_score(name, score):
    if name not in students:
        print("Siswa tidak ditemukan!")
    else:
        students[name].append(score)
        print("Nilai", score, "ditambah ke", name)

def get_average(name):
    if name not in students:
        print("Siswa tidak ditemukan!")
        return None

    values = students[name]
    if len(values) == 0:
        return 0

    total = 0
    for v in values:
    	total += v

    return total / len(values)

def show_status(name):
    avg = get_average(name)
    if avg is None:
        return

    if avg >= 75:
        print(name, "-> Lulus (avg:", avg, ")")
    else:
        print(name, "-> Remed (avg:", avg, ")")

def show_all():
    print("\n== Daftar Semua Siswa ==")
    for name, scores in students.items():     
        avg = get_average(name)
        print(name, ":", scores, "(avg:", avg, ")")
    print()

while True:
    print("""
==== Student Score Manager ====
1. Tambah Siswa
2. Tambah Nilai
3. Lihat Rata-Rata
4. Lihat Status
5. Lihat Semua Data
6. Keluar
""")

    choice = input("Pilih menu: ")

    if choice == "1":
        nama = input("Nama siswa baru: ")
        add_student(nama)

    elif choice == "2":
        nama = input("Nama siswa: ")
        nilai = int(input("Nilai: "))
        add_score(nama, nilai)

    elif choice == "3":
        nama = input("Nama siswa: ")
        avg = get_average(nama)
        if avg is not None:
            print("Rata-rata", nama, ":", avg)

    elif choice == "4":
        nama = input("Nama siswa: ")
        show_status(nama)

    elif choice == "5":
        show_all()

    elif choice == "6":
        print("Goodbye!")
        break

    else:
        print("Pilihan tidak valid!")