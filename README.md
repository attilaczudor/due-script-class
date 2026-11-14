# DUE Szkript Nyelvek - Kockajáték Szimuláció és Perzisztencia

## Hallgató adatai
- **Név**: Czudor Attila
- **Tantárgy**: Szkript nyelvek (Dunaújvárosi Egyetem)
- **Oktató**: Adamcsik János Béla

---

## 1. Feladat leírása

A projekt egy grafikus felhasználói felülettel (Tkinter) rendelkező kockadobás-szimulációs és statisztikai alkalmazás. A program tetszőleges számú kockadobást képes szimulálni, ellenőrzi a felhasználói bevitelt, és a kapott statisztikai eredményeket több különböző formátumban perzisztálja, valamint relációs adatbázisban tárolja és aggregálja. A rendszer kliens-szerver architektúrát is megvalósít egy Flask alapú REST API mikro-szolgáltatáson keresztül.

---

## 2. Rendszerarchitektúra és Modulok

### Főbb forrásfájlok:
1. **`kocka.py`**: A kezdeti szimulációs logika és grafikus felület procedurális megvalósítása.
2. **`kocka_class.py`**: A felületet és dobásszimulációt tartalmazó alaposztály (`Kockadobas`).
3. **`kocka_app.py`**: A `Kockadobas` osztályból származtatott kibővített alkalmazás (`KockaApp`), amely megvalósítja a TXT, CSV, JSON és SQLite3 perzisztenciát, valamint a statisztikai aggregációt.
4. **`backend.py`**: Flask webszerver, amely a `/api/uzenet` REST végponton keresztül szolgáltat JSON adatokat.
5. **`main.py`**: A teljes rendszer fő indítóállománya, amely elindítja a grafikus felületet és kapcsolatot létesít a Flask háttérszolgáltatással.

---

## 3. Használt modulok és függvények

- **`tkinter` / `tkinter.ttk`**:
  - `Tk()` – Alapablak létrehozása (`root`)
  - `Label()`, `Button()`, `Entry()` – Grafikus vezérlőelemek
  - `StringVar()` – Reaktív adatkapcsolat a beviteli mezőhöz
  - `grid()`, `config()`, `destroy()`, `mainloop()` – Geometria- és állapotkezelés
- **`tkinter.messagebox`**:
  - `showinfo()`, `showwarning()`, `showerror()` – Felhasználói tájékoztató és hibakezelő párbeszédablakok
- **`random`**:
  - `randint()` – Véletlenszerű dobások és dobásszámok generálása
- **`datetime`**:
  - `datetime.now()`, `strftime()` – Időbélyegzés a mentési rekordokhoz
- **`os`**:
  - `os.path.exists()`, `os.path.getsize()` – Fájllétezés és fejlécellenőrzés
- **`csv`**:
  - `csv.writer()`, `writerow()` – CSV rekordok és fejlécek mentése
- **`json`**:
  - `json.load()`, `json.dump()` – JSON adatszerkezetek deszerializálása és perzisztálása
- **`sqlite3`**:
  - `connect()`, `cursor()`, `execute()`, `fetchone()`, `commit()` – Relációs adatbázis műveletek (DDL, DML, aggregáció)
- **`flask`**:
  - `Flask()`, `jsonify()`, `app.run()` – REST API végpontok kiszolgálása
- **`requests`**:
  - `requests.get()` – HTTP kérések indítása a backend szerver felé

---

## 4. Osztályok

1. **`Kockadobas`** (`kocka_class.py`):
   - Felelősség: Alapablak inicializálása, felületi elemek elhelyezése rácsos elrendezéssel (`grid`), bemeneti validáció (`1 <= db <= 10000`), dobások elvégzése és az eredmények felületi megjelenítése.
2. **`KockaApp`** (`kocka_app.py`):
   - Felelősség: A `Kockadobas` osztály kiterjesztése. Mentési funkciók megvalósítása (sima szöveges fájl `mentes.txt`, vesszővel tagolt `mentes.csv`, strukturált `mentes.json`, relációs `mentes.db` tábla), valamint véletlen dobásszám-sorsoló (`veletlen_dobasszam`) és SQLite összesítő (`osszesites_sql`).

---

## 5. Telepítés és Futtatás

### Függőségek telepítése:
```bash
pip install -r requirements.txt
```

### 1. Lépés: Backend szerver indítása (opcionális terminálablakban)
```bash
python backend.py
```
A szerver a `http://127.0.0.1:5000` címen hallgat.

### 2. Lépés: Alkalmazás indítása
```bash
python main.py
```

---

## 6. Órai Leiratok (Transcripts)

A repository tartalmazza az órák teljes, időbélyeges átiratait:
- `transcript_20261012_gyakorlat.txt` (Gyakorlat – Kocka alapok)
- `transcript_20261019_eloadas.txt` (Előadás – OOP refaktorálás és TXT mentés)
- `transcript_20261026_eloadas.txt` (Előadás – CSV, JSON és SQLite3 alapok)
- `transcript_20261102_eloadas.txt` (Előadás – SQLite összesítés és Flask kliens-szerver)
