import sqlite3
import pandas as pd

def oppgave1():
    # Åpne en databaseforbindelse
    conn = sqlite3.connect('min_database.db')

    # Les inn CSV-filen
    data = pd.read_csv('randoms.csv')

    # Skriv dataene til databasen i tabellen "kunde-info"
    data.to_sql('kunde-info', conn, if_exists='append', index=False)

    # Lukk databaseforbindelsen
    conn.close()


def oppgave2():
    # Åpne en databaseforbindelse
    conn = sqlite3.connect('min_database.db')

    # Les inn CSV-filen
    postnummer_data = pd.read_csv('Postnummerregister.csv')

    # Skriv dataene til databasen i tabellen "postnummer-info"
    postnummer_data.to_sql('postnummer-info', conn, if_exists='append', index=False)

    # Lukk databaseforbindelsen
    conn.close()

def main():
    # Kjør oppgave1 og oppgave2
    oppgave1()
    oppgave2()

if __name__ == '__main__':
    main()
