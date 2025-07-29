# 🧾 Cashier Self-Service System

## 📘 Background Project

Andi adalah seorang pemilik supermarket besar di salah satu kota di Indonesia.  
Andi memiliki rencana untuk melakukan perbaikan proses bisnis, yaitu akan membuat sistem kasir yang self-service di supermarket miliknya.

Dengan sistem ini, customer bisa langsung memasukkan:
- item yang dibeli
- jumlah item
- harga item

Fitur ini memungkinkan pembeli dari luar kota juga bisa menggunakan sistem secara mandiri.  
Namun, Andi membutuhkan bantuan programmer untuk membangun fitur-fitur sistem kasir ini agar berjalan dengan baik.

---

## 🎯 Requirements / Objectives

### 🔁 Alur Program

1. Jalankan program `cashier.py`
2. Tambahkan item belanja (nama, jumlah, harga)
3. Update nama, jumlah, atau harga item jika perlu
4. Hapus item atau reset seluruh transaksi
5. Tampilkan daftar item belanja
6. Hitung total harga dan diskon otomatis
7. Cetak hasil akhir ke layar

### ⚙️ Proses / Fungsi yang Dibutuhkan

- `add_item()` → menambahkan item
- `update_item_name()` → mengganti nama item
- `update_item_qty()` → mengubah jumlah item
- `update_item_price()` → mengubah harga item
- `delete_item()` → menghapus item
- `reset_transaction()` → menghapus semua item
- `check_order()` → menampilkan daftar item
- `total_price()` → menghitung total dan diskon
