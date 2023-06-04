from Calisan import Calisan

class BeyazYaka(Calisan):
    def __init__(self, tc_no, ad, soyad, yas, cinsiyet, uyruk, sektor, tecrube, maas, tesvik_primi):
        super().__init__(tc_no, ad, soyad, yas, cinsiyet, uyruk, sektor, tecrube, maas)
        self.__tesvik_primi = tesvik_primi

    def get_tesvik_primi(self):
        return self.__tesvik_primi

    def set_tesvik_primi(self, tesvik_primi):
        self.__tesvik_primi = tesvik_primi

    def zam_hakki(self):
        try:
            if self.get_tecrube() < 2:
                return self.get_tesvik_primi()
            elif 2 <= self.get_tecrube() <= 4 and self.get_maas() < 15000:
                return (self.get_maas() % self.get_tecrube()) * 5 + self.get_tesvik_primi()
            elif self.get_tecrube() > 4 and self.get_maas() < 25000:
                return (self.get_maas() % self.get_tecrube()) * 4 + self.get_tesvik_primi()
            else:
                return self.get_maas()
        except Exception as e:
            print("Hata oluştu:", str(e))

    def __str__(self):
        try:
            return f"{super().__str__()}\nTeşvik Primi: {self.get_tesvik_primi()}"
        except Exception as e:
            print("Hata oluştu:", str(e))
