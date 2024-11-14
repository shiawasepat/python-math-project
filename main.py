nasabah = []
while True:
    N = int(input("Jumlah nasabah : "))
    if N <= 0:
        print("Invalid Number")
    else:
        break

for i in range(N):
    nama = str(input(f"Masukkan nama nasabah {i+1} : "))
    nasabah.append(nama)

while nasabah:
    print(f"Nasabah {nasabah[0]} sedang dilayani")
    s = str("Pilih transaksi:\n1. Tarik Tunai\n2. Cek Saldo\n3. Setor Tunai\n4. Selesai")
    uang = 0
    while True:
        print(s)
        n = int(input("Masukkan nomor transaksi: "))
        if n == 1:
            selisih = int(input("Masukkan jumlah yang ingin ditarik: "))
            if uang-selisih >= 0:
                print(f"Andi berhasil menarik tunai Rp{selisih}. Saldo sekarang: Rp{uang-selisih}")
                uang = uang-selisih
            else:
                print("Anda tidak bisa menarik saldo karena saldo anda tidak cukup")
        if n == 2:
            print(f"Saldo {nasabah[0]}: Rp{uang}")
        if n == 3:
            setor = int(input("Masukkan jumlah yang anda ingin setor: "))
            uang = uang+setor
        if n == 4:
            print(f"{nasabah[0]} telah selesai melakukan transaksi")
            nasabah.pop(0)
            break