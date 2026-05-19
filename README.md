# IBZ Barber – Bookingsystem

## Filstruktur
```
ibz_barber/
├── app.py               ← Python/Flask backend
├── database.sql         ← MariaDB oppsett
├── README.md
└── templates/
    ├── index.html       ← Forside + bookingskjema
    ├── bekreftelse.html ← Bekreftelses-side
    └── admin.html       ← Adminpanel
```

---

## Oppsett (steg for steg)

### 1. Installer det du trenger
```bash
pip install flask mysql-connector-python
```

### 2. Sett opp databasen i MariaDB
```bash
mysql -u root -p
```
Deretter lim inn innholdet fra `database.sql`, eller kjør:
```bash
mysql -u root -p < database.sql
```

### 3. Endre databasepassord i app.py
Åpne `app.py` og bytt ut:
```python
password="passord"   # ← Bytt til ditt eget passord
```

### 4. Start serveren
```bash
python app.py
```

### 5. Åpne i nettleser
- **Forside:** http://localhost:5000
- **Admin:**   http://localhost:5000/admin

---

## Funksjonalitet
| Side | URL | Beskrivelse |
|---|---|---|
| Forside | `/` | Viser tjenester og bookingskjema |
| Booking | `/book` | Lagrer bestilling i databasen |
| Bekreftelse | `/bekreftelse` | Viser bekreftelse til kunden |
| Admin | `/admin` | Oversikt over alle bestillinger |
| Slett | `/slett/<id>` | Sletter en bestilling |

---

## Teknologier brukt
- **Python + Flask** – Web-server og ruting
- **MariaDB** – Database for lagring av bestillinger
- **HTML + CSS** – Brukergrensesnitt (ingen ekstra rammeverk)
- **Jinja2** – Mal-system for dynamisk HTML (følger med Flask)