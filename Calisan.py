from Calisan(Insan):
  def __init__(self,tc_no,ad,soyad,yas,cinsiyet,uyruk,sektor,tecrube,maas):
    try: 
      super().__init__(tc_no,ad,soyad,yas,cinsiyet,uyruk)
      self.__sektor=sektor
      self.__tecrube=tecrube
      self.__maas=maas
    except Exception as e: 
      print("",str(e))
  def get_sektor(self):
        return self.__sektor
        
  def get_tecrube(self):
        return self.__tecrube

  def set_tecrube(self, tecrube):
        self.__tecrube = tecrube

  def get_maas(self):
        return self.__maas

  def set_maas(self, maas):
        self.__maas = maas
  def zam_hakki(self):
        if self.__tecrube < 2:
            return 0
        elif 2 <= self.__tecrube <= 4 and self.__maas < 15000:
            return self.__maas * (self.__tecrube / 100)
        elif self.__tecrube > 4 and self.__maas < 25000:
            return (self.__maas * (self.__tecrube / 100)) / 2
        else:
            return self.__maas
  def __str__(self):
    try:
      self.zam_hakki()
      return f"{super().__str__()}\nTecrübe: {self.__tecrube}\nYeni Maaş: {self.__maas}"
    except Exception as e:
      print("Hata: ",str(e))
     
    
