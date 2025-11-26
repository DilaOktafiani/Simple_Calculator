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

root = tk.Tk()
root.title("SIMPLE CALCULATOR")
root.geometry("300x400")

layar = Entry(root, font=("Arial", 18), border=3, relief="ridge", justify="right")
layar.pack(fill="both", padx=10, pady=10)

tombol_list =[
'7','8','9','/'
'4','5','6','*'
'1','2','3','-'
'0','.','=','+'
]

frame = tk.Frame(root)
frame.pack()

row = 0
col = 0

for tombol in tombol_list:
    if tombol == "=":
        btn = Button(frame, text=tombol, width=5, height=2, font=("Arial", 14), command=hitung)
    else:
        btn = Button(frame, text=tombol, width=5, height=2, font=("Arial", 14), command=lambda t=tombol:klik(t))

    btn.grid(row=row, column=col, padx=5, pady=5)

    col += 1
    if col > 3:
        col = 0
        row += 1

btn_clear = Button(root, text="Clear", width=10, height=2, font=("Arial", 14), command=hapus)
btn_clear.pack(pady=10)

root.mainloop()