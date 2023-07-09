# Import library
from cashier import *
import tabulate
import random
from datetime import datetime
import sys
"""
Self Service Cashier.

Tujuan: Merupakan program untuk membantu customer supermarket dalam menambah barang, merubah barang, menghapus barang,
menampilkan barang, sampai ke pembayaran.

"""

print("=" * 60)
print(f"Selamat Datang di Supermarket")
print(f"Self Service Cashier System")
print("=" * 60)

# Input nama customer
while True:
    name = input("Masukan Nama: ")
    if name.title():
        break
    else:
        print("Input salah. Please enter alphabetic characters only.")

# Membuat unique transaction id untuk setiap customer
transaction_id = "TX" + str(random.randint(100, 999))

# Membuat waktu dan tanggal transaksi
current_date = datetime.now()
date = current_date.strftime("%d/%m/%Y %H:%M:%S")

# Menampilkan profil customer
print(f"Name    : {name.title()}")
print(f"Date    : {date}")
print(f"TX ID   : {transaction_id}")
print("=" * 60)

# Menambahkan item ke list
print(" Tambah Barang ")
while True:
    add_item()
    print("=" * 60)
    more_items = input("Anda yakin ingin keluar? (y/n): ").lower()
    if more_items == "y":
        break

# Menampilkan menu super cashier
while True:
    print("=" * 60)
    print("Menu Utama")
    print("1. Tambah barang")
    print("2. Update barang")
    print("3. Hapus barang")
    print("4. Tampilkan semua barang")
    print("5. Reset barang")
    print("6. Total harga")
    print("7. Checkout")
    print("8. Keluar")

    try:
        print("=" * 60)
        choice = int(input("Pilih angka: "))
    except ValueError:
        print("Input salah, hanya masukkan angka")
        continue

    print("=" * 60)
    if choice == 1:
        print("---TAMBAH BARANG")
        while True:
            add_item()
            more_items = input("Tambah barang? (y/n): ").lower()
            print("\n")
            if more_items == "n":
                break
                
    elif choice == 2:
        print("---UPDATE BARANG")
        update_menu = True
        while update_menu:
            print("1. Update nama item")
            print("2. Update harga item")
            print("3. Update jumlah item")
            print("4. Kembali ke menu utama")

            try:
                update_choice = int(input("Pilih angka: "))
            except ValueError:
                print("Input salah, hanya masukkan angka")
                continue

            if update_choice == 1:
                update_item()

            elif update_choice == 2:
                update_price()

            elif update_choice == 3:
                update_qty()

            elif update_choice == 4:
                update_menu = False

            else:
                print("Input Salah")

    elif choice == 3:
        print("---HAPUS ITEM")
        delete_menu = True
        while delete_menu:
            print("1. Hapus item")
            print("2. Kembali ke menu utama")

            try:
                delete_choice = int(input("Pilih angka:"))
            except ValueError:
                print("Input salah, hanya masukkan angka")
                continue

            # Execute user's update choice
            if delete_choice == 1:
                delete_item()

            elif delete_choice == 2:
                delete_menu = False

            else:
                print("Input salah")

    elif choice == 4:
        print("---TAMPILKAN SEMUA BARANG")
        show_items()

    elif choice == 5:
        print("---RESET BARANG")
        reset_transaction()

    elif choice == 6:
        print("---MENGHITUNG TOTAL HARGA")
        total_price()

    elif choice == 7:
        print("---CHECKOUT BARANG")
        checkout_menu = True
        while checkout_menu:
            print("   1. Ya")
            print("   2. Tidak")

            try:
                checkout_choice = int(input("Apakah anda yakin ingin checkout? "))
            except ValueError:
                print("Input salah, hanya masukkan angka")
                continue

            # Execute user's checkout choice
            if checkout_choice == 1:
                checkout()
                print("============= Terima kasih telah belanja! ==============")
                print("=" * 60)
                reset_transaction()
                checkout_menu = False

            elif checkout_choice == 2:
                checkout_menu = False

            else:
                print("Input salah")

    elif choice == 8:
        exit_menu = True
        while exit_menu:
            print("Keluar")
            print("1. Ya")
            print("2. Tidak")

            try:
                exit_choice = int(input("Apakah yakin ingin keluar? "))
            except ValueError:
                print("Input salah, hanya masukkan angka")
                continue

            if exit_choice == 1:
                print("=" * 60)
                print("============= Terima kasih telah berbelanja! ==============")
                print("=" * 60)
                sys.exit()

            elif exit_choice == 2:
                exit_menu = False

            else:
                print("Input salah")

    else:
        print("Input salah")
