from Insan import Insan
class Issiz(Insan):
    def __init__(self, tc_no, ad, soyad, yas, cinsiyet, uyruk, statuler):
        super().__init__(tc_no, ad, soyad, yas, cinsiyet, uyruk)
        self.__statuler=statuler
         
    def get_statuler(self):
        return self.__statuler

    def set_statuler(self):
        self.__statuler=statuler

    def statu_bul(self):
        try:
            max_tecrube = max(self.__statuler.values())
            statu = ''
            for key, value in self.__statuler.items():
                if value == max_tecrube:
                    statu = key
                    break

            return statu
        except ValueError:
            return None

    def __str__(self):
        statu = self.statu_bul()
        if statu is not None:
            return f"Ad: {self.ad}\nSoyad: {self.soyad}\nEn uygun statü: {statu}"
        else:
            return f"Ad: {self.ad}\nSoyad: {self.soyad}\nUygun statü bulunamadı."
