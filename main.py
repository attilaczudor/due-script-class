import kocka_app
import tkinter as tk
from tkinter import ttk, messagebox
import requests

def backend_uzenet():
    try:
        valasz = requests.get('http://127.0.0.1:5000/api/uzenet', timeout=2)
        adat = valasz.json()
        backend_cimke.config(text=f"Backend: {adat.get('uzenet', '')}")
    except requests.exceptions.RequestException:
        messagebox.showerror('Hiba', 'A backend szerver nem elérhető! Indítsa el a backend.py-t.')

root = tk.Tk()
app = kocka_app.KockaApp(root)

backend_cimke = ttk.Label(root, text='Üzenet: -')
backend_cimke.grid(column=2, row=5, padx=5, pady=5)

backend_gomb = ttk.Button(root, text='Üzenet', command=backend_uzenet)
backend_gomb.grid(column=3, row=5, padx=5, pady=5)

if __name__ == "__main__":
    root.mainloop()
