from pathlib import Path
from functools import wraps
import PyInquirer


class Kayit(object):
    def __init__(
        self,
        kimlikNo,
        yeniİsim,
        yeniSoyisim,
        yeniBabaAdı,
        yeniAnneAdı,
        yeniDoğumYeri,
        yeniMedeniHal,
        yeniKanGrubu,
        yeniKütükŞehir,
        yeniKütükİlçe,
        yeniİkametgahŞehir,
        yeniİkametgahİlçe,
    ):
        self.kimlikNo = kimlikNo
        self.yeniİsim = yeniİsim
        self.yeniSoyisim = yeniSoyisim
        self.yeniBabaAdı = yeniBabaAdı
        self.yeniAnneAdı = yeniAnneAdı
        self.yeniDoğumYeri = yeniDoğumYeri
        self.yeniMedeniHal = yeniMedeniHal
        self.yeniKanGrubu = yeniKanGrubu
        self.yeniKütükŞehir = yeniKütükŞehir
        self.yeniKütükİlçe = yeniKütükİlçe
        self.yeniİkametgahŞehir = yeniİkametgahŞehir
        self.yeniİkametgahİlçe = yeniİkametgahİlçe

    @classmethod
    def yeni_kayit(
        cls,
    ):
        kimlikNo = input("Kayıt edilecek kişinin kimlik numarasını giriniz:")
        yeniİsim = input("Kayıt edilecek kişinin ismini giriniz:")
        yeniSoyisim = input("Kayıt edilecek kişinin soyadını giriniz:")
        yeniBabaAdı = input("Kayıt edilecek kişinin baba adını giriniz:")
        yeniAnneAdı = input("Kayıt edilecek kişinin anne adını giriniz:")
        yeniDoğumYeri = input("Kayıt edilecek kişinin doğum yerini giriniz:")
        yeniMedeniHal = input("Kayıt edilecek kişinin medeni durumunu giriniz:")
        yeniKanGrubu = input("Kayıt edilecek kişinin kan grubunu giriniz:")
        yeniKütükŞehir = input("Kayıt edilecek kişinin kütük şehrini giriniz:")
        yeniKütükİlçe = input("Kayıt edilecek kişinin kütük ilçesini giriniz:")
        yeniİkametgahŞehir = input("Kayıt edilecek kişinin ikametgah şehrini giriniz:")
        yeniİkametgahİlçe = input("Kayıt edilecek kişinin ikametgah ilçesini giriniz:")

        return cls(
            kimlikNo,
            yeniİsim,
            yeniSoyisim,
            yeniBabaAdı,
            yeniAnneAdı,
            yeniDoğumYeri,
            yeniMedeniHal,
            yeniKanGrubu,
            yeniKütükŞehir,
            yeniKütükİlçe,
            yeniİkametgahŞehir,
            yeniİkametgahİlçe,
        )

    def __str__(self):
        return """---------------------------------------------------\nKimlik No: {}\nİsim: {}\nSoyisim: {}\nBaba Adı: {}\nAnne Adı: {}\nDogum Yeri {}\nMedeni Hal: {}\nKan Grubu: {}\nKutuk Sehri {}\nKutuk Ilce {}\nIkametgah Sehir: {}\nIkametgah Ilce {}\n--------------------------------------------------""".format(
            self.kimlikNo,
            self.yeniİsim,
            self.yeniSoyisim,
            self.yeniBabaAdı,
            self.yeniAnneAdı,
            self.yeniDoğumYeri,
            self.yeniMedeniHal,
            self.yeniKanGrubu,
            self.yeniKütükŞehir,
            self.yeniKütükİlçe,
            self.yeniİkametgahŞehir,
            self.yeniİkametgahİlçe,
        )

    def virgulle_ayir(self):
        return ",".join(
            [
                self.kimlikNo,
                self.yeniİsim,
                self.yeniSoyisim,
                self.yeniBabaAdı,
                self.yeniAnneAdı,
                self.yeniDoğumYeri,
                self.yeniMedeniHal,
                self.yeniKanGrubu,
                self.yeniKütükŞehir,
                self.yeniKütükİlçe,
                self.yeniİkametgahŞehir,
                self.yeniİkametgahİlçe,
            ]
        )

    @classmethod
    def dosyadan_oku(cls, kayit):
        return cls(*kayit.split(","))

    def degistir(self, secenek, deger):
        secenekler = [
            "yeniİsim",
            "yeniSoyisim",
            "yeniBabaAdı",
            "yeniAnneAdı",
            "yeniDoğumYeri",
            "yeniMedeniHal",
            "yeniKanGrubu",
            "yeniKütükŞehir",
            "yeniKütükİlçe",
            "yeniİkametgahŞehir",
            "yeniİkametgahİlçe",
        ]

        contains = secenek in secenekler

        if contains is True:
            self.__dict__[secenek] = deger


class NufusYonetimi(object):
    def __init__(self):
        self.dosyaAdi = "kisiler.db"
        self.kayitlar = self.dosyadan_oku()

    def dosyadan_oku(self):
        kayitlar = []
        if Path(self.dosyaAdi).exists():
            with open(self.dosyaAdi, "r") as dosya:
                for line in dosya.read().splitlines():
                    kayitlar.append(Kayit.dosyadan_oku(line))

        return kayitlar

    def kayit_ekle(self):
        yeni_kayit = Kayit.yeni_kayit()
        for kayit in self.kayitlar:
            if yeni_kayit.kimlikNo == kayit.kimlikNo:
                print("Bu kimlik numarası başka bir kişiye aittir")
                return

        self.kayitlar.append(yeni_kayit)

    def kisi_silme(self, kimlik_no):
        for kayit in self.kayitlar:
            if kayit.kimlikNo == kimlik_no:
                self.kayitlar.remove(kayit)
                return
        else:
            print("Kimlik no {}'a sahip kayit bulunamadi".format(kimlik_no))

    def kisi_guncelleme(self, kimlik_no):
        degisecek = self.degistirilmek_istenen()
        deger = input("{} icin yeni deger girin: ".format(degisecek))

        for idx, kayit in enumerate(self.kayitlar):
            if kayit.kimlikNo == kimlik_no:
                (self.kayitlar[idx]).degistir(degisecek, deger)
                return
        else:
            print("Kimlik no {}'a sahip kayit bulunamadi".format(kimlik_no))

    def degistirilmek_istenen(self):
        sorular = [
            {
                "name": "secenek",
                "type": "list",
                "message": "Degistirmek istediginz sey?",
                "choices": [
                    "yeniİsim",
                    "yeniSoyisim",
                    "yeniBabaAdı",
                    "yeniAnneAdı",
                    "yeniDoğumYeri",
                    "yeniMedeniHal",
                    "yeniKanGrubu",
                    "yeniKütükŞehir",
                    "yeniKütükİlçe",
                    "yeniİkametgahŞehir",
                    "yeniİkametgahİlçe",
                ],
            }
        ]

        answers = PyInquirer.prompt(sorular)
        return answers.get("secenek")

    def veritabani_listele(self):
        for kayit in self.kayitlar:
            print(kayit)

    def arama(self, kimlik_no):
        for kayit in self.kayitlar:
            if kayit.kimlikNo == kimlik_no:
                print(kayit)

    def veritabanini_guncelle(fonksiyon):
        @wraps(fonksiyon)
        def decorator(self, *args, **kwargs):
            fonksiyon(self, *args, **kwargs)

            with open(self.dosyaAdi, "w") as dosya:
                for kayit in self.kayitlar:
                    dosya.write(kayit.virgulle_ayir() + "\n")

        return decorator

    @veritabanini_guncelle
    def secim_yap(self):
        secimler = [
            {
                "name": "secim",
                "type": "list",
                "message": "Seciniz",
                "choices": [
                    "Çıkış",
                    "Yeni Kayıt Ekleme",
                    "Arama",
                    "Kişi Güncelleme",
                    "Kişi Silme",
                    "Tüm veritabanını listeleme",
                ],
            }
        ]
        secim = PyInquirer.prompt(secimler).get("secim", "Çıkış")

        if secim == "Çıkış":
            print("Çıkış seçildi")
            exit(0)

        elif secim == "Yeni Kayıt Ekleme":
            self.kayit_ekle()

        elif secim == "Arama":
            kimlikno = input("Kimlik no: ")
            self.arama(kimlikno)

        elif secim == "Kişi Güncelleme":
            kimlikno = input("Kimlik no: ")
            self.kisi_guncelleme(kimlikno)

        elif secim == "Kişi Silme":
            kimlikno = input("Kimlik no: ")
            self.kisi_silme(kimlikno)

        elif secim == "Tüm veritabanını listeleme":
            self.veritabani_listele()

        else:
            print("Hatalı giriş!!!")

    def baslat(self):
        print("Toplam {} kayit bulundu".format(len(self.kayitlar)))
        while True:
            self.secim_yap()


NufusYonetimi().baslat()
