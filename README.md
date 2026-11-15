# DUE Szkript Nyelvek - Kockajáték Szimuláció és Perzisztencia

## Hallgató adatai
- **Név**: Czudor Attila
- **Tantárgy**: Szkript nyelvek (Dunaújvárosi Egyetem)
- **Oktató**: Adamcsik János Béla
- **GitHub**: [due-script-class](https://github.com/attilaczudor/due-script-class)

---

## 1. Az Alkalmazás Leírása

Ez a projekt egy Python nyelven írt, grafikus felhasználói felülettel (Tkinter) rendelkező kockadobás-szimulációs, perzisztencia- és kliens-szerver alkalmazás.

A rendszer főbb funkciói:
- **Kockadobás szimulációja**: Tetszőleges számú dobás szimulálása véletlenszám-generálással, szigorú bemeneti validációval (csak számok, 1 és 10000 közötti értékek).
- **Statisztikai kiértékelés**: A hat kockaoldal dobási gyakoriságának azonnali megjelenítése a grafikus felületen.
- **Négyféle adatperzisztencia**:
  - **Sima szöveges fájl (`mentes.txt`)**: Szótár formátumú sorok hozzáfűzése.
  - **CSV táblázat (`mentes.csv`)**: Oszlopfejlécekkel és aktuális dátummal ellátott táblázatos mentés.
  - **JSON dokumentum (`mentes.json`)**: Időbélyeggel kiegészített, strukturált JSON tömb tárolása.
  - **SQLite relációs adatbázis (`mentes.db`)**: `dobasok` tábla automatikus létrehozása és rekordok rögzítése.
- **Adatbázis-összesítés**: Az SQLite adatbázisban tárolt összes korábbi dobási rekord összegzése SQL aggregációval (`SELECT sum(...)`).
- **REST API kapcsolat**: Kliens-szerver kommunikáció egy háttérben futó Flask mikroszolgáltatással HTTP GET kérésen keresztül.

---

## 2. Rendszerkövetelmények és Telepítés

### Rendszerkövetelmények:
- **Python**: 3.9 vagy újabb (ajánlott: Python 3.12+) Tkinter támogatással.
- **Operációs rendszer**: macOS, Windows vagy Linux.

### Függőségek telepítése:
A szükséges külső csomagokat a mellékelt `requirements.txt` fájl tartalmazza (`Flask`, `requests`).

Nyiss egy terminált a projekt gyökérmappájában, és add ki a következő parancsot:
```bash
pip3 install -r requirements.txt
```

---

## 3. A Program Használata és Futtatása

Az alkalmazás kliens-szerver architektúrát használ, így a teljes funkcionalitás eléréséhez a backend szervert és a grafikus felületet két külön terminálablakban indítjuk.

### 1. Lépés: A Flask Backend szerver indítása
Nyiss egy terminálablakot a projekt gyökérmappájában, és indítsd el a backend szervert:
```bash
python3 backend.py
```
A szerver elindul a háttérben a `http://127.0.0.1:5000` címen, és elérhetővé teszi a `/api/uzenet` REST végpontot.

### 2. Lépés: A Grafikus Felület (Főalkalmazás) indítása
Egy második terminálablakban indítsd el a főprogramot:
```bash
python3 main.py
```

---

## 4. Kezelőfelület és Funkciók

A megjelenő grafikus ablakban az alábbi műveletek végezhetők el:

| Gomb / Mező | Működés és Teendő |
| :--- | :--- |
| **Dobásszám beviteli mező** | Írd be a kívánt dobások számát (alapértelmezett: `10`, engedélyezett: `1 - 10000`). |
| **Dobás** | Elvégzi a megadott számú kockadobást, és kiírja az egyes oldalak (1-estől 6-osig) darabszámait. Érvénytelen bemenet esetén hibaablakot jelenít meg. |
| **Dobásszám** | Véletlenszerű dobásszámot generál (10 és 500 között), beírja a mezőbe, és automatikusan elvégzi a dobást. |
| **Mentés - TEXT** | Az aktuális dobás eredményét hozzáfűzi a `mentes.txt` fájlhoz. |
| **Mentés - CSV** | Az aktuális eredményt dátummal kiegészítve elmenti a `mentes.csv` fájlba (automatikusan létrehozza a fejlécet, ha még nincs). |
| **Mentés - JSON** | Az eredményt időbélyeggel ellátva hozzáadja a `mentes.json` tömbhöz. |
| **Mentés - SQL** | Rögzíti az eredményt a `mentes.db` SQLite adatbázis `dobasok` táblájába. |
| **Összesítés** | Lekéri az adatbázisban tárolt összes korábbi dobás összegét, és megjeleníti az összesített darabszámokat a képernyőn. |
| **Üzenet** | HTTP GET kérést küld a helyi Flask backendhez (`http://127.0.0.1:5000/api/uzenet`), és kiírja a kapott üzenetet (`Backend: ok`). |
| **Kilépés** | Bezárja az alkalmazást. |

---

## 5. Fájlstruktúra és Modulok

- **`main.py`**: A teljes integrált alkalmazás belépési pontja (GUI + REST hívások).
- **`backend.py`**: A Flask REST API mikroszolgáltatás forráskódja.
- **`kocka_app.py`**: A perzisztenciát (TXT, CSV, JSON, SQLite) és összesítést megvalósító `KockaApp` osztály.
- **`kocka_class.py`**: Az ablakot, a rácsos elrendezést és a dobásszimulációt kezelő alaposztály (`Kockadobas`).
- **`kocka.py`**: Az egyszerű, önálló kockadobó szimulátor.
- **`requirements.txt`**: A külső függőségek specifikációja.
- **`.gitignore`**: A futás közben generált adatbázis- és adatfájlok (`mentes.*`), valamint gyorsítótárak kizárása.
