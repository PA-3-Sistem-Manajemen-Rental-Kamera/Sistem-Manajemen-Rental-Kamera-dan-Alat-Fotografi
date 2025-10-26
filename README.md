
# Lensakamu - Sistem Rental Kamera & Alat Fotografi (CLI)


<img width="906" height="311" alt="image" src="https://github.com/user-attachments/assets/c251d7d5-1b79-4d6e-8af9-c568e5f5f5e0" />

---

## ✨ Fitur Utama
- **Login & Register**
  - Role: `admin` & `user`
  - Register user baru dengan **PIN e‑wallet** (6 digit) + saldo awal 0
  - **Mask input** untuk password & PIN dengan `pwinput`
  - **3x percobaan** login gagal :  **timeout** dengan progress bar ASCII
- **Admin Menu**
  - List kamera per kategori (Mirrorless / DSLR / Cinema)
  - Tambah kamera baru (validasi harga, stok, status)
  - Update **status** & **stok** kamera
  - Hapus kamera
  - Riwayat transaksi seluruh pengguna
  - Cari kamera (full‑text contains)
  - Simpan perubahan (persist ke JSON)
- **User Menu**
  - Lihat daftar kamera per kategori + **sorting harga** (termurah/termahal)
  - **Sewa kamera** (metode bayar: **Saldo**/*QRIS*)
  - **Kembalikan kamera** (stok otomatis bertambah, status ke *Tersedia* bila stok > 0)
  - **Top Up** saldo (nominal preset / custom + verifikasi PIN)
  - **Riwayat transaksi** pribadi
  - **Cari kamera**
- **Pembayaran**
  - **Saldo**: potong saldo jika cukup & verifikasi PIN
  - **QRIS**: tampilkan **ASCII QR** via `qrcode_terminal`
- **Persistensi JSON**
  - `harga_sewa.json` (inventori kamera)
  - `datalogin.json` (akun, saldo, PIN, role)
  - `data_pelanggan.json` (transaksi)
- **Error Handling** menyeluruh (EOF/KeyboardInterrupt/ValueError/JSON errors) dengan pesan ramah pengguna

---

### Logika Sewa/Kembali 
- **Sewa**: cek ketersediaan & stok; pilih pembayaran → sukses → **stok−1**; bila stok < 1 → **status=Disewa**; catat transaksi (tanggal pinjam & estimasi kembali)
- **Kembalikan**: pilih transaksi aktif → **stok+1** → bila stok > 0 → **status=Tersedia**; perbarui `tanggal_kembali` & `status=Dikembalikan`

## Struktur Data

### 1) `datalogin.json`
```json
{
  "User": {
    "password": "User123",
    "role": "user",
    "saldo": 395000,
    "pin": "123456"
  },
  "Admin": {
    "password": "Admin123",
    "role": "admin",
    "saldo": 0,
    "pin": "123456"
  }
}
```
**Kunci penting**: `role` ("admin"/"user"), `saldo` (int, rupiah), `pin` (string numerik, 6 digit saat register).

### 2) `harga_sewa.json`
```json
{
  "Mirrorless": {
    "Sony A6300": {"harga": 175000, "status": "Tersedia", "stok": 9},
    "Canon R6 II": {"harga": 475000, "status": "Tersedia", "stok": 1}
  },
  "DSLR": { "Nikon D500": {"harga": 350000, "status": "Tersedia", "stok": 1} },
  "Cinema": { "Sony FX6 Cinema Line": {"harga": 1200000, "status": "Tersedia", "stok": 1} }
}
```
**Kunci penting**: `harga` per hari, `status` ("Tersedia"/"Disewa"), `stok` (int ≥ 0).

### 3) `data_pelanggan.json` (riwayat transaksi)
```json
[
  {
    "username": "User",
    "nama": "bunga anggrek",
    "kamera": "Canon R6 II",
    "lama_sewa": 1,
    "total_biaya": 475000,
    "tanggal_sewa": "24-10-2025 11:33:58",
    "tanggal_kembali": "25-10-2025 11:33:58",
    "metode_pembayaran": "Saldo",
    "status": "Dipinjam"
  }
]
```

---

##  Contoh Alur & Cuplikan Output Terminal

### 1) Login User (Sukses)

`![login-success](docs/screens/login-success.png)`


### 2) Gagal Login (Timeout 3x)

*Screenshot:* `![login-timeout](docs/screens/login-timeout.png)`

### 3) List & Sorting Kamera (User)

*Screenshot:*

### 4) Sewa Kamera — Bayar dengan **Saldo** (Berhasil)
*Screenshot:* `![pay-saldo-success](docs/screens/pay-saldo-success.png)`

### 5) Sewa Kamera — **Saldo Tidak Cukup** → Top Up

*Screenshot:* `![topup-success](docs/screens/topup-success.png)`

### 6) Sewa Kamera — **QRIS** (ASCII QR)

*Screenshot:* `![qris-ascii](docs/screens/qris-ascii.png)`

### 7) Kembalikan Kamera
`
Screenshot:* `![return-success](docs/screens/return-success.png)`

### 8) Riwayat Transaksi (User)
`
*Screenshot:* `![history-user](docs/screens/history-user.png)`

---

##  Validasi & Penanganan Error
- **Input kosong/tidak valid** (angka/huruf) → pesan error & retry
- **Login/Top Up** → verifikasi **PIN** (3x kesempatan)
- **File JSON hilang/korup** → fallback *default data* &/atau inisialisasi list kosong
- **KeyboardInterrupt (Ctrl+C) / EOF (Ctrl+D)** → keluar dengan pesan aman
- **Stok/Harga** divalidasi (rentang wajar) saat tambah/update/sewa

> **Security note**: Data **password/PIN** disimpan **tanpa hashing**. 

##  Shortcut & Tips Navigasi
- **Admin**: `S` untuk **Simpan** perubahan → commit ke JSON
- **User**: `S` (di menu sewa) membuka **Cari Kamera**
- Gunakan **huruf besar/kecil** sesuai label menu; `X` untuk kembali/batal

Flowchart

## 1.Menu Awal
## 2.Menu Admin
## 3.Menu User
## 4.Menu Register
## 5.Menu Keluar


```## 🙌 Kredit
Dibuat oleh **Kelompok 3B Sistem Informasi 2025**. Terima kasih untuk semua kontributor yang telah menyelesaikan Projek Akhir
