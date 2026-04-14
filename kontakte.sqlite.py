import sqlite3

conn = sqlite3.connect("kontakte.sqlite")
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS Kontakte (name TEXT, email TEXT)
""")
conn.commit()

while True:
    print("""
    --- Kontakte ---
    1. Kontakt hinzufügen
    2. Alle anzeigen
    3. Beenden
    """)

    auswahl = input("Was möchtest du tun? ")

    if auswahl == "1":
        name = input("Name: ")
        email = input("Email: ")
        cur.execute("INSERT INTO Kontakte (name, email) VALUES (?,?)", (name, email))
        conn.commit()
        print(f"{name} wurde gespeichert!")

    elif auswahl == "2":
        print("\n--- Alle Kontakte ---")
        cur.execute("SELECT name, email FROM Kontakte")
        rows = cur.fetchall()
        for row in rows:
            print(f"Name: {row[0]}, Email: {row[1]}")

    elif auswahl == "3":
        break

    else:
        print("Ungültige Eingabe")

cur.close()
conn.close()



