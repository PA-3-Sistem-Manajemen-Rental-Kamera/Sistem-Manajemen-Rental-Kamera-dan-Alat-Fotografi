import json
from prettytable import PrettyTable
import time
import pwinput
import os
import qrcode_terminal
from datetime import datetime, timedelta
from colorama import Fore, Back, Style, init
import sys
init(autoreset=True)

try:
    filelogin= 'datalogin.json'
    filejson= 'harga_sewa.json'
    filepelanggan='data_pelanggan.json'
    with open(filejson, 'r') as f:
        data_kamera = json.load(f)
    with open (filelogin, 'r') as f:
        akun = json.load(f)
    with open (filepelanggan, 'r') as f:
        data_pelanggan = json.load(f)

except FileNotFoundError:
    print("File json tidak ditemukan.")
    print("Menggunakan data default.")
    data_kamera = {
            "Mirrorless": {
            "Sony A6300": { "harga": 175000, "status": "Tersedia", "stok": 3 },
            "Sony A7ii": { "harga": 240000, "status": "Tersedia", "stok": 2 },
    },
    "DSLR": {
        "Canon 700D": { "harga": 120000, "status": "Tersedia", "stok": 5 },
        "Canon 60D": { "harga": 120000, "status": "Tersedia", "stok": 3 },
    },
    "Cinema" : {
    "Sony FX30 Cinema Line": { "harga": 400000, "status": "Disewa", "stok": 1 },
    "Sony FX6 Cinema Line": { "harga": 1200000, "status": "Tersedia", "stok": 1 }
    }
  }
    akun = {
    "Admin": {
        "password": "Admin123",
        "role": "admin"

    },
    "User": {
        "password": "User123",
        "role": "user"
    }
} 
    data_pelanggan= []
except json.JSONDecodeError:
    data_pelanggan= []




#FUNGSI SIMPAN DATAKE FILE JSON
def save():
  time.sleep(1)
  with open (filejson, 'w') as f:
    json.dump(data_kamera, f, indent=4)
  with open (filepelanggan, 'w') as f:
    json.dump(data_pelanggan, f, indent=4)
  print("data berhasil tersimpan!!")
  time.sleep(1)
  with open (filelogin, 'w') as f:
    json.dump(akun, f, indent=4)

#FUNGSI LOGIN PENGGUNA / ADMIN
def login_admin():
    os.system('cls')
    try:
        print(Fore.GREEN + '''
+=========================================+          
|            MENU LOGIN ADMIN             |
+=========================================+''')
        kesempatan = 3
        
        while kesempatan > 0:
            username = input("Username: ").strip()
            password = pwinput.pwinput(prompt="Password: ", mask="*").strip()            
            if (username in akun and 
                akun[username]['role'] == 'admin' and 
                akun[username]["password"] == password):
                os.system('cls')
                print(Fore.GREEN + f'''
-----------LOGIN BERHASIL----------- 
--------Selamat Datang {username}!!------''')
                time.sleep(2)
                return True
            else:
                kesempatan -= 1
                print(Fore.RED + "Username/Password salah!")
                print(f"Sisa kesempatan: {kesempatan}")
                if kesempatan == 0:
                    print("Kesempatan anda habis!")
                    timeout()
                    continue
                    
    except KeyboardInterrupt:
        print("Error, Pengguna keluar dari program")
        exit()
    except EOFError:
        print("Error, Pengguna keluar dari program")
        exit()
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")
        exit()
def login_user():
    os.system('cls')
    try:
        print(Fore.GREEN + '''
+=========================================+          
|            MENU LOGIN USER              |
+=========================================+''')
        kesempatan = 3
        
        while kesempatan > 0:
            username = input("Username: ").strip()
            password = pwinput.pwinput(prompt="Password: ", mask="*").strip()            
            if (username in akun and 
                akun[username]['role'] == 'user' and 
                akun[username]["password"] == password):
                os.system('cls')
                print(Fore.GREEN + f'''
-----------LOGIN BERHASIL----------- 
--------Selamat Datang {username}!!------''')
                time.sleep(2)
                return username
            else:
                kesempatan -= 1
                print(Fore.RED + "Username/Password salah!")
                print(f"Sisa kesempatan: {kesempatan}")
                if kesempatan == 0:
                    print("Kesempatan anda habis!")
                    timeout()
                    continue
                    
    except KeyboardInterrupt:
        print("Error: CTRL+C")
        exit()
    except EOFError:
        print("Error: CTRL+D")
        exit()
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")
        exit()   
        
        
        
#TIME OUT JIKA LOGIN GAGAL
def timeout():
    print(Fore.YELLOW + "\n" + "="*50)
    print(Fore.RED + "Login Terblokir, Silakan tunggu...".center(50))
    print(Fore.YELLOW + "="*50 + "\n")
    
    for i in range(10, 0, -1):
        bar = "█" * (i - 1)
        color = Fore.GREEN 
        print(f"\r{color}[{bar}] {i:2d} detik tersisa...", end="")
        time.sleep(1)
    
    print(f"\r{Fore.GREEN}[{'█'*10}] Done!{' '*20}\n")
    print(Fore.CYAN + "="*50)
    print(Fore.GREEN + "Silakan melanjutkan...".center(50))
    print(Fore.CYAN + "="*50)
    os.system('cls')




#FUNGSI PENDAFTARAN PENGGUNA BARU
def register():
  try:
    print('''
+=========================================+          
|               MENU REGISTER             |
+=========================================+      
---------------Buat Akun baru--------------''')
    while True:
      username = input("Username:").strip()
      if username is None or username == "":
        print("Username tidak boleh kosong!")
        continue
      password = pwinput.pwinput(prompt="Password: ", mask="*").strip()
      if len(password) < 6:
          print(Fore.RED + "Password harus terdiri dari minimal 6 karakter!")
          continue
      password_konfir = pwinput.pwinput(prompt="Masukan Kembali Password: ", mask="*").strip()
      pin = str(pwinput.pwinput(prompt="Masukan Pin E-Wallet: ", mask="*").strip())
      if pin.isdigit() == False or len(pin) != 6:
          print(Fore.RED+ "PIN harus terdiri dari 6 digit angka!")
          continue
      pin_konfir = str(pwinput.pwinput(prompt="Masukan Pin E-Wallet kembali: ", mask="*").strip())
      if username in akun:
        print("Username sudah terdaftar!")
        continue
      elif password==password_konfir and pin == pin_konfir:
        akun[username] = {
    "password": password,
    "role": "user",
    "saldo": 0,
    "pin" : pin
}
        with open (filelogin, 'w') as f:
          json.dump(akun, f, indent=4)
        print (f"""
===============================================
Berhasil membuat akun dengan username:{username}
===============================================""")
        return
      else:
        print("Password atau Pin tidak sama!")
        continue    
  except KeyboardInterrupt:
      print("Error, CTRL+C")
      
  except EOFError:
      print("Error, CTRL+D")
      
  except Exception as e:
      print(f"Terjadi kesalahan: {e}")
      
# FUNGSI PEMBAYARAN DAN SISTEM SALDO
def saldo(total, username):
    try:
      user = akun.get(username)  
      pin_user= str(user.get("pin", "")).strip()
      print(f"Total Bayar: Rp{total:,}")
      kesempatan = 3
      while kesempatan > 0:
        saldouser = user.get("saldo", 0)
        print(f"\nSaldo Anda : Rp{saldouser:,}")
        print(Fore.CYAN + "\nMasukan PIN untuk konfirmasi pembayaran:")
        pinkonfirmasi= pwinput.pwinput(prompt="PIN: ", mask="*")
        pinkonfirmasi= str(pinkonfirmasi).strip()        
        if pinkonfirmasi != pin_user:
          print("PIN ANDA SALAH!")
          kesempatan-=1
          if kesempatan <=0: 
            print("Kesempatan anda telah habis")
            return False
          continue
        
        if saldouser >= total:
              user["saldo"] = saldouser - total
              print("Pembayaran berhasil menggunakan SALDO!")
              print(f"Sisa Saldo : Rp{user['saldo']:,}\n")
              return True
        else:
            print("Saldo anda tidak mencukupi")
            topup_ = input("Masuk ke Menu topup saldo? (Y/N):")
            if topup_ in ("Y", "y"):
                ok = topup(username=username)
                if ok:
                    continue
                return False
            elif topup_ in ("N", "n"):
                return False

    except Exception as e:
      print("error", e)

def topup(username):
  os.system('cls')
  user = akun.get(username)
  print(Fore.CYAN + '''
+=========================================+''')
  print(Fore.GREEN + "Saldo Anda:",  user['saldo'])
  print(Fore.CYAN + '+=========================================+')
  while True:
    try:
      user = akun.get(username)
      print(Fore.LIGHTBLUE_EX + "\n+----------- PILIH NOMINAL TOPUP -----------+")
      print("| 1 | Rp50.000                              |")
      print("| 2 | Rp100.000                             |")
      print("| 3 | Rp500.000                             |")
      print("| 4 | Rp1.000.000                           |")
      print("| 5 | Nominal Lain                          |")
      print(Fore.RED+"| X | Batal                                 |")
      print(Fore.LIGHTBLUE_EX +"+-------------------------------------------+")
      pilihan = input("Pilih opsi: ").strip().upper()
      if pilihan == "1":
          nominal = 50_000
      elif pilihan == "2":
          nominal = 100_000
      elif pilihan == "3":
          nominal = 500_000
      elif pilihan == "4":
          nominal = 1_000_000
      elif pilihan == "5":
          try:
              nominal = int(input("Masukkan nominal (angka saja): "))
          except ValueError:
              print("Input nominal tidak valid!")
              return False
          if nominal <= 0:
              print("Nominal harus lebih dari 0!")
              continue
          elif nominal > 10000000:
              print("Limit Nominal TOPUP adalah 10 JUTA")
              continue
            
      elif pilihan in  ("X", "x"):
          print("Topup dibatalkan.\n")
          return False
      else:
          print("Pilihan tidak tersedia.")
          return False
      kesempatan= 3
      while kesempatan > 0:
        pinkonfirmasi= pwinput.pwinput(prompt="PIN: ", mask="*").strip()
        if pinkonfirmasi != user.get("pin"):
          print("PIN anda salah")
          kesempatan -=1
          continue
        else:
          user["saldo"] += nominal
          with open(filelogin, "w") as f:
              json.dump(akun, f, indent=4)
          os.system('cls')
          print("="*40)
          print(f"| TOPUP BERHASIL!")
          print(f"| Username   : {username}")
          print(f"| Topup      : Rp{nominal:,}")
          print(f"| Saldo Baru : Rp{user['saldo']:,}\n")
          print("="*40)
          return True
        print("kesempatan anda habis")
        break
        
  
      
    except Exception as e:
      print("Error", e)

def tf_bank(total):
  pass
def qris(total):
  print("Memproses Pembayaran Anda...\n")
  time.sleep(1)
  print(f"""==============================
TOTAL PEMBAYARAN SEBESAR:Rp{total}
==============================""")
  time.sleep(1)
  data = "www.youtube.com"
  qrcode_terminal.draw(data)
  time.sleep(1)
  print("Pembayaran Berhasil!")
  return True

#RIWAYAT TRANSAKSI PENGGUNA
def riwayat_transaksi_pengguna(username, data_pelanggan):
    if not data_pelanggan:
        print("Belum ada transaksi.")
        input("\nTekan Enter untuk Kembali...")
        os.system('cls')
        return

    hasil = []
    for d in data_pelanggan:
        if not isinstance(d, dict):
            continue
        rec = d.get("User") if isinstance(d.get("User"), dict) else d

        if rec.get("username") == username:
            hasil.append(rec)
        elif rec.get("username") is None and rec.get("nama", "").lower() == str(username).lower():
            hasil.append(rec)

    if not hasil:
        print("Belum ada transaksi untuk akun ini.")
        input("\nTekan Enter untuk Kembali...")
        os.system('cls')
        return
    print(f"{Fore.RED}\n=== RIWAYAT TRANSAKSI {username} ===")
    for i, r in enumerate(hasil, start=1):
        nama = r.get("nama", "-")
        no_hp = r.get("no_hp", "-")
        kamera = r.get("kamera", "-")
        lama = r.get("lama_sewa", 0)
        total = r.get("total_biaya", r.get("total", 0))
        metode = r.get("metode_pembayaran", r.get("metode", "-"))
        tpinjam_str = r.get("tanggal_sewa", r.get("tanggal_pinjam", "-"))
        tkembali_str = r.get("tanggal_kembali", "-")
        status = r.get("status", "Dipinjam")
        print(f"{Fore.CYAN}\n=== TRANSAKSI {i} ===")
        print(f"Nama Penyewa     : {nama}")
        print(f"No HP            : {no_hp}")
        print(f"Nama Kamera      : {kamera}")
        print(f"Lama Sewa        : {lama} Hari")
        print(f"Total Biaya      : Rp{total:,}")
        print(f"Metode Bayar     : {metode}")
        print(f"Tanggal Pinjam   : {tpinjam_str}")
        print(f"Tanggal Kembali  : {tkembali_str}")
        print(f"Status           : {status}")
    input("\nTekan Enter untuk Kembali...")
    os.system('cls')

def riwayat_transaksi_admin(data_pelanggan):
    if not data_pelanggan:
        print("Belum ada transaksi.")
        return
    for i, d in enumerate(data_pelanggan, start=1):
        username = d.get("username", "-")
        nama = d.get("nama", "-")
        no_hp = d.get("no_hp", "-")
        kamera = d.get("kamera", "-")
        lama = d.get("lama_sewa", 0)
        total = d.get("total_biaya", d.get("total", 0))
        metode = d.get("metode_pembayaran", d.get("metode", "-"))
        tpinjam_str = d.get("tanggal_sewa", d.get("tanggal_pinjam"))
        tkembali_str = d.get("tanggal_kembali")
        tpinjam = None
        if tpinjam_str:
            try:
                tpinjam = datetime.strptime(tpinjam_str, "%d-%m-%Y %H:%M:%S")
            except:
                tpinjam = None
        if not tkembali_str and tpinjam:
            tkembali_str = (tpinjam + timedelta(days=lama)).strftime("%d-%m-%Y %H:%M:%S")
        status = d.get("status", "Dipinjam")

        print(f"{Fore.CYAN}\n=== TRANSAKSI {i} ===")
        print(f"Username        : {username}")
        print(f"Nama Penyewa     : {nama}")
        print(f"No HP            : {no_hp}")
        print(f"Nama Kamera      : {kamera}")
        print(f"Lama Sewa        : {lama} Hari")
        print(f"Total Biaya      : Rp{total:,}")
        print(f"Metode Bayar     : {metode}")
        print(f"Tanggal Pinjam   : {tpinjam_str or '-'}")
        print(f"Tanggal Kembali  : {tkembali_str or '-'}")
        print(f"Status           : {status}")
    input("\nTekan Enter untuk Kembali...")
    os.system('cls')
  #CRUD ALAT ALAT SEBAGIA ADMIN
def menuadmin():
  while True:
    try:
      os.system('cls')
      print(Fore.RED+ """ 
+----------------------------------+
|            MENU ADMIN            |
+----------------------------------+""")
      print("|  |1| List Kamera                 |")
      print("|  |2| Tambah Kamera               |")
      print("|  |3| Update Status               |")
      print("|  |4| Hapus Kamera                |")
      print("|  |5| Riwayat Transaksi Pembeli   |")
      print("|  |6| Cari Kamera                 |")
      print("|  |S| Simpan                      |")
      print("|  |X| Kembali                     |")
      print("+----------------------------------+")

      pilihan = input(">>")
      if pilihan == '1':
        tampilkan_kategori_user()
      elif pilihan == '2':
        os.system('cls')
        print('''
===============================              
       MENU TAMBAH KAMERA       
+-----------------------------+
|         JENIS KAMERA        |
+-----------------------------+
|1| Mirrorless                |
|2| DSLR                      |
|3| Cinema                    | 
|X| Kembali                   |
+-----------------------------+
              ''')
        jenis_kamera = input("Pilihan>>")
        if jenis_kamera == '1':
          jenis_kamera = "Mirrorless"
        elif jenis_kamera == '2':
          jenis_kamera = "DSLR"
        elif jenis_kamera == '3':
          jenis_kamera = "Cinema"
        elif jenis_kamera in ("X", "x"):
          continue
        else:
          print("Pilihan tidak valid.")
          continue
        nama_kamera = input("Masukan nama kamera:")
        harga_sewa = int(input("Masukan harga sewa:"))
        if harga_sewa <=0 or harga_sewa > 10000000:
          print("Harga sewa tidak valid.")
          time.sleep(1)
          continue  
        status_rental= input("Masukan status rental:")
        if status_rental not in ("Tersedia", "Disewa"):
          print(" Status rental hanya: Tersedia/Disewa")
          time.sleep(1)
          continue
        stok_kamera = input("Masukan Stok kamera:")
        if stok_kamera.isdigit() == False or int(stok_kamera) <0 or int(stok_kamera) >100:
          print("Stok kamera tidak valid.")
          time.sleep(1)
          continue
        data_kamera[jenis_kamera][nama_kamera] = {
            "harga": harga_sewa,
            "status": status_rental,
            "stok": stok_kamera
        }
        
      elif pilihan == '3':
        while True:
          try: 
            jenis_kamera=tampilkan_kategori()
            if jenis_kamera in ("X", "x"):
              break
            nama_kamera = input("Masukan nama kamera yang ingin di update:")
            if nama_kamera not in data_kamera[jenis_kamera]:
                print("Kamera tidak ditemukan.")
                continue
            status_rental = input("Masukan status (Tersedia/Disewa):")
            if status_rental in ("Tersedia", "Disewa"):
              stok_rental = int(input ("Masukan stok kamera:"))
              if stok_rental <0 or stok_rental >100:
                print("Stok kamera tidak valid.")
                continue
              print("Status rental hanya: Tersedia/Disewa")
              data_kamera[jenis_kamera][nama_kamera]["status"] = status_rental
              data_kamera[jenis_kamera][nama_kamera]["stok"] = stok_rental
              print("Data kamera berhasil diupdate.")
              time.sleep(1)
              break
            else:
              print(" Error!!, Status rental hanya: Tersedia/Disewa")
              continue
          except ValueError:
            print("Masukan nilai yang valid")
          except KeyboardInterrupt:
            print("Error, CTRL+C")
          except EOFError:
              print("Error, CTRL+D")
          except Exception as e:
              print(f"Terjadi kesalahan: {e}")
              continue
        
      elif pilihan == '4':
        while True:
          try:
            jenis_kamera = tampilkan_kategori()
            if jenis_kamera == '1':
              jenis_kamera = "Mirrorless"
            elif jenis_kamera == '2':
              jenis_kamera = "DSLR"
            elif jenis_kamera == '3':
              jenis_kamera = "Cinema"
            elif jenis_kamera in ("X", "x"):
              break
            nama_kamera = input("Masukan nama kamera yang ingin dihapus:")
            if nama_kamera not in data_kamera[jenis_kamera]:
                  print("Kamera tidak ditemukan.")
                  continue
            del data_kamera[jenis_kamera][nama_kamera]
            print("Data kamera berhasil dihapus.")
            input("\nTekan Enter untuk lanjut...")
            break
          except KeyboardInterrupt:
              print("Error, CTRL+C")
          except EOFError:
              print("Error, CTRL+D")
          except Exception as e:
              print(f"Terjadi kesalahan: {e}")
              continue
      elif pilihan == '5':
        riwayat_transaksi_admin(data_pelanggan)
      elif pilihan == '6':
        cari_kamera(data_kamera)
      elif pilihan in ("S", "s"):
        save()
      elif pilihan in ("X", "x"):
        break
      else:
        print("Pilihan tidak valid.")
        continue
    except KeyboardInterrupt:
        print("Error, CTRL+C")
    except EOFError:
        print("Error, CTRL+D")
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")
        continue


def cari_kamera(data_kamera):
    try:
        nama_cari = input("Masukkan nama kamera yang ingin dicari: ").strip()
        ditemukan = False
        table = PrettyTable()
        table.field_names = ["No", "Nama Kamera", "Kategori", "Harga/Hari (Rp)", "Status", "Stok"]
        table.align["Nama Kamera"] = "l"
        for kategori, kamera_dict in data_kamera.items():
            for nama, data in kamera_dict.items():
                if nama_cari.lower() in nama.lower():
                    harga = data["harga"]
                    status = data["status"]
                    stok = data["stok"]
                    ditemukan = True
                    table.add_row([len(table._rows) + 1, nama, kategori, f"{harga:,}", status, stok])
        if ditemukan:
            os.system('cls')
            print(f"\nHasil pencarian untuk '{nama_cari}':")
            print(table)
            input("Tekan Enter untuk kembali ke menu utama...")
            os.system('cls')
            
        else:
            os.system('cls')
            print(f"\nHasil pencarian untuk '{nama_cari}':")
            print(Fore.CYAN + "Tidak Ditemukan")
            input("Tekan Enter untuk kembali ke menu utama...")
            os.system('cls')
    except KeyboardInterrupt:
        print("Error, CTRL+C")
    except EOFError:
        print("Error, CTRL+D")
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")

#FUNGSI CRUD LIST KAMERA BERDASARKAN KATEGORI
def tampilkan_kategori():
    while True:
        try:
            kategori_ = input("Mau lihat kategori kamera yang mana?\n[1] Mirrorless\n[2] DSLR\n[3] Cinema\n[X] Keluar\n> ")
            table = PrettyTable()
            table.field_names = ["No", "Nama Kamera", "Kategori", "Harga/Hari (Rp)", "Status", "Stok"]
            table.align["Nama Kamera"] = "l"

            if kategori_ == '1':
                kategori = "Mirrorless"
            elif kategori_ == '2':
                kategori = "DSLR"
            elif kategori_ == '3':
                kategori = "Cinema"
            elif kategori_ in ("X", "x"):
                kategori ="X"
                return kategori
            else:
                print("Pilihan tidak valid.")
                continue
            os.system('cls')
            for i, (nama, data) in enumerate(data_kamera[kategori].items(), start=1):
                harga = data["harga"]
                status = data["status"]
                stok = data["stok"]
                table.add_row([i, nama, kategori, f"{harga:,}", status, stok])
            print(f"\nDaftar Kamera {kategori}")
            print(table)
            os.system('pause')            
            return kategori
        except KeyboardInterrupt:
            print("Error, CTRL+C")
        except EOFError:
            print("Error, CTRL+D")
        except Exception as e:
            print(f"Terjadi kesalahan: {e}")
            continue
          
def tampilkan_kategori_user():
    while True:
        try:
            os.system('cls')
            print('''
+-----------------------------+
|         LIST KAMERA         |
+-----------------------------+
|1| Mirrorless                |
|2| DSLR                      |
|3| Cinema                    | 
|X| Kembali                   |
+-----------------------------+
                  ''')
            kategori_ = input("Pilihan>> ")
            os.system('cls')
            if kategori_ == '1':
                kategori = "Mirrorless"
            elif kategori_ == '2':
                kategori = "DSLR"
            elif kategori_ == '3':
                kategori = "Cinema"
            elif kategori_ in ('X', 'x'):
                kategori= 'X'
                return kategori
            else:
                print("Pilihan tidak valid.")
                continue
            table = PrettyTable()
            table.field_names = ["No", "Nama Kamera", "Harga/Hari (Rp)", "Status", "Stok"]
            table.align["Nama Kamera"] = "l"
            for i, (nama, data) in enumerate(data_kamera[kategori].items(), start=1):
                table.add_row([i, nama, f"Rp{data['harga']:,}", data['status'], data['stok']])
            os.system('cls')
            print(f"\nDaftar Kamera {kategori}")
            print(table)
            while True:
                menu = input("\n[1] Sort Termurah\n[2] Sort Termahal\n[X] Kembali\n>> ")
                os.system('cls')
                if menu == "1":
                    sorting_kategori(kategori, ascending=True)
                elif menu == "2":
                    sorting_kategori(kategori, ascending=False)
                elif menu.upper() == "X":
                    return kategori
                else:
                    print("Pilihan tidak valid.")
        except Exception as e:
            print(f"Terjadi kesalahan: {e}")
            
        except KeyboardInterrupt:
            print("Error, CTRL+C")
        except EOFError:
            print("Error, CTRL+D")
        except Exception as e:
            print(f"Terjadi kesalahan: {e}")
            continue
          
          
def sorting_kategori(kategori, ascending=True):
    items = list(data_kamera[kategori].items())
    items.sort(key=lambda x: x[1]['harga'], reverse=not ascending)
    table = PrettyTable()
    table.field_names = ["No", "Nama Kamera", "Harga/Hari (Rp)", "Status", "Stok"]
    table.align["Nama Kamera"] = "l"
    for i, (nama, data) in enumerate(items, start=1):
        table.add_row([i, nama, f"Rp{data['harga']:,}", data['status'], data['stok']])
    os.system('cls')
    print(f"\nDaftar Kamera {kategori}")
    print(table)

#FUNGSI CRUD
#FUNGSI SEWA KAMERA 
def sewa_kamera(logged, data_pelanggan=data_pelanggan, data_kamera=data_kamera):
  try:  
    while True:
      print(""" 
+=========================+
|    LensaKamu Studio     |
+-------------------------+
| |1| List Kamera         | 
| |2| Sewa Kamera         |
| |3| Kembalikan Kamera   |
| |4| Top Up Saldo        |
| |5| Riwayat Transaksi   |
| |S| Cari Kamera         |
| |X| Kembali             |
+-------------------------+""")
      pilihan = input(">>")
      if pilihan == "1":
        tampilkan_kategori_user()
        continue
      elif pilihan=="2":    
        while True:
          try:
            jenis_kamera = tampilkan_kategori()
            if jenis_kamera in ("x", "X"):
              break
            else:
              pilih_kamera = input ("Nama kamera yang ingin di sewa:")
              if pilih_kamera not in data_kamera[jenis_kamera]:
                  print("Nama kamera tidak di temukan!")
                  continue
              kamera_sewa = data_kamera[jenis_kamera][pilih_kamera]
              print("Pengecekan Stok....")
              time.sleep(1)
              if kamera_sewa['status'].lower() != 'tersedia' and kamera_sewa['stok'] < 1:
                print ('Maaf, Kamera ini tidak tersedia/stok habis')
                continue
              print(f"Kamera {pilih_kamera} tersedia!")
              nama=input("Nama Penyewa:").strip()
              email=input("Email:").strip()
              nohp=(input("NO.HP:"))
              print(f"Harga Sewa perhari : {kamera_sewa['harga']}")
              lama_sewa=int(input ("Berapa hari ingin sewa:"))
              if lama_sewa < 1 or lama_sewa > 30:
                print("Sewa minimal 1 hari! dan maksimal 30 Hari")
                continue
              harian=kamera_sewa['harga']
              total_biaya = harian * lama_sewa
              os.system('cls')
              print(f"""
      +===========================+
      | Total harga sewa:{total_biaya:<9}|
      +===========================+              
      | [1] Saldo                 |
      | [2] QRIS                  |
      | [X] Tidak jadi sewa deh   |
      +----------------------------
      """)
              konfir = input("Pilih Metode Pembayaran:")
              if konfir == "1":
                terbayar = saldo(total_biaya, logged)
                if terbayar:
                  pelanggan_baru = {
                  "username": logged,
                  "nama": nama,
                  "email": email,
                  "no_hp": nohp,
                  "kamera": pilih_kamera,
                  "lama_sewa": lama_sewa,
                  "total_biaya": total_biaya,
                  "tanggal_sewa": datetime.now().strftime("%d-%m-%Y %H:%M:%S"),
                  "tanggal_kembali": (datetime.now() + timedelta(days=lama_sewa)).strftime("%d-%m-%Y %H:%M:%S"),
                  "metode_pembayaran": "Saldo",
                  "status" : "Dipinjam"
          }
                  data_kamera[jenis_kamera][pilih_kamera]['stok'] -=1
                  stok = data_kamera[jenis_kamera][pilih_kamera]['stok']

                  if stok < 1: 
                    data_kamera[jenis_kamera][pilih_kamera]['status'] = "Disewa"
                    
                  data_pelanggan.append(pelanggan_baru)
                  save()
                  break
                else:
                  print("ERROR!, Pembayaran GAGAL!")
                  break
              elif konfir =="2":
                terbayar = qris(total_biaya)
                if terbayar:
                  pelanggan_baru = {
                  "username": logged,
                  "nama": nama,
                  "email": email,
                  "no_hp": nohp,
                  "kamera": pilih_kamera,
                  "lama_sewa": lama_sewa,
                  "total_biaya": total_biaya,
                  "tanggal_sewa": datetime.now().strftime("%d-%m-%Y %H:%M:%S"),
                  "tanggal_kembali": (datetime.now() + timedelta(days=lama_sewa)).strftime("%d-%m-%Y %H:%M:%S"),
                  "metode_pembayaran": "QRIS",
                  "status" : "Dipinjam"
          }
                  data_kamera[jenis_kamera][pilih_kamera]['stok'] -=1
                  stok = data_kamera[jenis_kamera][pilih_kamera]['stok'] 
                  if stok < 1: 
                    data_kamera[jenis_kamera][pilih_kamera]['status'] = "Disewa"
                  data_pelanggan.append(pelanggan_baru)
                  save()
                else:
                  print("ERROR!, Pembayaran GAGAL!")
                  break
              elif konfir in ("x", "X"):
                break
              else: 
                print("Input tidak valid")
          except KeyboardInterrupt:
            print("Error, CTRL+C")
          except EOFError:
            print("Error, CTRL+D")
          except Exception as e:
            print(f"Terjadi kesalahan: {e}")
      elif pilihan=="3":
        kembalikan_kamera(data_pelanggan, data_kamera)
      elif pilihan == "4":
        topup(logged)
      elif pilihan == "5":
        riwayat_transaksi_pengguna(logged, data_pelanggan)
      elif pilihan in ("S", "s"):
        cari_kamera(data_kamera)

      
      elif pilihan in ("X", "x"):
        break
      
      else:
        continue
  except ValueError:
    print("Masukan hanya berupa angka!")
  except KeyboardInterrupt:
    print("Error, CTRL+C")
  except EOFError:
    print("Error, CTRL+D")
  except Exception as e:
    print(f"Terjadi kesalahan: {e}")


def kembalikan_kamera(data_pelanggan=data_pelanggan, data_kamera=data_kamera):
    try:
        aktif = [t for t in data_pelanggan if t.get("status", "Dipinjam") == "Dipinjam"]
        if not aktif:
            print("Tidak ada transaksi aktif.")
            return
        print("\nDaftar Transaksi Aktif:")
        for i, t in enumerate(aktif, start=1):
            print(f"[{i}] {t.get('nama','-')} - {t.get('kamera','-')}")
        pilih = input("Pilih nomor transaksi yang ingin dikembalikan (X untuk batal): ").strip()
        if pilih in ("x", "X"):
            return
        try:
            idx = int(pilih) - 1
            if idx < 0 or idx >= len(aktif):
                print("Pilihan tidak valid.")
                return
        except ValueError:
            print("Pilihan tidak valid.")
            return
        trx = aktif[idx]
        kamera = trx.get("kamera")
        kategori = trx.get("kategori")
        if not kategori:
            kategori = next((k for k, cams in data_kamera.items() if kamera in cams), None)
        if not kategori or kamera not in data_kamera.get(kategori, {}):
            print("Data kamera tidak ditemukan di stok.")
            return
        data_kamera[kategori][kamera]["stok"] += 1
        if data_kamera[kategori][kamera]["stok"] > 0:
            data_kamera[kategori][kamera]["status"] = "Tersedia"
        for d in data_pelanggan:
            if d is trx:
                d["status"] = "Dikembalikan"
                d["tanggal_kembali"] = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
                break
        print("Kamera berhasil dikembalikan.")
        save()
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")
    except KeyboardInterrupt:
        print("Error, CTRL+C")
    except EOFError:
        print("Error, CTRL+D")
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")

#BARIS PROGRAM UTAMA 
os.system("cls")
print(Fore.LIGHTMAGENTA_EX+"Lensakamu.exe | Version 1.0 | Copyright Kelompok 3B @2025")
lines = [
    "  _                          _  __                        _____ _             _ _       ",
    " | |                        | |/ /                       / ____| |           | (_)      ",
    " | |     ___ _ __  ___  __ _| ' / __ _ _ __ ___  _   _  | (___ | |_ _   _  __| |_  ___  ",
    " | |    / _ \\ '_ \\/ __|/ _` |  < / _` | '_ ` _ \\| | | |  \\___ \\| __| | | |/ _` | |/ _ \\ ",
    " | |___|  __/ | | \\__ \\ (_| | . \\ (_| | | | | | | |_| |  ____) | |_| |_| | (_| | | (_) |",
    " |______\\___|_| |_|___/\\__,_|\\_\\_\\__,_|_| |_| |_|\\__,_| |_____/ \\__|\\__,_|\\__,_|_|\\___/ ",
    "      ==========================================================================",
    "      Ｋａｒｅｎａ  ｃｕｍａ  ｋａｍｉ  ｙａｎｇ  ｍａｓｉｈ  ｆｏｋｕｓｉｎ  ｋａｍｕ"
]
for teks in lines:
    print(Fore.GREEN + teks)
    time.sleep(0.4)
print("")  
print(Fore.CYAN+ "LOADING".center(92))
for i in range (92):
  loading_teks = i + 9
  bar = "=" * i
  if i < 30:
    warna = Fore.RED
  elif i < 60:
    warna = Fore.YELLOW
  else:
    warna = Fore.LIGHTGREEN_EX
  print(f"\r{warna}{bar} {loading_teks}%", end="")
  time.sleep(0.03)
time.sleep(2)
while True:
  os.system('cls')      
  try:    
    
    print('''
  ============================================    
  | SELAMAT DATANG DI RENTAL KAMERA DAN ALAT |
  |                FOTOGRAFI                 |
  ============================================''')
    print(Fore.LIGHTMAGENTA_EX+ """  +------------------------------------------+
  |        SILAHKAN PILIH MENU LOGIN         |   
  +------------------------------------------+       
  |1| Login Admin                            |
  |2| Login User                             |      
  |3| Register                               |
  |X| Keluar Program                         |
  +------------------------------------------+""")
    pilihan = input(">>").strip()
    if pilihan == '1':
        logged= login_admin()
        if logged is not None:
          menuadmin()
        else: continue
    elif pilihan =="2":
        logged = login_user()
        if logged is not None:
          sewa_kamera(logged, data_pelanggan, data_kamera)
        else: continue
    elif pilihan == '3':
        register()
    elif pilihan in ("x","X"):
        print("Terima kasih telah berkunjung")
        break
  except KeyboardInterrupt:
    print("Error, CTRL+C")
    
  except EOFError:
    print("Error, CTRL+D")
    
  except Exception as e:
    print(f"Terjadi kesalahan: {e}")
    

