"""
ACHMAT VIDIANTO
KELAS EKSTENSI
NIM 20083000180
"""

from datetime import date
today = str(date.today()) #MENAMPILKAN TANGGAL HARI INI
gajipokok = [0,2500000,4500000,6500000] # GAJI POKOK GOLONGAN 1 2 3
persentunjangan= [0,1,3,5] # PERSENTASE TUNJANGAN
tambah="Y" #UNTUK PERULANGAN HITUNG GAJI LAGI

while tambah.lower()=="y" :
    nama = input(">> MASUKAN NAMA                         :    = ")
    ulang_jenisKelamin = 1 #PERULANGAN JIKA JENIS KELAMIN YANG DIMASUKAN SALAH
    while ulang_jenisKelamin == 1 :    
      jenis_kelamin = input(">> MASUKAN JENIS KELAMIN (L/P)          :    = ")
      if jenis_kelamin.lower() != "l" and jenis_kelamin.lower() != "p" :
        print("JENIS KELAMIN YANG ANDA MASUKAN SALAH !")
      else :
        ulang_jenisKelamin = 0
     
    ulang_golongan = 1 #PERULANGAN JIKA JENIS GOLONGAN YANG DIMASUKAN SALAH
    while ulang_golongan == 1 :    
        golongan = int(input('>> INPUT GOLONGAN (1,2,3)               :    = '))
        if golongan > 3 or golongan < 1 :
          print("GOLONGAN YANG ANDA MASUKAN SALAH !")
        else :
          ulang_golongan = 0 
    
    ulang_statusKawin = 1 #PERULANGAN JIKA STATUS PERKAWINAN YANG DIMASUKAN SALAH 
    while ulang_statusKawin == 1 :    
      statusKawin = input(">> STATUS KAWIN (K=KAWIN B=BELUM KAWIN) :    = ")
      if statusKawin.lower() != "k" and statusKawin.lower() != "b" :
        print("STATUS KAWIN YANG ANDA MASUKAN SALAH !")
      else :
        ulang_statusKawin = 0
        if statusKawin.lower() == "k" : # JIKA SUDAH KAWIN MASUKAN JUMLAH ANAK ONLY INTERGER
         while True:
          try:
            jumlahAnak = int(input('>> JUMLAH ANAK                          :    = '))
            break
          except:
            print("INPUT YANG ANDA MASUKAN SALAH !")
    
    # OUTPUT TAMPILKAN DENGAN HURUF BESAR SEMUA
    print("==========================================")
    print("               SLIP GAJI      ")
    print("           TANGGAL : ",today)
    print("==========================================")
    print("NAMA               : ",nama.upper())
    print("GOLONGAN           : ",golongan)
    print("JENIS KELAMIN      : ",jenis_kelamin.upper())
    print("STATUS KAWIN       : ",statusKawin.upper())
    print("GAJI POKOK         : ",gajipokok[golongan])
    
    tunjanganistri = 0 #DEFAULT VARIABEL TUNJANGAN ISTRI
    if jenis_kelamin.lower() == "l" : # JIKA JENIS KELAMIN LAKI LAKI TAMPILKAN TUNJANGAN ISTRI
      tunjanganistri = gajipokok[golongan] * persentunjangan[golongan] /100 ; 
      print("TUNJANGAN ISTRI    : ",tunjanganistri)  
    tunjangananak = 0 #DEFAULT VARIABEL TUNJANGAN ANAK
    if statusKawin.lower() == "k" : # JIKA STATUS KAWIN TAMPILKAN JUMLAH ANAK
      tunjangananak = gajipokok[golongan] * 2 /100 
      print("TUNJANGAN ANAK     : ",tunjangananak) 
    
    #PERHITUNGAN GAJI
    gajibruto = tunjangananak + tunjanganistri + gajipokok[golongan] 
    iuranjabatan = gajibruto * 0.5 /100
    iuranpensiun = 15500
    iuranorganisasi = 3500
    gajinetto = gajibruto - (iuranjabatan + iuranpensiun + iuranorganisasi)
    print("GAJI BRUTO         : ",gajibruto)
    print("==========================================")
    print("BIAYA JABATAN      : ",iuranjabatan)
    print("IURAN PENSIUN      : ",iuranpensiun)
    print("IUTAN ORGANISASI   : ",iuranorganisasi)
    print("GAJI NETO          : ",gajinetto)
    print("==========================================")
    
    ulangLagi = 1
    while ulangLagi == 1 :
      tambah = input("HITUNG GAJI LAGI Y/T ? ")
      if tambah.lower() != "y" and tambah.lower() != "t" :
        print("INPUT YANG ANDA MASUKAN SALAH !")
      else :
        ulangLagi = 0
        if tambah.lower() == "t" :
          break
