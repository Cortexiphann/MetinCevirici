#FurkanFilikci
class MetinDonusturucu:
    def __init__(self, metin):
        self.metin = metin
    
    def ters_cevir(self):
        return self.metin[::-1]
    
    def buyuk_harfe_cevir(self):
        return self.metin.upper()
    
    def kucuk_harfe_cevir(self):
        return self.metin.lower()

# Kullanıcıdan bir metin iste
metin = input("Dönüştürmek İstediğiniz Metni Girin: ")
metin_donusturucu = MetinDonusturucu(metin)

# Kullanıcıya dönüştürme seçeneklerini göster
print("Dönüştürme Seçenekleri:")
print("1. Metnin Ters Çevrilmiş Hali")
print("2. Metnin Büyük Harflerle Yazılmış Hali")
print("3. Metnin Küçük Harflerle Yazılmış Hali")

secim = input("Yapmak istediğiniz dönüşümün numarasını girin (1/2/3): ")

if secim == "1":
    print("Metnin Ters Çevrilmiş Hali:", metin_donusturucu.ters_cevir())
elif secim == "2":
    print("Metnin Büyük Harflerle Yazılmış Hali:", metin_donusturucu.buyuk_harfe_cevir())
elif secim == "3":
    print("Metnin Küçük Harflerle Yazılmış Hali:", metin_donusturucu.kucuk_harfe_cevir())
else:
    print("Geçersiz seçim! Lütfen 1, 2 veya 3 numaralarından birini girin.")
