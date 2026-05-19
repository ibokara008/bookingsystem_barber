from flask import Flask, render_template, request, redirect, url_for
import mysql.connector
from datetime import datetime

app = Flask(__name__)

# --- Databasetilkobling ---
def get_db():
    return mysql.connector.connect(
        host="localhost",
        user="ibrahim",          # Bytt til ditt brukernavn
        password="greenhouse",   # Bytt til ditt passord
        database="ibz_barber"
    )

# --- Forside med bookingskjema ---
@app.route("/")
def index():
    return render_template("index.html")

# --- Behandle booking ---
@app.route("/book", methods=["POST"])
def book():
    navn = request.form["navn"]
    telefon = request.form["telefon"]
    tjeneste = request.form["tjeneste"]
    dato = request.form["dato"]
    tid = request.form["tid"]

    db = get_db()
    cursor = db.cursor()
    sql = "INSERT INTO bestillinger (navn, telefon, tjeneste, dato, tid) VALUES (%s, %s, %s, %s, %s)"
    cursor.execute(sql, (navn, telefon, tjeneste, dato, tid))
    db.commit()
    cursor.close()
    db.close()

    return redirect(url_for("bekreftelse", navn=navn, tjeneste=tjeneste, dato=dato, tid=tid))

# --- Bekreftelsesside ---
@app.route("/bekreftelse")
def bekreftelse():
    navn = request.args.get("navn")
    tjeneste = request.args.get("tjeneste")
    dato = request.args.get("dato")
    tid = request.args.get("tid")
    return render_template("bekreftelse.html", navn=navn, tjeneste=tjeneste, dato=dato, tid=tid)

# --- Admin: se alle bestillinger ---
@app.route("/admin")
def admin():
    db = get_db()
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM bestillinger ORDER BY dato, tid")
    bestillinger = cursor.fetchall()
    cursor.close()
    db.close()
    return render_template("admin.html", bestillinger=bestillinger)

# --- Slett bestilling ---
@app.route("/slett/<int:id>")
def slett(id):
    db = get_db()
    cursor = db.cursor()
    cursor.execute("DELETE FROM bestillinger WHERE id = %s", (id,))
    db.commit()
    cursor.close()
    db.close()
    return redirect(url_for("admin"))

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
