import kocka_class
import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
import csv
import json
import os
import random
import sqlite3

class KockaApp(kocka_class.Kockadobas):
    def __init__(self, root):
        super().__init__(root)
        self.mentes_gomb = ttk.Button(root, text='Mentés - TEXT', command=self.mentes)
        self.mentes_gomb.grid(column=0, row=3, padx=5, pady=5)

        self.mentes_csv_gomb = ttk.Button(root, text='Mentés - CSV', command=self.mentes_csv)
        self.mentes_csv_gomb.grid(column=1, row=3, padx=5, pady=5)

        self.mentes_json_gomb = ttk.Button(root, text='Mentés - JSON', command=self.mentes_json)
        self.mentes_json_gomb.grid(column=2, row=3, padx=5, pady=5)

        self.mentes_sql_gomb = ttk.Button(root, text='Mentés - SQL', command=self.mentes_sql)
        self.mentes_sql_gomb.grid(column=0, row=4, padx=5, pady=5)

        self.osszesites_gomb = ttk.Button(root, text='Összesítés', command=self.osszesites_sql)
        self.osszesites_gomb.grid(column=1, row=4, padx=5, pady=5)

        self.veletlen_gomb = ttk.Button(root, text='Dobásszám', command=self.veletlen_dobasszam)
        self.veletlen_gomb.grid(column=1, row=1, padx=5, pady=5)

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

    def mentes_sql(self):
        if sum(self.eredmenyek.values()) == 0:
            messagebox.showwarning('Dobás', 'Először dobjon')
            return
        datum = datetime.now().strftime('%Y.%m.%d')
        try:
            with sqlite3.connect('mentes.db') as conn:
                cursor = conn.cursor()
                cursor.execute("""
                    CREATE TABLE IF NOT EXISTS dobasok (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        datum TEXT,
                        egy INTEGER,
                        ketto INTEGER,
                        harom INTEGER,
                        negy INTEGER,
                        ot INTEGER,
                        hat INTEGER
                    )
                """)
                cursor.execute("""
                    INSERT INTO dobasok (datum, egy, ketto, harom, negy, ot, hat)
                    VALUES (?, ?, ?, ?, ?, ?, ?)
                """, (datum, *self.eredmenyek.values()))
                conn.commit()
            messagebox.showinfo('Mentés', 'Sikeres volt a Mentés')
        except sqlite3.Error as e:
            messagebox.showerror('Hiba', f'Nem sikerült a Mentés: {e}')

    def osszesites_sql(self):
        try:
            with sqlite3.connect('mentes.db') as conn:
                cursor = conn.cursor()
                cursor.execute("""
                    CREATE TABLE IF NOT EXISTS dobasok (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        datum TEXT,
                        egy INTEGER,
                        ketto INTEGER,
                        harom INTEGER,
                        negy INTEGER,
                        ot INTEGER,
                        hat INTEGER
                    )
                """)
                cursor.execute("SELECT sum(egy), sum(ketto), sum(harom), sum(negy), sum(ot), sum(hat) FROM dobasok")
                eredmeny = cursor.fetchone()
                if eredmeny and eredmeny[0] is not None:
                    szoveg = 'Összesítés (SQL):\n' + '\n'.join(f'{i}. = {eredmeny[i-1]}' for i in range(1, 7))
                    self.dobas_eredmenye.config(text=szoveg)
                else:
                    messagebox.showinfo('Összesítés', 'Még nincs adat az adatbázisban!')
        except sqlite3.Error as e:
            messagebox.showerror('Hiba', f'Nem sikerült a lekérdezés: {e}')

if __name__ == "__main__":
    root = tk.Tk()
    app = KockaApp(root)
    root.mainloop()
