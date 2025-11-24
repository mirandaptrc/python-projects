
barang_db = {
    "BRG001": {"nama": "Indomie Kari Ayam", "harga": 3500},
    "BRG002": {"nama": "Aqua 600ml", "harga": 5000},
    "BRG003": {"nama": "Chitato BBQ", "harga": 12000},
    "BRG004": {"nama": "Kopi Good Day", "harga": 2500},
}

keranjang = []

while True:
    print("\n=== INPUT BARANG ===")
    kode = input("Kode barang: ").upper()

    if kode not in barang_db:
        print("Kode tidak ditemukan anj, cek lagi.")
        continue

    qty = int(input("Qty: "))

    nama = barang_db[kode]["nama"]
    harga = barang_db[kode]["harga"]
    subtotal = harga * qty

    keranjang.append({
        "kode": kode,
        "nama": nama,
        "harga": harga,
        "qty": qty,
        "subtotal": subtotal
    })

    lagi = input("Tambah barang lain? (y/n): ")
    if lagi.lower() != "y":
        break

total = sum(item["subtotal"] for item in keranjang)

print("\n===== STRUK PEMBELIAN =====")
for item in keranjang:
    print(f"{item['kode']} | {item['nama']} x{item['qty']} = {item['subtotal']}")

print("----------------------------")
print("TOTAL:", total)
print("============================")