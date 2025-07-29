class Transaction:
    def __init__(self):
        self.items = {}

    def add_item(self, nama_item, jumlah_item, harga_per_item):
        '''
        Function untuk menambahkan item belanja ke dalam transaksi.

        Parameters
        ----------
        nama_item : str
            Nama barang yang dibeli.
        jumlah_item : int
            Jumlah unit barang yang dibeli.
        harga_per_item : int
            Harga satuan dari barang tersebut.
        '''

        if jumlah_item <= 0 or harga_per_item <= 0:
            print("Jumlah item dan harga harus lebih dari 0")
            return
        self.items[nama_item] = {
            "Jumlah Item": jumlah_item,
            "Harga per Item": harga_per_item,
            "Total Harga": jumlah_item * harga_per_item
        }

    def update_item_name(self, nama_lama, nama_baru):
        '''
        Function untuk mengganti nama item yang sudah ada.

        Parameters
        ----------
        nama_lama : str
            Nama item yang ingin diubah.
        nama_baru : str
            Nama baru untuk menggantikan nama item lama.
        '''

        if nama_lama in self.items:
            self.items[nama_baru] = self.items.pop(nama_lama)
        else:
            print(f"Item '{nama_lama}' tidak ditemukan.")

    def update_item_qty(self, nama_item, qty_baru):
        '''
        Function untuk memperbarui jumlah item yang dibeli.

        Parameters
        ----------
        nama_item : str
            Nama item yang ingin diubah jumlahnya.
        qty_baru : int
            Jumlah item baru yang diinginkan.
        '''
        if nama_item in self.items:
            self.items[nama_item]["Jumlah Item"] = qty_baru
            self.items[nama_item]["Total Harga"] = qty_baru * self.items[nama_item]["Harga per Item"]
        else:
            print(f"Item '{nama_item}' tidak ditemukan.")

    def update_item_price(self, nama_item, harga_baru):
        '''
        Function untuk memperbarui harga satuan dari sebuah item.

        Parameters
        ----------
        nama_item : str
            Nama item yang ingin diperbarui harganya.
        harga_baru : int
            Harga satuan baru untuk item tersebut.
        '''

        if nama_item in self.items:
            self.items[nama_item]["Harga per Item"] = harga_baru
            self.items[nama_item]["Total Harga"] = harga_baru * self.items[nama_item]["Jumlah Item"]
        else:
            print(f"Item '{nama_item}' tidak ditemukan.")

    def delete_item(self, nama_item):
        '''
        Function untuk menghapus sebuah item dari daftar belanja.

        Parameters
        ----------
        nama_item : str
            Nama item yang ingin dihapus dari transaksi.
        '''
        
        if nama_item in self.items:
            del self.items[nama_item]
        else:
            print(f"Item '{nama_item}' tidak ditemukan.")

    def reset_transaction(self):
        '''
        Function untuk menghapus seluruh item yang ada di dalam transaksi.
        Digunakan jika ingin memulai transaksi baru dari awal.
        '''

        self.items.clear()
        print("Transaksi berhasil di-reset.")

    def check_order(self):
        '''
        Function untuk memvalidasi transaksi dan menampilkan daftar item
        dalam format dictionary sederhana.

        Menampilkan pesan jika terdapat input tidak valid (jumlah atau harga <= 0),
        atau jika transaksi kosong.
        '''
        
        if not self.items:
            print("Transaksi kosong.")
            return

        for nama, detail in self.items.items():
            if (not nama or
                detail["Jumlah Item"] <= 0 or
                detail["Harga per Item"] <= 0):
                print("Terdapat kesalahan input data")
                return

        print("Pemesanan sudah benar")
        # Menampilkan dalam format dictionary seperti contoh
        simple_dict = {nama: [detail["Jumlah Item"], detail["Harga per Item"]] for nama, detail in self.items.items()}
        print(f"Item yang dibeli adalah {simple_dict}")

    def total_price(self):
        '''
        Function untuk menghitung total harga belanja setelah diskon
        berdasarkan jumlah total harga dari seluruh item yang dibeli.

        Parameters
        ----------
        self.items : dict
            Dictionary yang berisi daftar item, jumlah, dan harga masing-masing barang.
        '''

        total = sum(item["Total Harga"] for item in self.items.values())

        if total > 500_000:
            diskon = 0.10
        elif total > 300_000:
            diskon = 0.08
        elif total > 200_000:
            diskon = 0.05
        else:
            diskon = 0

        total_setelah_diskon = total * (1 - diskon)
        print(f"Total Belanja yang harus dibayarkan adalah Rp. {total_setelah_diskon:,.2f}")

# Contoh Penggunaan
trnsct_123 = Transaction()

# Menambahkan item
trnsct_123.add_item("Mobil", 2, 100000)
trnsct_123.add_item("Mie", 1, 5000)
trnsct_123.add_item("Tempe", 3, 3000)

# Update item
trnsct_123.update_item_name("Mie", "Indomie")
trnsct_123.update_item_qty("Indomie", 5)
trnsct_123.update_item_price("Indomie", 6000)

# Cek dan tampilkan hasil transaksi
trnsct_123.check_order()
trnsct_123.total_price()