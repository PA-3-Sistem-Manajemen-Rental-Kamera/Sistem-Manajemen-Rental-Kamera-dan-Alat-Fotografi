# Lensakamu - Sistem Rental Kamera & Alat Fotografi (CLI)

<img width="906" height="311" alt="banner" src="https://github.com/user-attachments/assets/c251d7d5-1b79-4d6e-8af9-c568e5f5f5e0" />

> Aplikasi **terminal (CLI)** untuk mengelola rental kamera & alat fotografi dengan **login multi‑role (admin/user)**, **saldo e‑wallet + PIN**, pembayaran **Saldo/QRIS**, **CRUD inventori**, **riwayat transaksi**, **sort & search**, dan **persistensi JSON**.

---

## 👥 Kelompok 3B
| No | Nama Lengkap | NIM |
|----|--------------|-----|
| 1 | Muhammad Fahriel | 2509116050 |
| 2 | Muhammad Farel Awaluddin | 2509116055 |
| 3 | Syafir Ahzami | 2509116074 |
| 4 | Paschal Wijaya Salu | 2209116058 |

---

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



## ▶️ Cara Menjalankan
1. **Siapkan Python 3.8+**
2. **Install dependensi**
   ```bash
   pip install prettytable
   pip install pwinput
   pip install colorama
   pip install qrcode_terminal
   pip install os
   pip instal sys
   pip install time
   ```
3. **Pastikan file JSON ada di satu folder dengan file py**
   - `rental kamera.FIX.py`
   - `datalogin.json`
   - `harga_sewa.json`
   - `data_pelanggan.json`
4. **Jalankan aplikasi**
   ```bash
   python "rental kamera.FIX.py"
   ```
---
---

## Contoh Penggunaa Beberapa Fitur



#### Main Menu 
<img width="753" height="495" alt="image" src="https://github.com/user-attachments/assets/a3d8d747-c9d8-4e16-85ad-92b8eabe34bc" />

### Register 
**a. Berhasil** <br/>

<img width="524" height="401" alt="image" src="https://github.com/user-attachments/assets/f828af4e-c4b2-4daa-b9b1-53c256424b9e" />

**b. Gagal - Username sudah ada** <br/>

<img width="432" height="212" alt="image" src="https://github.com/user-attachments/assets/aba7eed6-ef39-4271-a90a-a9d0fa1c63b8" />
  
**c. Gagal - PIN tidak valid** <br/>

<img width="380" height="76" alt="image" src="https://github.com/user-attachments/assets/73ccdcef-9a32-4036-834c-78370ed6bdd2" />

**d. Gagal - Password Kurang dari/ tidak sama** <br/>

<img width="428" height="80" alt="image" src="https://github.com/user-attachments/assets/41438ff7-46de-4f3d-8ff4-5016b368b8fd" />
<img width="380" height="144" alt="image" src="https://github.com/user-attachments/assets/5d0dc068-cd7e-456d-98f4-aebb77150d0b" />


### Login User (Sukses)

<img width="520" height="352" alt="image" src="https://github.com/user-attachments/assets/000bc3ce-71b3-45d6-84ab-f5a6d27f9bd7" />


### Gagal Login (Timeout 3x)

<img width="618" height="383" alt="image" src="https://github.com/user-attachments/assets/f55684c4-902b-415e-bf60-33e5fced9c9f" />

### List & Sorting Kamera (User)
> Termurah & Termahal
<img width="654" height="451" alt="image" src="https://github.com/user-attachments/assets/a40c2de1-a892-425f-9904-3a481abdd2a5" />

<img width="619" height="441" alt="image" src="https://github.com/user-attachments/assets/6efef33b-8324-4f67-9284-b274ae0b9934" />


### Sewa Kamera
<img width="740" height="518" alt="image" src="https://github.com/user-attachments/assets/fe0d8d9b-b820-477b-b0b9-0b5a0eca5530" />

### Bayar dengan **Saldo** (Berhasil)
<img width="506" height="421" alt="image" src="https://github.com/user-attachments/assets/3da47e5e-a314-47a6-8e1f-05ed60ff0518" />

### Sewa Kamera — **Saldo Tidak Cukup** → Top Up -> Bayar Lagi
<br> >Saldo Tidak Cukup <br>
<img width="549" height="411" alt="image" src="https://github.com/user-attachments/assets/1281fae6-520a-4437-97af-0c9dda8f6092" /><br>
<br> >Top Up <br>
<img width="483" height="333" alt="image" src="https://github.com/user-attachments/assets/e0ea4d93-099e-44f6-b41c-d191d89add0e" /><br>
<br> >Bayar Lagi <br>
<img width="480" height="350" alt="image" src="https://github.com/user-attachments/assets/1565d564-7304-48fe-b76b-555bb2ae9c42" /><br>


### Sewa Kamera - Simulasi **QRIS** (ASCII QR)

<img width="906" height="866" alt="image" src="https://github.com/user-attachments/assets/8ce313a9-3293-491c-8324-201ef513b2ea" />

### Kembalikan Kamera
`
<img width="687" height="618" alt="image" src="https://github.com/user-attachments/assets/bdeb21e2-8c34-4d5d-8bc9-df60f8d6dfc9" />

### Riwayat Transaksi (User)
`
<img width="567" height="731" alt="image" src="https://github.com/user-attachments/assets/fbf0eb06-89b7-469d-aa62-3322156f8c58" />

### Search Kamera
<img width="629" height="341" alt="image" src="https://github.com/user-attachments/assets/f7773b17-3da9-4677-9e69-019c372fdc66" />

<img width="783" height="219" alt="image" src="https://github.com/user-attachments/assets/6b99b5ff-0f40-41a2-8897-45e0eab5f526" />



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
- Bebas gunakan **huruf besar/kecil** sesuai label menu; `X atau x` untuk kembali/batal

## Flowchart

## 1.Menu Awal
<img width="1467" height="1312" alt="Menu utama rev drawio" src="https://github.com/user-attachments/assets/9a481616-c06e-481d-99f5-f3d25af11db5" />

## 2.Menu Admin
<img width="4212" height="1070" alt="MENU ADMIN" src="https://github.com/user-attachments/assets/e70109f2-fea1-4423-a49f-f094fc558dcd" />

## 3.Menu User
<img width="3672" height="3092" alt="MENU USER 2 rev 3" src="https://github.com/user-attachments/assets/deb8a884-f001-4f64-874d-f9a8faa960ec" />

## 4.Menu Register
<img width="393" height="1302" alt="reg" src="https://github.com/user-attachments/assets/a5b1c79d-3237-4f39-a474-3af42ebda454" />


## 5.Menu Keluar
<img width="232" height="62" alt="Keluar" src="https://github.com/user-attachments/assets/ee8bc577-da62-4e03-8500-8dec0b24a157" />


## 🙌 Kredit
Dibuat oleh **Kelompok 3B Sistem Informasi 2025**. Terima kasih untuk semua kontributor yang telah menyelesaikan Projek Akhir
