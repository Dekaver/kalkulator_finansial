import itertools as iter

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

def reksadana(biaya_pernikahan,waktu_invest,tingkat_resiko):
    biaya_pernikahan = int(biaya_pernikahan)
    tingkat_resiko = tingkat_resiko / 12
    x = 1 + tingkat_resiko / 100
    hasil = biaya_pernikahan / x ** waktu_invest
    e = sum(list(map(lambda x,i : x**i, iter.repeat(x), range(1,waktu_invest+1) )))
    hasil2 = biaya_pernikahan/e
    return (int(hasil), int(hasil2))
