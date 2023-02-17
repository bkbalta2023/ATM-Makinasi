print("""

*********************************
ATM MAKİNESİNE HOŞ GELDİNİZ

İŞLEMLER:

1.PARA YATIRMA

2.PARA ÇEKME

3.BAKİYE SORGULAMA

Islem sonlandirma: `q`
*********************************
""")
dogru_sifre = 1995
bakiye = 1000



while True:
    sifre = int(input("Sifrenizi Giriniz: "))
    if (sifre == 1995):
        while True:


            islem = input("Lutfen Yapmak Istediginiz Islemi Secin: ")

            if (islem== "q"):
                print("Isleminiz Sonlandirildi...")
                break
            elif (islem == "1"):
                miktar=int(input("Yatirmak istediginiz tutari giriniz: "))
                bakiye += miktar
                print("Yeni Bakiyeniz: ", bakiye)
            elif (islem== "2"):
                miktar=int(input("Cekmek istediginiz tutari giriniz: "))
                if(miktar > bakiye):
                    print("Yetersiz Bakiye")
                    continue
                else:
                    bakiye -= miktar
                    print("Yeni Bakiyeniz: ", bakiye)
            elif (islem== "3"):
                print("Bakiyeniz: ", bakiye)
            else:
                print("Yanlis islem girdiniz:")
    else:
        print("Yanlis Sifre Girdiniz")

























