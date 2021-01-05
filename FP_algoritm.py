from time import time
from collections import namedtuple
import itertools as iter

reksadana = dict()
Inputt = namedtuple('Input', ['biaya_pernikahan', 'waktu_invest', 'modal','gaji'])
Output = namedtuple('Output', ['dana_darurat', 'invest_bulan'])

I = Inputt(100000000,12,10000000)

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

def invest_modal(uang, waktu_invest):
    hasil = uang
    for i in range (waktu_invest):
        hasil += hasil * 10/100
    return hasil

def reksadana(biaya_pernikahan,waktu_invest,tingkat_resiko):
    biaya_pernikahan = int(biaya_pernikahan)
    tingkat_resiko = tingkat_resiko / 12
    x = 1 + tingkat_resiko / 100
    hasil = biaya_pernikahan / x ** waktu_invest
    e = sum(list(map(lambda x,i : x**i, iter.repeat(x), range(1,waktu_invest+1) )))
    hasil2 = biaya_pernikahan/e
    return (hasil,hasil2)

def waktu_dibutuhkan(biaya_pernikahan, invest_bulan, tingkat_resiko):
    waktu = 0
    invest = invest_bulan
    while int(invest) < int(biaya_pernikahan):
        print(waktu, invest)
        invest += invest * 10/100
        waktu +=1
    return waktu


def reksadana_no_FP(biaya_pernikahan,waktu_invest,tingkat_resiko):
    biaya_pernikahan = int(biaya_pernikahan)
    tingkat_resiko = tingkat_resiko / 12
    x = 1 + tingkat_resiko / 100
    hasil = biaya_pernikahan / x ** waktu_invest
    summ = 0
    for i in range(1, waktu_invest+1):
        summ += x**i
    hasil2 = biaya_pernikahan/summ
    return (hasil,hasil2)

    
def waktu(biaya_pernikahan, invest_bulan ,tingkat_resiko):
    biaya_pernikahan = int(biaya_pernikahan)
    tingkat_resiko = tingkat_resiko / 12
    x = 1 + tingkat_resiko / 100
    summ = 0
    bulan = 0
    while summ*invest_bulan < biaya_pernikahan:
        summ += x**bulan
        bulan += 1    
    return bulan-1
    
    

a,b = reksadana_no_FP(100000000,12,10)
# b = invest_modal(10000000,12)
print(b)
w = waktu(100000000,b,10)
print('waktu', w)


# start = time()
# a=reksadana(100000000, 84, 7)
# print(a)
# end = time()
# print("proccess time",float(end - start))
# b=reksadana_no_FP(100000000, 84, 7)
# print(a.__sizeof__())
# print(b.__sizeof__())