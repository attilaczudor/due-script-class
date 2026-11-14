import kocka_class
import tkinter as tk
from tkinter import ttk, messagebox

class KockaApp(kocka_class.Kockadobas):
    def __init__(self, root):
        super().__init__(root)
        self.mentes_gomb = ttk.Button(root, text='Mentés', command=self.mentes)
        self.mentes_gomb.grid(column=0, row=3)

    def mentes(self):
        if sum(self.eredmenyek.values()) == 0:
            messagebox.showwarning('Dobás', 'Először dobjon')
            return
        sor = f'{self.eredmenyek}\n'
        try:
            with open('mentes.txt', 'a', encoding='utf-8') as f:
                f.write(sor)
            messagebox.showinfo('Mentés', 'Sikeres volt a Mentés')
        except OSError:
            messagebox.showerror('Hiba', 'Nem sikerült a Mentés')

if __name__ == "__main__":
    root = tk.Tk()
    app = KockaApp(root)
    root.mainloop()
