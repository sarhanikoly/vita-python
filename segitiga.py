def hitung_luas_segitiga(alas,tinggi):
    luas = 0.5 * alas * tinggi 
    return luas 
def hitung_keliling_segitiga(sisi_a,sisi_b,sisi_c):
    keliling = sisi_a + sisi_b + sisi_c
    return keliling

sisi_a = float(input("Masukkan panjang sisi a:"))
sisi_b = float(input("Masukkan panjang sisi b:"))
sisi_c = float(input("Masukkan panjang sisi c:"))

luas = hitung_luas_segitiga(sisi_a,sisi_b)

keliling = hitung_keliling_segitiga(sisi_a,sisi_b,sisi_c)

print("luas segitiga adalah:",luas)
print("keliling segitiga adalah:",luas)


