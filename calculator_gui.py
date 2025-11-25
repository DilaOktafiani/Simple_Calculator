import tkinter as tk
from tkinter import Entry, Button, END

# Fungsi untuk menambah angka ke layar
def klik(tombol):
    layar.insert(END, tombol)

# Fungsi hitung
def hitung():
    try:
        hasil = eval(layar.get())
        layar.delete(0, END)
        layar.insert(END, hasil)
    except:
        layar.delete(0, END)
        layar.insert(END, "Error")

# Fungsi clear
def hapus():
    layar.delete(0, END)
    