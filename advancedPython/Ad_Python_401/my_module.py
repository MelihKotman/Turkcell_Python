#from math import pi

pi = 3.14

def topla(a, b):
    return a + b
def daireCevreHesapla(r):
    return 2* pi * r
def daireAlanHesapla(r): #Fonksiyon tanımı için fonksiyon içinde üç tırnak kullanırsan bu şekilde yaparsın
    """

    :param r: dairenin yarı çapı
    :return: dairenin alanını hesaplar
    """
    return (pi ** 2) * r

if __name__ == '__main__':
    print(topla(3,4))

print(__name__)
