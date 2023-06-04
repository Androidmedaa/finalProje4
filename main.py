import pandas as pd
from Insan import Insan
from Issiz import Issiz
from Calisan import Calisan
from MaviYaka import MaviYaka
from BeyazYaka import BeyazYaka

try: 
    insan1 = Insan("12345678901", "Ziya", "Yılmaz", 30, "Erkek", "Türk") 
    insan2 = Insan("98765432109", "Ayşe", "Demir", 25, "Kadın", "Türk")
    
    issiz1 = Issiz("11111111111", "Ali", "Kaya", 40, "Erkek", "Türk", {"mavi yaka": 2, "beyaz yaka": 1, "yönetici": 0}) 
    issiz2 = Issiz("12345678901", "Ahmet", "Yılmaz", 30, "Erkek", "Yabancı", {"mavi yaka": 4, "beyaz yaka": 6, "yönetici": 3})
    issiz3 = Issiz("98765432109", "Burcu", "Özer", 28, "Kadın", "Türk", {"mavi yaka": 3, "beyaz yaka": 2, "yönetici": 6})
    
    calisan1 = Calisan("44444444444", "Hande", "Alp", 28, "Kadın", "Türk", "teknoloji", 5, 10000) 
    calisan2 = Calisan("55555555555", "Cem", "Yıldız", 35, "Erkek", "Türk", "muhasebe", 7, 77000) 
    calisan3 = Calisan("66666666666", "Mehmet", "Demir", 32, "Erkek", "Türk", "insaat", 3, 9000) 
    
    mavi_yaka1 = MaviYaka("77777777777", "Merve", "Kara", 28, "Kadın", "Türk", "insaat", 4, 9000, 0.2) 
    mavi_yaka2 = MaviYaka("88888888888", "Emir", "Yılmaz", 35, "Erkek", "Türk", "muhasebe", 6, 70000, 0.5) 
    mavi_yaka3 = MaviYaka("99999999999", "Kaan", "Demir", 32, "Erkek", "Türk", "diger", 2, 5500, 0.2) 
    
    beyaz_yaka1 = BeyazYaka("10101010101", "Canan", "Şahin", 28, "Kadın", "Türk", "Pazarlama", 8, 15000, 1500) 
    beyaz_yaka2 = BeyazYaka("12121212121", "Berk", "Yıldız", 35, "Erkek", "Türk", "İnsan Kaynakları", 1, 12000, 2000) 
    beyaz_yaka3 = BeyazYaka("13131313131", "Selin", "Demir", 32, "Kadın", "Türk", "İK", 6, 10400, 2000) 
    
    # Verileri içeren bir sözlük oluşturulması
    data = {
        "Nesne": ["Çalışan", "Çalışan", "Çalışan", "Mavi Yaka", "Mavi Yaka", "Mavi Yaka", "Beyaz Yaka", "Beyaz Yaka", "Beyaz Yaka"],
        "TC No": [calisan1.get_tc_no(), calisan2.get_tc_no(), calisan3.get_tc_no(), mavi_yaka1.get_tc_no(), mavi_yaka2.get_tc_no(), mavi_yaka3.get_tc_no(), beyaz_yaka1.get_tc_no(), beyaz_yaka2.get_tc_no(), beyaz_yaka3.get_tc_no()],
        "Ad": [calisan1.get_ad(), calisan2.get_ad(), calisan3.get_ad(), mavi_yaka1.get_ad(), mavi_yaka2.get_ad(), mavi_yaka3.get_ad(), beyaz_yaka1.get_ad(), beyaz_yaka2.get_ad(), beyaz_yaka3.get_ad()], 
        "Soyad": [calisan1.get_soyad(), calisan2.get_soyad(), calisan3.get_soyad(), mavi_yaka1.get_soyad(), mavi_yaka2.get_soyad(), mavi_yaka3.get_soyad(), beyaz_yaka1.get_soyad(), beyaz_yaka2.get_soyad(), beyaz_yaka3.get_soyad()], 
        "Yaş": [calisan1.get_yas(), calisan2.get_yas(), calisan3.get_yas(), mavi_yaka1.get_yas(), mavi_yaka2.get_yas(), mavi_yaka3.get_yas(), beyaz_yaka1.get_yas(), beyaz_yaka2.get_yas(), beyaz_yaka3.get_yas()], 
        "Cinsiyet": [calisan1.get_cinsiyet(), calisan2.get_cinsiyet(), calisan3.get_cinsiyet(), mavi_yaka1.get_cinsiyet(), mavi_yaka2.get_cinsiyet(), mavi_yaka3.get_cinsiyet(), beyaz_yaka1.get_cinsiyet(), beyaz_yaka2.get_cinsiyet(), beyaz_yaka3.get_cinsiyet()], 
        "Uyruk": [calisan1.get_uyruk(), calisan2.get_uyruk(), calisan3.get_uyruk(), mavi_yaka1.get_uyruk(), mavi_yaka2.get_uyruk(), mavi_yaka3.get_uyruk(), beyaz_yaka1.get_uyruk(), beyaz_yaka2.get_uyruk(), beyaz_yaka3.get_uyruk()], 
        "Sektör": [calisan1.get_sektor(), calisan2.get_sektor(), calisan3.get_sektor(), mavi_yaka1.get_sektor(), mavi_yaka2.get_sektor(), mavi_yaka3.get_sektor(), beyaz_yaka1.get_sektor(), beyaz_yaka2.get_sektor(), beyaz_yaka3.get_sektor()], 
        "Tecrübe": [calisan1.get_tecrube(), calisan2.get_tecrube(), calisan3.get_tecrube(), mavi_yaka1.get_tecrube(), mavi_yaka2.get_tecrube(), mavi_yaka3.get_tecrube(), beyaz_yaka1.get_tecrube(), beyaz_yaka2.get_tecrube(), beyaz_yaka3.get_tecrube()], 
        "Maaş": [calisan1.get_maas(), calisan2.get_maas(), calisan3.get_maas(), mavi_yaka1.get_maas(), mavi_yaka2.get_maas(), mavi_yaka3.get_maas(), beyaz_yaka1.get_maas(), beyaz_yaka2.get_maas(), beyaz_yaka3.get_maas()], 
        "Yıpranma Payı": [0, 0, 0, mavi_yaka1.get_yipranma_payi(), mavi_yaka2.get_yipranma_payi(), mavi_yaka3.get_yipranma_payi(), 0, 0,0], 
        "Teşvik Prim": [0, 0, 0, 0, 0, 0, beyaz_yaka1.get_tesvik_primi(), beyaz_yaka2.get_tesvik_primi(),beyaz_yaka3.get_tesvik_primi()],
        "Yeni Maaş": [calisan1.zam_hakki()+calisan1.get_maas(),calisan2.zam_hakki()+calisan2.get_maas(),calisan3.zam_hakki()+calisan3.get_maas(),mavi_yaka1.get_maas()+mavi_yaka1.zam_hakki(),mavi_yaka2.get_maas()+mavi_yaka2.zam_hakki(),mavi_yaka3.get_maas()+mavi_yaka3.zam_hakki(),beyaz_yaka1.get_maas()+beyaz_yaka1.zam_hakki(),beyaz_yaka2.get_maas()+beyaz_yaka2.zam_hakki(),beyaz_yaka3.get_maas()+beyaz_yaka3.zam_hakki()]}


    # DataFrame'in oluşturulması
    df = pd.DataFrame(data)
    
    # DataFrame üzerinde işlemlerin gerçekleştirilmesi
    df.fillna(0, inplace=True) 
    print("Tecrübe ve Yeni Maaş Ortalamaları:") 
    print(df.groupby("Nesne")[["Tecrübe", "Yeni Maaş"]].mean())
    print("\n15000 TL üzerinde maaş alanların sayısı:", 
    len(df[df["Maaş"] > 15000])) 
    df.sort_values("Yeni Maaş", inplace=True) 
    print("\nYeni Maaşa göre küçükten büyüğe sıralanmış DataFrame:") 
    print(df) 
    print("\n3 yıldan fazla tecrübesi olan Beyaz Yaka çalışanlar:") 
    print(df[(df["Nesne"] == "Beyaz Yaka") & (df["Tecrübe"] > 3)]) 
    print("\nYeni maaşı 10000 TL üzerinde olanlardan 2-5 satır arasındaki çalışanlar için TC No ve Yeni Maaş Bilgisi:") 
    first_df= df[df["Yeni Maaş"] > 10000]
    print(first_df.iloc[1:4][["TC No", "Yeni Maaş"]])
    new_df = df[["Ad", "Soyad", "Sektör", "Yeni Maaş"]] 
    print("\nAd, Soyad, Sektör ve Yeni Maaş bilgilerini içeren yeni DataFrame:") 
    print(new_df) 
except Exception as e:
    print("7. Bir hata oluştu:", str(e))
