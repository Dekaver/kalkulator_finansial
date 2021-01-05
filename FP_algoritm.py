from time import time
from collections import namedtuple
import itertools as iter
from multiprocessing import Pool

Reksadana_value = (12, 10.5, 6, 7.5)
Reksadana = namedtuple('Reksadana', ['saham', 'obligasi', 'pasar_uang', 'syariah'])
R = Reksadana(*Reksadana_value)

Input1 = namedtuple('Input', ['biaya_pernikahan', 'waktu_invest', 'modal', 'jenis_invest'])
Output1 = namedtuple('Output', ['invest_bulan', 'Total_untung', 'total_uang'])
Input2 = namedtuple('Input', ['biaya_pernikahan', 'waktu_invest', 'gaji', 'resiko'])
Output2 = namedtuple('Output', ['invest_bulan', 'Total_untung', 'total_uang'])

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

def jumlah(x , i):
    x = iter.repeat(x)
    bulan = range(1, i+1)
    return sum(list(map(lambda x,i : x**i, x, bulan)))
    
def jumlah2(x,i):
    summ = 0
    bulan = range(1, i+1)
    for i in bulan:
        summ += x**i
    return summ

def invest_modal(uang, waktu_invest, jenis_invest):
    hasil = uang
    for i in range (waktu_invest):
        hasil = hasil + hasil * jenis_invest/100
    return hasil

def hitung_invest_bulan(biaya_pernikahan,waktu_invest,jenis_invest):
    biaya_pernikahan = int(biaya_pernikahan)
    jenis_invest = jenis_invest / 12
    x = 1 + jenis_invest / 100
    hasil = biaya_pernikahan / x ** waktu_invest
    e = jumlah(x, waktu_invest)
    hasil2 = biaya_pernikahan/e
    return (int(hasil),int(hasil2))


def reksadana_no_FP(biaya_pernikahan,waktu_invest,tingkat_resiko):
    biaya_pernikahan = int(biaya_pernikahan)
    tingkat_resiko = tingkat_resiko / 12
    x = 1 + tingkat_resiko / 100
    hasil = biaya_pernikahan / x ** waktu_invest
    summ = jumlah2(x,waktu_invest)
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
    
    
# if __name__ == '__main__':
#     a,b = reksadana(100000000,12,15)
#     # b = invest_modal(10000000,12)
#     print(a,b)
#     w = waktu(100000000,b,10)
#     print('waktu', w)
    
