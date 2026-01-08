# Python-Project
print('Selamat datang di program ATM, Bank KDHR')

f = open('datanasabah.txt', 'r')
isi = f.read().split('\n')
f.close()


for x in range(3):
    nmr = input('Masukkan Nomer Nasabah Anda! ')
    pin = input('Silahkan masukkan 4 digit pin, Anda : ')
    IDN = 0
    for y in isi:
        dn = y.split('|')
        if dn[0] == nmr and dn[3] == pin:
            print('Data Anda Valid!')
            print('Selamat Datang', dn[1] )
            cp = True
            break
        else:
            cp = False
        IDN += 1

    if cp:
        break
    if cp == False:
        print('Data Anda Tidak Terdaftar')

    if x == 2:
        print('Kartu Anda Terblokir!')
        exit()


saldo = int(dn[2])

while True:   
    daftar_kalimat = [ 
        '1. Silahkan tekan 1 untuk Informasi Saldo',
        '2. Silahkan tekan 2 untuk Penarikan Uang',
        '3. Silahkan tekan 3 untuk Nabung',
        '4. Silahkan tekan 4 untuk Membuat Akun',
        '5. Exit'
    ]
    for kalimat in daftar_kalimat:
            print(kalimat)
    pilih = int(input('Silahkan pilih menu yang Anda inginkan? '))

    if pilih == 1:
        print('Isi saldo Anda : ', saldo)

    elif pilih == 2:
        while True:
            print('Jumlah nominal penarikan sebesar: 50000, 100000, 250000, 500000, 1000000')
            penarikan = int(input('Berapa jumlah penarikan Anda? '))

            if penarikan not in [50000, 100000, 250000, 500000, 1000000]:
                print('Tidak valid! silahkan pilih nominal yang tertera!')
            
            elif penarikan > saldo:
                print('Saldo tidak cukup! Silahkan kembali menginput jumlah penarikan ')

            else:
                break
      


        Sisa = saldo - penarikan
        
        with open('datanasabah.txt', 'r') as file:
            nasabah = file.readlines()
        
        nasabah[IDN]= dn[0] + '|' + dn[1] + '|' + str(Sisa) + '|' + dn[3] + '\n'
        with open('datanasabah.txt', 'w') as file:
            file.writelines(nasabah)

        if Sisa > 0:
            print('Uang akan segera keluar, Mohon Tunggu!')
            print('Sisa saldo anda ;', Sisa)
        saldo = Sisa

    elif pilih == 3:
        nabung = int(input('Silahkan berapa nominal uang yang Anda tabung: '))
        tabungan = saldo + nabung
        with open('datanasabah.txt', 'r') as file:
            nasabah = file.readlines()
        nasabah[IDN]= dn[0] + '|' + dn[1] + '|' + str(tabungan) + '|' + dn[3] + '\n'
        with open('datanasabah.txt', 'w') as file:
            file.writelines(nasabah)
        print('Uang Anda Sudah Tersimpan')

    elif pilih == 4:
        nomer = input('Masukkan Nomor Nasabah! ')
        nama = input('Masukkan Nama! ')
        sldo = input('Masukkan Isi Saldo Anda! ')
        pin = input('Masukkan Nomor Pin! ')
        save = input('Apakah data mau di simpan? ya atau tidak (y/t) ')
        if save == 'y':
            f = open('datanasabah.txt', 'a')
            f.write(nomer + '|' + nama + '|' + sldo + '|' + pin + '\n')
            f.flush()
            print('Data Anda sudah tersimpan')
        elif save == 't':
            print('Data Anda tidak disimpan')
        


    elif pilih == 5:
        print('Exit')
        break

    else:
        print('Tidak valid')
        break
    
