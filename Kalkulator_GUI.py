from tkinter import *
from tkinter import ttk
import tkinter as tk
from FP_algoritm import reksadana, formatrupiah


window = tk.Tk()
window.maxsize(540, 320) 
window.minsize(540, 320) 
window.geometry("540x320")
window.title("Calculator")

Label(
    window, 
    text='Biaya Pernikahan', 
    font=('times new roman', 16)
    ).grid(
        column = 1,
        row = 1
        )

Label(
    window, 
    text='Modal', 
    font=('times new roman', 16)
    ).grid(
        column = 1,
        row = 2
        )

Label(
    window, 
    text='Waktu yang di inginkan', 
    font=('times new roman', 16)
    ).grid(
        column = 1,
        row = 3
        )

Label(
    window, 
    text='Reksadana', 
    font=('times new roman', 16)
    ).grid(
        column = 1,
        row = 4
        )

Label(
    window, 
    text='Modal yang Dibutuhkan', 
    font=('times new roman', 16)
    ).grid(
        column = 1,
        row = 5
        )

Label(
    window, 
    text='Tabungan Per Bulan', 
    font=('times new roman', 16)
    ).grid(
        column = 1,
        row = 6
        )
        

txt_biaya = Entry(font=('Helvetica',20,'bold'), justify='right', fg='Grey', bd='5')
txt_biaya.insert(0, 0)
txt_biaya.bind("<FocusIn>", lambda args: focus_in_entry_box(txt_biaya))
txt_biaya.bind("<FocusOut>", lambda args: focus_out_entry_box(txt_biaya, 0))
txt_biaya.grid(columnspan=2, column= 2, row=1)

txt_modal = Entry(font=('Helvetica',20,'bold'), justify='right', fg='Grey', bd='5')
txt_modal.insert(0, 0)
txt_modal.bind("<FocusIn>", lambda args: focus_in_entry_box(txt_modal))
txt_modal.bind("<FocusOut>", lambda args: focus_out_entry_box(txt_modal, 0))
txt_modal.grid(columnspan=2, column= 2, row=2)


txt_waktu_invest = Entry(font=('Helvetica',20,'bold'), justify='right', fg='Grey', bd='5')
txt_waktu_invest.insert(0, '/bulan')
txt_waktu_invest.bind("<FocusIn>", lambda args: focus_in_entry_box(txt_waktu_invest))
txt_waktu_invest.bind("<FocusOut>", lambda args: focus_out_entry_box(txt_waktu_invest, 0))
txt_waktu_invest.grid(columnspan=2, column= 2, row=3)

entry_uang_yang_dibutuhkan = IntVar()
txt_uang_yg_dibutuhkan = Entry(font=('Helvetica',20,'bold'), textvariable=entry_uang_yang_dibutuhkan, justify='right', fg='Grey', bd='5', state='readonly')
txt_uang_yg_dibutuhkan.grid(columnspan=2, column=2, row=5)

entry_tabungan_perbulan = IntVar()
entry_tabungan_perbulan.set(0)
txt_tabungan_Perbulan = Entry(font=('Helvetica',20,'bold'), textvariable=entry_tabungan_perbulan, justify='right', fg='Grey', bd='5', state='readonly')
txt_tabungan_Perbulan.grid(columnspan=2, column= 2, row=6)

cbb_reksadana = ttk.Combobox(window,value=['Saham', 'Obligasi', 'Kontrak Investasi'], state="readonly")
cbb_reksadana.config(width=10, font=('times new roman', 16))
cbb_reksadana.grid(column=2, row=4)
cbb_reksadana.current(0)

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
    txt_biaya.insert(0,formatrupiah(biaya))
    entry_tabungan_perbulan.set(formatrupiah(hasil2))
    entry_uang_yang_dibutuhkan.set(formatrupiah(hasil1))
    

btn_hitung = Button(window, text='Hitung', height=2, width=10, bg='gray', bd=6, command = hitung)
btn_hitung.grid(row = 7 , column = 2)

window.mainloop()



