import mysql.connector

conn = mysql.connector.connect(
    user="root",
    host="localhost",
    password="",
    database="penjualan"
)
cur = conn.cursor()

# Membuat Database (opsional, jika belum ada)
# cur.execute("CREATE DATABASE penjualan")

# Membuat tabel Pegawai
# cur.execute('''
# CREATE TABLE IF NOT EXISTS Pegawai (
#     NIK VARCHAR(20) PRIMARY KEY,
#     Nama VARCHAR(100) NOT NULL,
#     Alamat VARCHAR(100))''')

# Membuat tabel Transaksi
# cur.execute('''
# CREATE TABLE IF NOT EXISTS Transaksi (
#     No_Transaksi VARCHAR(20) PRIMARY KEY,
#     Detail_Transaksi VARCHAR(50))''')

# Membuat tabel Produk
# cur.execute('''
# CREATE TABLE IF NOT EXISTS Produk (
#     Kode_Produk VARCHAR(20) PRIMARY KEY,
#     Nama_Produk VARCHAR(100) NOT NULL,
#     Jenis_Produk VARCHAR(50),
#     Harga INT)''')

# # Membuat tabel Struk
# cur.execute('''
# CREATE TABLE IF NOT EXISTS Struk (
#     No_Transaksi VARCHAR(20),
#     NIK_Pegawai VARCHAR(20),
#     Kode_Produk VARCHAR(20),
#     Jumlah_Produk INT,
#     Total_Harga DECIMAL(15, 2),
#     FOREIGN KEY (No_Transaksi) REFERENCES Transaksi (No_Transaksi),
#     FOREIGN KEY (NIK_Pegawai) REFERENCES Pegawai (NIK),
#     FOREIGN KEY (Kode_Produk) REFERENCES Produk (Kode_Produk))''')

# # Menyimpan perubahan dan menutup koneksi
# conn.commit()
# conn.close()

# print("Database dan tabel berhasil dibuat.")

while True:
    print("1. Input Pegawai")
    print("2. Input Produk")
    print("3. Input Transaksi")
    print("4. Tampil Struk")
    print("5. Edit")
    print("6. Hapus")
    print("0. Keluar")
    menu = input("Pilihan Menu: ")

    if menu == "1":
        # Input data Pegawai
        NIK = input("Masukkan NIK Pegawai: ")
        Nama = input("Masukkan Nama Pegawai: ")
        Alamat = input("Masukkan Alamat Pegawai: ")

        try:
            cur.execute("INSERT INTO Pegawai (NIK, Nama, Alamat) VALUES (%s, %s, %s)", (NIK, Nama, Alamat))
            conn.commit()
            print("Data Pegawai berhasil ditambahkan.")
        except mysql.connector.Error as err:
            print(f"Error: {err}")

    elif menu == "2":
        # Input data Produk
        Kode_Produk = input("Masukkan Kode Produk: ")
        Nama_Produk = input("Masukkan Nama Produk: ")
        Jenis_Produk = input("Masukkan Jenis Produk: ")
        Harga = int(input("Masukkan Harga Produk: "))

        try:
            cur.execute("INSERT INTO Produk (Kode_Produk, Nama_Produk, Jenis_Produk, Harga) VALUES (%s, %s, %s, %s)",
                        (Kode_Produk, Nama_Produk, Jenis_Produk, Harga))
            conn.commit()
            print("Data Produk berhasil ditambahkan.")
        except mysql.connector.Error as err:
            print(f"Error: {err}")

    elif menu == "3":
        # Input data Transaksi
        No_Transaksi = input("Masukkan Nomor Transaksi: ")
        Detail_Transaksi = input("Masukkan Detail Transaksi: ")

        try:
            cur.execute("INSERT INTO Transaksi (No_Transaksi, Detail_Transaksi) VALUES (%s, %s)",
                        (No_Transaksi, Detail_Transaksi))
            conn.commit()
            print("Data Transaksi berhasil ditambahkan.")
        except mysql.connector.Error as err:
            print(f"Error: {err}")

    elif menu == "4":
        # Tampilkan data Struk
        cur.execute('''
        SELECT s.No_Transaksi, p.Nama, pr.Nama_Produk, s.Jumlah_Produk, s.Total_Harga
        FROM Struk s
        JOIN Pegawai p ON s.NIK_Pegawai = p.NIK
        JOIN Produk pr ON s.Kode_Produk = pr.Kode_Produk
        ''')
        result = cur.fetchall()

        for row in result:
            print(f"No Transaksi: {row[0]}, Nama Pegawai: {row[1]}, Nama Produk: {row[2]}, "
                  f"Jumlah: {row[3]}, Total Harga: {row[4]}")

    elif menu == "5":
        # Edit data Struk
        No_Transaksi = input("Masukkan Nomor Transaksi yang ingin diubah: ")
        kolom = input("Kolom yang ingin diubah (Jumlah_Produk/Total_Harga): ")
        nilai_baru = input(f"Masukkan nilai baru untuk {kolom}: ")

        try:
            query = f"UPDATE Struk SET {kolom} = %s WHERE No_Transaksi = %s"
            cur.execute(query, (nilai_baru, No_Transaksi))
            conn.commit()
            print("Data berhasil diubah.")
        except mysql.connector.Error as err:
            print(f"Error: {err}")

    elif menu == "6":
        # Hapus data dari Struk
        No_Transaksi = input("Masukkan Nomor Transaksi yang ingin dihapus: ")

        try:
            cur.execute("DELETE FROM Struk WHERE No_Transaksi = %s", (No_Transaksi,))
            conn.commit()
            print("Data berhasil dihapus.")
        except mysql.connector.Error as err:
            print(f"Error: {err}")

    elif menu == "0":
        print("Keluar dari program.")
        break

    else:
        print("Pilihan tidak valid, coba lagi.")

# Menutup koneksi
conn.close()
