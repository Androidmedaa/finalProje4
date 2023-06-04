class Insan:
  def __init__(self,tc_no,ad,soyad,yas,cinsiyet,uyruk):
    self.__tc_no=tc_no
    self.__ad=ad
    self.__soyad=soyad
    self.__yas=yas
    self.__cinsiyet=cinsiyet
    self.__uyruk=uyruk
  def get_tc_no(self):
        return self.__tc_no
  def set_tc_no(self):
        self.__tc_no = tc_no
    
  def get_ad(self):
        return self.__ad
  def set_ad(self):
        self.__ad = ad
    
  def get_soyad(self):
        return self.__soyad
  def set_soyad(self):
        self.__soyad = soyad   

  def get_yas(self):
        return self.__yas 
  def set_yas(self):
        self.__yas = yas

  def get_cinsiyet(self):
        return self.__cinsiyet
  def set_cinsiyet(self):
        self.__cinsiyet = cinsiyet
    
  def get_uyruk(self):
        return self.__uyruk 
  def set_uyruk(self):
        self.__uyruk=uyruk
  def __str__(self):
        try:
            return f"Ad: {self.get_ad()}\nSoyad: {self.get_soyad()}\nYaş: {self.get_yas()}\nCinsiyet: {self.get_cinsiyet()}\nUyruk: {self.get_uyruk()}"

        except Exception as e:
            print("1.Hata oluştu:", str(e))
