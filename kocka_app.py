import kocka_class
import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
import csv
import json
import os
import random

class KockaApp(kocka_class.Kockadobas):
    def __init__(self, root):
        super().__init__(root)
        self.mentes_gomb = ttk.Button(root, text='Mentés - TEXT', command=self.mentes)
        self.mentes_gomb.grid(column=0, row=3)

        self.mentes_csv_gomb = ttk.Button(root, text='Mentés - CSV', command=self.mentes_csv)
        self.mentes_csv_gomb.grid(column=1, row=3)

        self.mentes_json_gomb = ttk.Button(root, text='Mentés - JSON', command=self.mentes_json)
        self.mentes_json_gomb.grid(column=2, row=3)

        self.veletlen_gomb = ttk.Button(root, text='Dobásszám', command=self.veletlen_dobasszam)
        self.veletlen_gomb.grid(column=1, row=1)

    def veletlen_dobasszam(self):
        szam = random.randint(10, 500)
        self.dobas_szam.set(str(szam))
        self.dobas()

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

    def mentes_csv(self):
        if sum(self.eredmenyek.values()) == 0:
            messagebox.showwarning('Dobás', 'Először dobjon')
            return
        fajlnev = 'mentes.csv'
        adatok = self.eredmenyek.copy()
        adatok['Dátum'] = datetime.now().strftime('%Y.%m.%d')
        fejlec_kell = not os.path.exists(fajlnev) or os.path.getsize(fajlnev) == 0
        try:
            with open(fajlnev, mode='a', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                if fejlec_kell:
                    writer.writerow(adatok.keys())
                writer.writerow(adatok.values())
            messagebox.showinfo('Mentés', 'Sikeres volt a Mentés')
        except OSError:
            messagebox.showerror('Hiba', 'Nem sikerült a Mentés')

    def mentes_json(self):
        if sum(self.eredmenyek.values()) == 0:
            messagebox.showwarning('Dobás', 'Először dobjon')
            return
        fajlnev = 'mentes.json'
        adatok = self.eredmenyek.copy()
        adatok['Dátum'] = datetime.now().strftime('%Y.%m.%d')
        mentett_adatok = []
        if os.path.exists(fajlnev):
            try:
                with open(fajlnev, mode='r', encoding='utf-8') as f:
                    mentett_adatok = json.load(f)
            except (json.JSONDecodeError, OSError):
                mentett_adatok = []
        mentett_adatok.append(adatok)
        try:
            with open(fajlnev, mode='w', encoding='utf-8') as f:
                json.dump(mentett_adatok, f, ensure_ascii=False, indent=2)
            messagebox.showinfo('Mentés', 'Sikeres volt a Mentés')
        except OSError:
            messagebox.showerror('Hiba', 'Nem sikerült a Mentés')

if __name__ == "__main__":
    root = tk.Tk()
    app = KockaApp(root)
    root.mainloop()
