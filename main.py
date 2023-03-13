import sqlite3
import pandas as pd
import tkinter as tk

# Create the GUI
class App:
    def __init__(self, master):
        self.master = master
        master.title("Kundeinformasjon")

        # Add a label and entry box for the kunde_nr input
        self.label = tk.Label(master, text="Skriv inn kunde_nr:")
        self.label.pack()
        self.entry = tk.Entry(master)
        self.entry.pack()

        # Add a button to submit the kunde_nr and display the customer info
        self.submit_button = tk.Button(master, text="Hent kundeinfo", command=self.get_customer_info)
        self.submit_button.pack()

    def get_customer_info(self):
        # Get the user input from the entry box
        kunde_nr = self.entry.get()

        # Connect to the database
        conn = sqlite3.connect('TKdatabase.db')

        # Query the database for the customer info
        query = f"SELECT * FROM 'kunde-info' WHERE kunde_nr = {kunde_nr}"
        result = pd.read_sql_query(query, conn)

        # Display the customer info in a new window
        top = tk.Toplevel(self.master)
        top.title("Kundeinfo")
        text = tk.Text(top)
        text.pack()
        text.insert(tk.END, result.to_string(index=False))

        # Close the database connection
        conn.close()

def create_database():
    # Connect to the database
    conn = sqlite3.connect('TKdatabase.db')

    # Create the kunde-info table
    conn.execute('''CREATE TABLE kunde_info
                     (kunde_nr INTEGER PRIMARY KEY,
                      fnavn TEXT,
                      enavn TEXT,
                      adresse TEXT,
                      epost TEXT,
                      postnummer INTEGER)''')

    # Create the postnummer-info table
    conn.execute('''CREATE TABLE postnummer_info
                     (postnummer INTEGER PRIMARY KEY,
                      poststed TEXT)''')

    # Close the database connection
    conn.close()

def oppgave1():
    # Connect to the database
    conn = sqlite3.connect('TKdatabase.db')

    # Read in the randoms.csv file
    data = pd.read_csv('randoms.csv')

    # Add a kunde_nr column to the DataFrame with values ranging from 1 to the number of rows in the DataFrame
    data['kunde_nr'] = range(1, len(data) + 1)

    # Write the data to the kunde-info table
    data.to_sql('kunde-info', conn, if_exists='append', index=False)

    # Close the database connection
    conn.close()

def oppgave2():
    # Connect to the database
    conn = sqlite3.connect('TKdatabase.db')

    # Read in the Postnummerregister.csv file
    postnummer_data = pd.read_csv('Postnummerregister.csv')

    # Write the data to the postnummer-info table
    postnummer_data.to_sql('postnummer-info', conn, if_exists='append', index=False)

    # Close the database connection
    conn.close()

def main():
    # Create the database and add data to the tables
    create_database()
    oppgave1()
    oppgave2()

    # Create the GUI
    root = tk.Tk()
    app = App(root)
    root.mainloop()

if __name__ == "__main__":
    main()
