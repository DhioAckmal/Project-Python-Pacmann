# Import library
import tabulate

shopping_list = []
"""
Self Service Cashier Functions.

Merupakan kumpulan function yang berfungsi untuk program self service cashier yang terdiri dari add item, update item, update price, update quantity
, delete item, show itema, reset transaction, total price, dan checkout.

"""
# Add Item
def add_item():
    """
    Fungsi add_item

    Tujuan: input dan menambahkan barang ke list shopping_list
    """
    
    while True:
        # Menginput barang yang ingin dibeli
        while True:
            name = input("Masukkan nama barang (ketik 'end' untuk keluar): ").lower()
            if name.isnumeric():
                print("---Hanya masukkan nama barang.---")
            elif name == 'end':
                return  # Keluar dari fungsi jika input 'end'
            else:
                break
        
        # Menginput jumlah barang yang ingin dibeli
        while True:
            try:
                qty = int(input("Jumlah barang yang ingin dibeli: "))
                break
            except ValueError:
                print("---Hanya masukkan angka untuk jumlah barang.---")

        # Menginput harga barang yang ingin dibeli
        while True:
            try:
                price = float(input("Masukkan harga barang: "))
                break
            except ValueError:
                print("---Hanya masukkan angka untuk harga.---")
        
        # Total harga barang
        total_price = qty * price
                
        # Menambahkan nomor barang
        item_id = len(shopping_list) + 1
    
        # Membuat dictionary untuk ditambahkan ke list shopping_list
        shopping_list.append({
            'No': item_id,
            'Nama': name,
            'Jumlah': qty,
            'Harga': price,
            'Total Harga': total_price
        })
    
        print(f'============================')
        print(f"Barang berhasil ditambahkan")
        

# Update Item
def update_item():
    """
    Fungsi update_item()
    
    Tujuan: merubah nama barang
    """
    print(tabulate.tabulate(shopping_list, headers='keys'))
    while True:
        try:
            item_id = int(input("Masukan nomor item yang ingin diubah: "))
            break
        except ValueError:
            print("---Nomor item salah---")
    new_name = input("Masukan nama item baru: ")

    for item in shopping_list:
        if item['No'] == item_id:
            item['Nama']= new_name
            break

    print("=" * 60)
    print("---Item berhasil diubah---")
    print("=" * 60)
    print(tabulate.tabulate(shopping_list, headers='keys'))

# Update Price
def update_price():
    """
    Fungsi update_price()
    
    Tujuan: merubah harga barang
    """
    print(tabulate.tabulate(shopping_list, headers='keys'))
    while True:
        try:
            item_id = int(input("Masukan nomor item yang ingin diubah: "))
            break
        except ValueError:
            print("---Nomor item salah---")
    new_price = float(input("Masukan harga item baru "))

    for item in shopping_list:
        if item['No'] == item_id:
            item['Harga'] = new_price
            break

    print("=" * 60)
    print("---Item berhasil diubah---")
    print("=" * 60)
    print(tabulate.tabulate(shopping_list, headers='keys'))

# Update Quantity
def update_qty():
    """
    Fungsi update_qty()
    
    Tujuan: merubah jumlah barang
    """
    print(tabulate.tabulate(shopping_list, headers='keys'))
    while True:
        try:
            item_id = int(input("Masukan nomor item yang ingin diubah: "))
            break
        except ValueError:
            print("---Nomor item salah---")
    new_qty = int(input("Masukan jumlah item baru: "))

    for item in shopping_list:
        if item['No'] == item_id:
            item['Jumlah'] = new_qty
            break
        
    print("=" * 60)
    print("---Item berhasil diubah---")
    print("=" * 60)
    print(tabulate.tabulate(shopping_list, headers='keys'))
 
# Delete Item
def delete_item():
    """
    Fungsi delete_item

    Tujuan: menghapus list belanjaan yang dipilih.
    
    Cara: Akan menampilkan tabel dan user akan memilih nomor item untuk di delete,
    terakhir akan menampilkan shopping_list yang sudah di update.
    """
    # menampilkan nomor item untuk di delete
    print(tabulate.tabulate(shopping_list, headers='keys'))
    item_id = int(input("Masukan nomor item yang ingin dihapus: "))

    # menggunakan looping untuk mencari no item yang sesuai
    for i, item in enumerate(shopping_list):
        if item['No'] == item_id:
            shopping_list.remove(item)
    
            # mengupdate item number yang baru
            for j in range(i, len(shopping_list)):
                shopping_list[j]['no'] -= 1
            break

    # print pesan bahwa telah berhasil di update
    print("=" * 60)
    print("---Barang berhasil dihapus.---")
    print("=" * 60)
    
    print(tabulate.tabulate(shopping_list, headers='keys'))
    print("\n")

# Show Items 
def show_items():
    """
    Fungsi show_items

    Tujuan: menampilkan list shopping_list dengan format tabel menggunakan
    library tabulate.
    """
    
    if not shopping_list:
        print("=" * 60)
        print("---Tidak ada barang, silahkan tambahkan barang.---")
        print("=" * 60)
    else:
        # menggunakan library tabulate untuk menampilkan list shopping_list
        print(tabulate.tabulate(shopping_list, headers='keys', tablefmt='fancy_grid'))
   
# Reset Transaction
def reset_transaction():
    """
    Fungsi reset_transaction
    
    Tujuan: menghapus atau reset semua list di shopping_list
    """
    confirm = input("Apakah anda yakin menghapus list belanjaan anda? (y/n)").lower()

    if confirm == 'y':
        shopping_list.clear()
        print("=" * 60)
        print("---List belanjaan berhasil dihapus.---")
    else:
        print("=" * 60)
        print("---Penghapusan list belanjaan dibatalkan.---")

# Total Price  
def total_price():
    """
    Fungsi total_price
    
    Tujuan: Menghitung total harga list belanja, menghitung diskon yang didapatkan, 
    berdasarkan harga yang dibelanjakan, dan menghitung total harga setelah diskon.

    """
    total_price = 0
    for item in shopping_list:
        total_price += item['Harga'] * item['Jumlah']
    
    discount = 0

    # menentukan diskon yang didapat berdasarkan requirement
    if total_price > 500_000:
        discount = 0.1
    elif total_price > 300_000:
        discount = 0.08
    elif total_price > 200_000:
        discount = 0.05

    print(tabulate.tabulate(shopping_list, headers='keys', tablefmt='fancy_grid'))

    discount_amount = total_price * discount # menghitung potongan harga
    discounted_price = total_price - discount_amount # menghitung harga setelah diskon
    
    # menampilkan total harga, diskon, dan harga setelah diskon
    print("=" * 60)
    print(f"Harga: Rp. {total_price}")
    print(f"Diskon: {discount * 100}%")
    print(f"Total Diskon: Rp. {discount_amount}")
    print(f"Total Harga: Rp. {discounted_price}")
    print("=" * 60)
 
# Checkout (payment) 
def checkout():
    """
    Fungsi checkout()
    
    Tujuan: menampilkan total harga belanja setelah diskon dan tempat untuk melakukan
    pembayaran.

    """
    total_price = 0
    for item in shopping_list:
        total_price += item['Harga'] * item['Jumlah']
    
    discount = 0

    # menentukan diskon yang didapat berdasarkan requirement
    if total_price > 500_000:
        discount = 0.1
    elif total_price > 300_000:
        discount = 0.08
    elif total_price > 200_000:
        discount = 0.05

    print("Super Cashier")
    print("instagram : Super Cashier")
    print(tabulate.tabulate(shopping_list, headers='keys', tablefmt='fancy_grid'))

    discount_amount = total_price * discount # menghitung potongan harga
    discounted_price = total_price - discount_amount # menghitung harga setelah diskon
    
    # menampilkan total harga, diskon, besaran diskon, dan harga setelah diskon
    print("=" * 60)
    print(f"Harga: Rp. {total_price}")
    print(f"Diskon: {discount * 100}%")
    print(f"Total Diskon: Rp. {discount_amount}")
    print(f"Total Harga: Rp. {discounted_price}")
    print("=" * 60)
    
    
    while True:
        try:
            payment = float(input("Masukan nominal pembayaran: "))
        except ValueError: 
            print("=" * 60)
            print("---Input salah. Hanya masukkan angka.---")
            print("=" * 60)
            continue
        
        if payment < discounted_price:
            print("=" * 60)
            print("---Nominal kurang---")
            print("=" * 60)
        else:
            break
    
    # menghitung kembalian
    change = payment - discounted_price
    print(f"Kembali: Rp. {change:.1f}")
    print("=" * 60)
    print("Terima kasih telah berbelanja")

    
