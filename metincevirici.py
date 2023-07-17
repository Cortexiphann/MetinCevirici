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
metin = input("Dönüştürmek istediğiniz metni girin: ")

metin_donusturucu = MetinDonusturucu(metin)

print("Metnin Ters Çevrilmiş Hali:", metin_donusturucu.ters_cevir())
print("Metnin Büyük Harflerle Yazılmış Hali:", metin_donusturucu.buyuk_harfe_cevir())
print("Metnin Küçük Harflerle Yazılmış Hali:", metin_donusturucu.kucuk_harfe_cevir())
