# from multiprocessing import Pool

# def f(x):
#     return x*x

# if __name__ == '__main__':
#     with Pool(2) as p:
#         print(p.map(f, [1, 2, 3]))

import math
import itertools as iter
print("Kalkulator Biaya Pernikahan & solusi buat kamu\n")
# Txt_Biaya = input('Biaya :')
# Txt_modal = input('Modal :')
Txt_Biaya = '100000000'
bulannya = 12
resiko = 7

Jenis_investasi = (
    ('reksadana' , '20%'),
    ('saham' , '12%'),
    ('obligasi' , '5.7%')
)

uang = 20000000

def formatrupiah(u, last= True):
    s = str(u)
    if len(s) > 3 :
        if (last):
            a = s[-3:] + ',00'
        else:
            a = s[-3:]
        b = s[:-3]
        return formatrupiah(b,False) + '.' + a
    else :
        return 'Rp ' + s

def bulan(x = None):
    if x == None:
        for i in range(1,7):
            yield i*6
    else:
        yield x

# def hitung():
#     b=bulan(8)
#     reksadana(Txt_Biaya, b)

# def obligasi(x):
#     pass

# def saham(x):
#     pass


def reksadana(biaya_pernikahan,waktu_invest,tingkat_resiko):
    biaya_pernikahan = int(biaya_pernikahan)
    tingkat_resiko = tingkat_resiko / 12
    x = 1 + tingkat_resiko / 100
    hasil = biaya_pernikahan / x ** waktu_invest
    e = sum(list(map(lambda x, i : x**i, iter.repeat(x), range(1, waktu_invest+1))))
    hasil2 = biaya_pernikahan/e
    return (int(hasil), int(hasil2))




reksa = reksadana(Txt_Biaya, bulannya, resiko)

a, b = map(formatrupiah, reksa)
print(a, b)

# reksadana(3,waktu)
    # 1.000.000 x 10/100 + 1.000.000 = 1.200.000
    # 1.000.000 x (20/2)*1/100 + 1.000.000 = 1.200.000

    # a x 1.6/100 + a = 100.000.000
    # a x 101.67/100  = 100.000.000

    # a x 10/100 + a  = 100.000.000
    # a x 110/100    = 100.000.000
    # a = 100.000.000 x 100 /110
    # a = 90.909.090

