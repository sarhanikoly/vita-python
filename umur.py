def hitung_umur(tahun_lahir):
    tahun_ini= 2024
    umur = tahun_ini-tahun_lahir
    return umur 

tahun_lahir = int(input("Masukan tahun lahir anda:"))

umur = hitung_umur(tahun_lahir)
 
print("umur anda adalah:",umur,"tahun")
