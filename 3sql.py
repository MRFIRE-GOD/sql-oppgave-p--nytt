import sqlite3
import pandas as pd

def create_database():
    # Åpne en tilkobling til databasen
    conn = sqlite3.connect('database.db')

    # Opprett en tabell "kunde_info" med kolonner for kunde_nr, fnavn, enavn, adresse, epost og postnummer
    conn.execute('''CREATE TABLE kunde_info
                     (kunde_nr INTEGER PRIMARY KEY,
                      fnavn TEXT,
                      enavn TEXT,
                      adresse TEXT,
                      epost TEXT,
                      postnummer INTEGER)''')

    # Opprett en tabell "postnummer_info" med kolonner for postnummer og poststed
    conn.execute('''CREATE TABLE postnummer_info
                     (postnummer INTEGER PRIMARY KEY,
                      poststed TEXT)''')

    # Lukk tilkoblingen til databasen
    conn.close()

def oppgave1():
    # Åpne en tilkobling til databasen
    conn = sqlite3.connect('database.db')

    # Les inn "randoms.csv"-filen
    data = pd.read_csv('randoms.csv')

    # Legg til en "kunde_nr"-kolonne til DataFrame med verdier som spenner fra 1 til antall rader i DataFrame
    data['kunde_nr'] = range(1, len(data) + 1)

    # Skriv dataen til "kunde-info"-tabellen
    data.to_sql('kunde-info', conn, if_exists='append', index=False)

    # Lukk tilkoblingen til databasen
    conn.close()

def oppgave2():
    # Åpne en tilkobling til databasen
    conn = sqlite3.connect('database.db')

    # Les inn "Postnummerregister.csv"-filen
    postnummer_data = pd.read_csv('Postnummerregister.csv')

    # Skriv dataen til "postnummer-info"-tabellen
    postnummer_data.to_sql('postnummer-info', conn, if_exists='append', index=False)

    # Lukk tilkoblingen til databasen
    conn.close()

def get_customer_info():
    # Åpne en tilkobling til databasen
    conn = sqlite3.connect('database.db')

    # Hent inn bruker-inputted kunde_nr
    kunde_nr = input("Skriv inn kunde_nr: ")

    # Hent ut raden fra "kunde-info"-tabellen som matcher kunde_nr
    query = f"SELECT * FROM 'kunde-info' WHERE kunde_nr = {kunde_nr}"
    result = pd.read_sql_query(query, conn)

    # Skriv ut resultatet
    print(result)

    # Lukk tilkoblingen til databasen
    conn.close()

def main():
    # Opprett databasen og legg til data i tabellene
    create_database()
    oppgave1()
    oppgave2()

    # Hent kundeinfo fra brukeren
    get_customer_info()

if __name__ == "__main__":
    main()
