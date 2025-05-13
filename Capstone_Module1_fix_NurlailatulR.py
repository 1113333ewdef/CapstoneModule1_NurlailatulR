menuList = [
    '1. Menampilkan data peminjaman',
    '2. Menambahkan data peminjaman',
    '3. Mengubah data peminjaman',
    '4. Menghapus data peminjaman',
    '5. Keluar'
]

dataPeminjaman = [
    {'nama': 'Ilham Adi', 'judulBuku': 'Matematika Lanjut', 'tanggalPeminjaman': '01-05-2025', 'tanggalPengembalian': '08-05-2025', 'status': "dipinjam"},
    {'nama': 'Rezki Ananda', 'judulBuku': 'Fisika Dasar', 'tanggalPeminjaman': '16-04-2025', 'tanggalPengembalian': '23-04-2025', 'status': "dikembalikan"},
    {'nama': 'Rina Sukmawati', 'judulBuku': 'How to Improve Public Speaking Skill', 'tanggalPeminjaman': '19-01-2025', 'tanggalPengembalian': '26-01-2025', 'status': "dikembalikan"},
    {'nama': 'Jilan Nuril', 'judulBuku': 'Seismology Introduction', 'tanggalPeminjaman': '03-05-2025', 'tanggalPengembalian': '10-05-2025', 'status': "dipinjam"},
    {'nama': 'Muhammad Taufiq', 'judulBuku': 'Manajemen Pemasaran', 'tanggalPeminjaman': '29-03-2025', 'tanggalPengembalian': '06-04-2025', 'status': "dikembalikan"},
    {'nama': 'Nindi Arianti', 'judulBuku': 'Seismology Introduction', 'tanggalPeminjaman': '08-04-2025', 'tanggalPengembalian': '13-04-2025', 'status': "dikembalikan"},
    {'nama': 'Rizki Abdullah', 'judulBuku': 'Matematika Lanjut', 'tanggalPeminjaman': '02-03-2025', 'tanggalPengembalian': '08-03-2025', 'status': "dikembalikan"},
    {'nama': 'Rima Risma', 'judulBuku': 'Manajemen Pemasaran', 'tanggalPeminjaman': '11-02-2025', 'tanggalPengembalian': '18-02-2025', 'status': "dikembalikan"},
    {'nama': 'Andi Saputra', 'judulBuku': 'Dasar Pemrograman Python', 'tanggalPeminjaman': '18-04-2025', 'tanggalPengembalian': '25-04-2025', 'status': "dikembalikan"},
    {'nama': 'Ivan Setiawan', 'judulBuku': 'Fisika Dasar', 'tanggalPeminjaman': '03-05-2025', 'tanggalPengembalian': '10-05-2025', 'status': "dipinjam"}
]

## Function untuk menambahkan filter pada tampilan data (READ) ##
def tampilkan(data, status=None, nama=None, judulBuku=None):
    hasil = [
        item for item in data 
        if (not status or item["status"].lower() == status.lower()) 
        and (not nama or item["nama"].lower() == nama.lower())
        and (not judulBuku or item["judulBuku"].lower() == judulBuku.lower())
    ]
    if hasil:
        for x in hasil:
            print(f'{x["nama"]} | {x["judulBuku"]} | {x["tanggalPeminjaman"]} | {x["tanggalPengembalian"]} | {x["status"]}')
    else:
        print("Tidak ada data yang sesuai!")


## Function untuk menambahkan data baru (CREATE) ##
def tambahData():
    nama = input("Masukkan nama peminjam: ")
    judulBuku = input("Masukkan judul buku yang dipinjam: ")
    tanggalPeminjaman = input("Masukkan tanggal peminjaman buku: ")
    tanggalPengembalian = input("Masukkan tanggal pengembalian buku: ")
    status = input("Masukkan status peminjaman buku: ")

    dataBaru = {
        'nama' : nama,
        'judulBuku' : judulBuku,
        'tanggalPeminjaman' : tanggalPeminjaman,
        'tanggalPengembalian' : tanggalPengembalian,
        'status' : status
    }

    dataPeminjaman.append(dataBaru)
    print("Data berhasil ditambahkan!")

# Function untuk mengubah data peminjaman (uPDATE) ##

def ubahData():
    namaUbah = input("Nama Peminjam: ")

    for i in dataPeminjaman:
        if i['nama'].lower() == namaUbah.lower():
            print("Masukkan data yang ingin diubah, kosongkan apabila tidak diubah: ")
            i['nama'] = input("nama peminjam baru: ") or i['nama']
            i['judulBuku'] = input("Judul buku baru: ") or i['judulBuku']
            i['tanggalPeminjaman'] = input("Tanggal peminjaman baru: ") or i['tanggalPeminjaman']
            i['tanggalPengembalian'] = input("Tanggal pengembalian baru: ") or i['tanggalPengembalian']
            i['status'] = input("Status baru: ") or i['status']
            print("Data berhasil diubah!")
            return
    print("Data tidak ditemukan!")

## Function untuk menghapus data peminjaman (DELETE) ##
def hapusData():
    dataNama = input("Nama Peminjam: ").strip()
    dataJudul = input("Judul buku: ").strip()

    for i, k in enumerate(dataPeminjaman):
        if k['nama'].lower() == dataNama.lower() and k['judulBuku'].lower() == dataJudul.lower():
            konfirmasi = input(f"Apakah Anda yakin ingin menghapus data {k['nama']} - {k['judulBuku']}? (yes/no): ")
            if konfirmasi.lower() == 'yes':
                del dataPeminjaman[i]
                print("Berhasil menghapus data")
                return
            elif konfirmasi == 'no':
                print("Penghapusan dibatalkan/tidak berhasil menghapus data")
                return


#### ======================= MAIN MENU ====================== ####
def mainMenu():
    for menu in menuList:
        print(menu)
    userInput = input("Masukkan menu yang dituju [1-5]: ")
    
    if userInput == '1':
        print("\nMenampilkan Data Peminjaman")
        print("1. Tampilkan semua Data Peminjaman")
        print("2. Tampilkan data Peminjaman Tertentu")
        print("3. Kembali")
        subMenu = input("Masukkan menu yang dipilih [1-3]: ")

        if subMenu == '1':
            tampilkan(dataPeminjaman)
        elif subMenu == '2':
            print("===== Filter Data Peminjaman =====")
            statusInput = input("Masukkan status (dipinjam/dikembalikan), kosongkan jika ingin semua: ")
            namaInput = input("Masukkan nama, kosongkan jika ingin semua: ")
            judulBukuInput = input("Masukkan judul buku, kosongkan jika ingin semua: ")
            status = statusInput if statusInput else None
            nama = namaInput if namaInput else None
            judulBuku = judulBukuInput if judulBukuInput else None
            tampilkan(dataPeminjaman, status, nama, judulBuku)
        elif subMenu == '3':
            mainMenu()
        else:
            print("Pilihan tidak tersedia!")
    elif userInput == '2':
        print("\nMenambahkan Data Peminjaman")
        print("1. Tambah Data Peminjaman")
        print("2. Kembali")
        subMenu = input("Masukkan menu yang dipilih [1-2]: ")
        if subMenu == '1':
            tambahData()
            print(dataPeminjaman)
        elif subMenu == '2':
            mainMenu()
    elif userInput == '3':
        print("\nMengubah Data Peminjaman")
        print("1. Ubah data peminjaman")
        print("2. Kembali")
        subMenu = input("Masukkan menu yang dipilih [1-2]: ")

        if subMenu == '1':
            ubahData()
            print(dataPeminjaman)
        elif subMenu == '2':
            mainMenu()
    elif userInput == '4':
        print("\nMenghapus Data Peminjaman")
        print("1. Hapus Data Peminjaman")
        print("2. Kembali")
        subMenu = input("Masukkan menu yang dipilih [1-2]: ")
        if subMenu == '1':
            hapusData()
            print(dataPeminjaman)
        elif subMenu == '2':
            mainMenu()
    elif userInput == '5':
        print("Anda telah keluar dari aplikasi")
    else:
        print("Pilihan tidak tersedia")

# Jalankan program
mainMenu()

