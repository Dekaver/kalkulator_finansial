from tkinter import *
from tkinter import ttk
import tkinter as tk
from FP_algoritm import *


window = tk.Tk()
# window.maxsize(540, 320) 
# window.minsize(540, 320) 
window.geometry("540x580")
window.resizable(0,0)
window.title("Kalkulator Pesiapan Dana Pernikahan")


# Label(
#     window, 
#     text='Kalkulator Persiapan Dana Pernikahan ', 
#     font=('times new roman', 16)
#     ).grid(
#         column = 1,  
#         columnspan = 2,      
#         row=1
#         )


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
txt_biayaPernikahan.grid(columnspan=2, column= 2, row=2, pady=5)


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
txt_modal.grid(columnspan=2, column= 2, row=3, pady=5)


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
txt_waktu_invest.grid(columnspan=2, column= 2, row=4, pady=5)


# Label(
#     window, 
#     text='Gaji Perbulan ', 
#     font=('times new roman', 16)
#     ).grid(
#         column = 1,        
#         row=5
#         )   

# txt_pengeluaranPerbulan = Entry(font=('Helvetica',20,'bold'), justify='right', fg='Grey', bd='5')
# txt_pengeluaranPerbulan.insert(0, 0)
# txt_pengeluaranPerbulan.bind("<FocusIn>", lambda args: focus_in_entry_box(txt_pengeluaranPerbulan))
# txt_pengeluaranPerbulan.bind("<FocusOut>", lambda args: focus_out_entry_box(txt_pengeluaranPerbulan, 0))
# txt_pengeluaranPerbulan.grid(columnspan=2, column= 2, row=5, pady=5)


Label(
    window, 
    text='Jenis Investasi ', 
    font=('times new roman', 16)
    ).grid(
        column = 1,        
        row=6
        )    

cbb_reksadana = ttk.Combobox(window,value=['Saham', 'Obligasi', 'Kontrak Investasi'], state="readonly")
cbb_reksadana.config(width=26, font=('times new roman', 16))
cbb_reksadana.grid(column=2, row=6, pady=5)
cbb_reksadana.current(0)


Label(
    window, 
    text='Investasi Perbulan ', 
    font=('times new roman', 16)
    ).grid(
        column = 1,        
        row=8
        )

text_invest_perbulan = Entry(font=('Helvetica',20,'bold'), justify='right', fg='Grey', bd='5')
text_invest_perbulan.insert(0, 0)
text_invest_perbulan.bind("<FocusIn>", lambda args: focus_in_entry_box(text_invest_perbulan))
text_invest_perbulan.bind("<FocusOut>", lambda args: focus_out_entry_box(text_invest_perbulan, 0))
text_invest_perbulan.grid(columnspan=2, column= 2, row=8, pady=5)


Label(
    window, 
    text='Total Keuntungan ', 
    font=('times new roman', 16)
    ).grid(
        column = 1,        
        row=9
        )  
txt_danaDarurat = Entry(font=('Helvetica',20,'bold'), justify='right', fg='Grey', bd='5')
txt_danaDarurat.insert(0, 0)
txt_danaDarurat.bind("<FocusIn>", lambda args: focus_in_entry_box(txt_danaDarurat))
txt_danaDarurat.bind("<FocusOut>", lambda args: focus_out_entry_box(txt_danaDarurat, 0))
txt_danaDarurat.grid(columnspan=2, column= 2, row=9, pady=5)


Label(
    window, 
    text='Total Dana ', 
    font=('times new roman', 16)
    ).grid(
        column = 1,        
        row=10
        )      
txt_totalDana = Entry(font=('Helvetica',20,'bold'), justify='right', fg='Grey', bd='5')
txt_totalDana.insert(0, 0)
txt_totalDana.bind("<FocusIn>", lambda args: focus_in_entry_box(txt_totalDana))
txt_totalDana.bind("<FocusOut>", lambda args: focus_out_entry_box(txt_totalDana, 0))
txt_totalDana.grid(columnspan=2, column= 2, row=10, pady=5)

def focus_out_entry_box(widget, widget_text):
    if widget['fg'] == 'Black' and len(widget.get()) == 0:
        widget.delete(0, END)
        widget['fg'] = 'Grey'
        widget.insert(0, widget_text)
        
def focus_in_entry_box(widget):
    if widget['fg'] == 'Grey':
        widget['fg'] = 'Black'
        widget.delete(0, END)

def hitung():
    biaya = txt_biaya.get()
    modal = txt_modal.get()
    reksa = cbb_reksadana.get()
    waktu = txt_waktu_invest.get()
    if reksa == "Saham":
        reksa = 7
    elif reksa == 'Obligasi':
        reksa = 15
    elif reksa == 'Kontrak Investasi':
        reksa = 19
    else :
        reksa = 12
    hasil1, hasil2 = reksadana(int(biaya) - int(modal), int(waktu), reksa)
    # txt_biaya.insert(0,formatrupiah(biaya))
    # entry_tabungan_perbulan.set(formatrupiah(hasil2))
    # entry_uang_yang_dibutuhkan.set(formatrupiah(hasil1))
    

btn_hitung = Button(window, text='HITUNG INVEST', height=2, width=20, bg='gray', bd=6, command = hitung)
btn_hitung.grid(row = 7 , column = 2)

# btn_hitung = Button(window, text='HITUNG WAKTU', height=2, width=20, bg='gray', bd=6, command = hitung)
# btn_hitung.grid(row = 7 , column = 2 )


window.mainloop()



