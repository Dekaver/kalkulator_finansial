from tkinter import *
from tkinter import ttk
import tkinter as tk
from FP_algoritm import *


window = tk.Tk()
# window.maxsize(540, 320) 
# window.minsize(540, 320) 
window.geometry("1000x540")
window.resizable(0,0)
window.title("Kalkulator Pesiapan Dana Pernikahan")


Label(
    window, 
    text='Kalkulator Persiapan Dana Pernikahan ', 
    font=('times new roman', 16)
    ).grid(
        column = 1,  
        columnspan = 2,      
        row=1
        )

Label(
    window, 
    text='Kalkulator Waktu Investasi ', 
    font=('times new roman', 16)
    ).grid(
        column = 3,  
        columnspan = 2,      
        row=1
        )

#Side Kiri
Label(
    window, 
    text='Biaya Pernikahan', 
    font=('times new roman', 16)
    ).grid(
        column = 1,        
        row=2
        )

txt_biayaPernikahan = Entry(font=('Helvetica',20,'bold'), justify='right', fg='Grey', bd='5')
txt_biayaPernikahan.insert(0, 0)
txt_biayaPernikahan.bind("<FocusIn>", lambda args: focus_in_entry_box(txt_biayaPernikahan))
txt_biayaPernikahan.bind("<FocusOut>", lambda args: focus_out_entry_box(txt_biayaPernikahan, 0))
txt_biayaPernikahan.grid( column= 2, row=2, pady=5)

Label(
    window, 
    text='Modal ', 
    font=('times new roman', 16)
    ).grid(
        column = 1,        
        row=3
        )

txt_modal = Entry(font=('Helvetica',20,'bold'), justify='right', fg='Grey', bd='5')
txt_modal.insert(0, 0)
txt_modal.bind("<FocusIn>", lambda args: focus_in_entry_box(txt_modal))
txt_modal.bind("<FocusOut>", lambda args: focus_out_entry_box(txt_modal, 0))
txt_modal.grid( column= 2, row=3, pady=5)

Label(
    window, 
    text='Waktu ', 
    font=('times new roman', 16)
    ).grid(
        column = 1,        
        row=4
        )

txt_waktu_invest = Entry(font=('Helvetica',20,'bold'), justify='right', fg='Grey', bd='5')
txt_waktu_invest.insert(0, '/bulan')
txt_waktu_invest.bind("<FocusIn>", lambda args: focus_in_entry_box(txt_waktu_invest))
txt_waktu_invest.bind("<FocusOut>", lambda args: focus_out_entry_box(txt_waktu_invest, 0))
txt_waktu_invest.grid( column= 2, row=4, pady=5)

Label(
    window, 
    text='Jenis Investasi ', 
    font=('times new roman', 16)
    ).grid(
        column = 1,        
        row=5
        )    

cbb_jenis_invest = ttk.Combobox(window,value=['Pasar Uang', 'Syariah', 'Obligasi', 'Saham'], state="readonly")
cbb_jenis_invest.config(width=26, font=('times new roman', 16))
cbb_jenis_invest.grid(column=2, row=5, pady=5)
cbb_jenis_invest.current(0)


Label(
    window, 
    text='Investasi Perbulan ', 
    font=('times new roman', 16)
    ).grid(
        column = 1,        
        row=7
        )
entry_invest_perbulan = StringVar()
entry_invest_perbulan.set(0)
text_invest_perbulan = Entry(font=('Helvetica',20,'bold'), textvariable=entry_invest_perbulan, justify='right', fg='Grey', bd='5', state='readonly')
text_invest_perbulan.grid( column= 2, row=7, pady=5)


Label(
    window, 
    text='Total Keuntungan ', 
    font=('times new roman', 16)
    ).grid(
        column = 1,        
        row=8
        ) 
entry_totalKeuntungan = StringVar()
entry_totalKeuntungan.set(0)
txt_totalKeuntungan = Entry(font=('Helvetica',20,'bold'), textvariable=entry_totalKeuntungan, justify='right', fg='Grey', bd='5', state = 'readonly')
txt_totalKeuntungan.grid( column= 2, row=8, pady=5)


Label(
    window, 
    text='Total Dana ', 
    font=('times new roman', 16)
    ).grid(
        column = 1,        
        row=9
        )  
entry_totalDana = StringVar()
entry_totalDana.set(0)
txt_totalDana = Entry(font=('Helvetica',20,'bold'), textvariable = entry_totalDana, justify='right', fg='Grey', bd='5', state='readonly')
txt_totalDana.grid( column= 2, row=9, pady=5)




#Side Kanan

Label(
    window, 
    text='Biaya Pernikahan ', 
    font=('times new roman', 16)
    ).grid(
        column = 3,        
        row=2
        )

txt_biayaPernikahan2 = Entry(font=('Helvetica',20,'bold'), justify='right', fg='Grey', bd='5')
txt_biayaPernikahan2.insert(0, 0)
txt_biayaPernikahan2.bind("<FocusIn>", lambda args: focus_in_entry_box(txt_biayaPernikahan2))
txt_biayaPernikahan2.bind("<FocusOut>", lambda args: focus_out_entry_box(txt_biayaPernikahan2, 0))
txt_biayaPernikahan2.grid( column= 4, row=2, pady=5)

Label(
    window, 
    text='Modal', 
    font=('times new roman', 16)
    ).grid(
        column = 3,        
        row=3
        )

txt_modal2 = Entry(font=('Helvetica',20,'bold'), justify='right', fg='Grey', bd='5')
txt_modal2.insert(0, 0)
txt_modal2.bind("<FocusIn>", lambda args: focus_in_entry_box(txt_modal2))
txt_modal2.bind("<FocusOut>", lambda args: focus_out_entry_box(txt_modal2, 0))
txt_modal2.grid( column= 4, row=3, pady=5)

Label(
    window, 
    text='Gaji Perbulan', 
    font=('times new roman', 16)
    ).grid(
        column = 3,        
        row=4
        )

txt_gajiPerbulan = Entry(font=('Helvetica',20,'bold'), justify='right', fg='Grey', bd='5')
txt_gajiPerbulan.insert(0, 0)
txt_gajiPerbulan.bind("<FocusIn>", lambda args: focus_in_entry_box(txt_gajiPerbulan))
txt_gajiPerbulan.bind("<FocusOut>", lambda args: focus_out_entry_box(txt_gajiPerbulan, 0))
txt_gajiPerbulan.grid( column= 4, row=4, pady=5)

Label(
    window, 
    text='Tingkat Resiko ', 
    font=('times new roman', 16)
    ).grid(
        column = 3,        
        row=5
        )    

cbb_tingkatResiko = ttk.Combobox(window,value=['Saham', 'Obligasi', 'Kontrak Investasi'], state="readonly")
cbb_tingkatResiko.config(width=26, font=('times new roman', 16))
cbb_tingkatResiko.grid(column=4, row=5, pady=5)
cbb_tingkatResiko.current(0)

Label(
    window, 
    text='Opsi Investasi', 
    font=('times new roman', 16)
    ).grid(
        column = 3,        
        row=7
        )

txt_opsiInvestasi = Entry(font=('Helvetica',20,'bold'), justify='right', fg='Grey', bd='5')
txt_opsiInvestasi.insert(0, 0)
txt_opsiInvestasi.bind("<FocusIn>", lambda args: focus_in_entry_box(txt_opsiInvestasi))
txt_opsiInvestasi.bind("<FocusOut>", lambda args: focus_out_entry_box(txt_opsiInvestasi, 0))
txt_opsiInvestasi.grid( column= 4, row=7, pady=5)

Label(
    window, 
    text='Jangka Waktu', 
    font=('times new roman', 16)
    ).grid(
        column = 3,        
        row=8
        )

txt_jangkaWaktu = Entry(font=('Helvetica',20,'bold'), justify='right', fg='Grey', bd='5')
txt_jangkaWaktu.insert(0, 0)
txt_jangkaWaktu.bind("<FocusIn>", lambda args: focus_in_entry_box(txt_jangkaWaktu))
txt_jangkaWaktu.bind("<FocusOut>", lambda args: focus_out_entry_box(txt_jangkaWaktu, 0))
txt_jangkaWaktu.grid( column= 4, row=8, pady=5)

Label(
    window, 
    text='Skema Investasi', 
    font=('times new roman', 16)
    ).grid(
        column = 3,        
        row=9
        )

txt_skemaInvestasi = Entry(font=('Helvetica',20,'bold'), justify='right', fg='Grey', bd='5')
txt_skemaInvestasi.insert(0, 0)
txt_skemaInvestasi.bind("<FocusIn>", lambda args: focus_in_entry_box(txt_skemaInvestasi))
txt_skemaInvestasi.bind("<FocusOut>", lambda args: focus_out_entry_box(txt_skemaInvestasi, 0))
txt_skemaInvestasi.grid( column= 4, row=9, pady=5)

def focus_out_entry_box(widget, widget_text):
    if widget['fg'] == 'Black' and len(widget.get()) == 0:
        widget.delete(0, END)
        widget['fg'] = 'Grey'
        widget.insert(0, widget_text)
        
def focus_in_entry_box(widget):
    if widget['fg'] == 'Grey':
        widget['fg'] = 'Black'
        widget.delete(0, END)

def hitung1():
    biaya = txt_biayaPernikahan.get()
    modal = txt_modal.get()
    jenis_invest = cbb_jenis_invest.get()
    waktu = txt_waktu_invest.get()
    if jenis_invest == "Pasar Uang":
        jenis_invest = R.pasar_uang
    elif jenis_invest == 'Syariah':
        jenis_invest = R.syariah
    elif jenis_invest == 'Obligasi':
        jenis_invest = R.obligasi
    else :
        jenis_invest = R.saham
    Input = Input1(int(biaya), int(waktu), int(modal), int(jenis_invest))
    modal = invest_modal(Input.modal, Input.waktu_invest, Input.jenis_invest)

    hasil1, hasil2 = hitung_invest_bulan(int(Input.biaya_pernikahan) - modal, int(Input.waktu_invest), int(Input.jenis_invest))

    totalDana = hasil2 * Input.waktu_invest
    hasilInvest = invest_modal(hasil2, Input.waktu_invest, Input.jenis_invest)
    print(hasilInvest,hasil2)
    txt_biayaPernikahan.delete(0, END)
    txt_biayaPernikahan.insert(0, formatrupiah(Input.biaya_pernikahan))
    txt_modal.delete(0,END)
    txt_modal.insert(0, formatrupiah(Input.modal))
    entry_totalDana.set(formatrupiah(totalDana))
    entry_totalKeuntungan.set(formatrupiah(hasilInvest - totalDana + modal))
    entry_invest_perbulan.set(formatrupiah(hasil2))

def hitung2():
    pass

btn_hitung = Button(window, text='HITUNG INVEST', height=2, width=20, bg='gray', bd=6, command = hitung1)
btn_hitung.grid(row = 6 , column = 2)

btn_hitung = Button(window, text='HITUNG WAKTU', height=2, width=20, bg='gray', bd=6, command = hitung2)
btn_hitung.grid(row = 6 , column = 4)

# btn_hitung = Button(window, text='HITUNG WAKTU', height=2, width=20, bg='gray', bd=6, command = hitung)
# btn_hitung.grid(row = 7 , column = 2 )


window.mainloop()



