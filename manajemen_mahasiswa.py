mahasiswa = []

def tambah(nama, nilai):
    mahasiswa.append({'nama': nama, 'nilai': nilai})

def tampilkan():
    if not mahasiswa:
        print("Tidak ada data mahasiswa.")
        return
    print("Daftar Nilai Mahasiswa:")
    for mhs in mahasiswa:
        print(f"Nama: {mhs['nama']}, Nilai: {mhs['nilai']}")

def hapus(nama):
    global mahasiswa
    mahasiswa = [mhs for mhs in mahasiswa if mhs['nama'] != nama]

def ubah(nama_lama, nama_baru, nilai_baru):
    for mhs in mahasiswa:
        if mhs['nama'] == nama_lama:
            mhs['nama'] = nama_baru
            mhs['nilai'] = nilai_baru
            break

def menu():
    while True:
        print("\nMenu:")
        print("1. Tambah Data Mahasiswa")
        print("2. Tampilkan Data Mahasiswa")
        print("3. Hapus Data Mahasiswa")
        print("4. Ubah Data Mahasiswa")
        print("5. Keluar")
        
        pilihan = input("Pilih menu (1-5): ")
        
        if pilihan == '1':
            nama = input("Masukkan nama mahasiswa: ")
            nilai = input("Masukkan nilai mahasiswa: ")
            tambah(nama, nilai)
        
        elif pilihan == '2':
            tampilkan()
        
        elif pilihan == '3':
            nama = input("Masukkan nama mahasiswa yang ingin dihapus: ")
            hapus(nama)
        
        elif pilihan == '4':
            # Proses pencarian mahasiswa yang akan diubah
            nama_lama = input("Masukkan nama mahasiswa yang ingin diubah: ")
            
            # Cek apakah mahasiswa ditemukan
            mahasiswa_ditemukan = False
            for mhs in mahasiswa:
                if mhs['nama'] == nama_lama:
                    mahasiswa_ditemukan = True
                    print(f"\nData Mahasiswa yang Akan Diubah:")
                    print(f"Nama Saat Ini: {mhs['nama']}")
                    print(f"Nilai Saat Ini: {mhs['nilai']}")
                    break
            
            if not mahasiswa_ditemukan:
                print("Mahasiswa tidak ditemukan!")
                continue
            
            # Proses pengubahan data
            nama_baru = input("Masukkan nama baru: ")
            nilai_baru = input("Masukkan nilai baru: ")
            
            ubah(nama_lama, nama_baru, nilai_baru)
            print(f"Data berhasil diubah")
        
        elif pilihan == '5':
            print("Terima kasih!")
            break
        
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

menu()