import sqlite3
import pandas as pd


# Åpne en database
conn = sqlite3.connect('sq1.db')

# Les CSV filen 
data = pd.read_csv('randoms.csv')

# til databasen
data.to_sql('kunde-info', conn, if_exists='append', index=False)

# Lukk 
conn.close()

