import pandas as pd
import sqlite3
import tkinter.messagebox as mb

connector = sqlite3.connect('library.db')
cursor = connector.cursor()

connector.execute(
'CREATE TABLE IF NOT EXISTS Library (BK_NAME TEXT, BK_ID TEXT PRIMARY KEY NOT NULL, AUTHOR_NAME TEXT, BK_STATUS TEXT, CARD_ID TEXT)'
)

def add_record(bk_name, bk_id, author_name, bk_status,card_id):
    global connector
    try:
            connector.execute(
                'INSERT INTO Library (BK_NAME, BK_ID, AUTHOR_NAME, BK_STATUS, CARD_ID) VALUES (?, ?, ?, ?, ?)',
                        (bk_name, bk_id, author_name, bk_status, card_id))
            connector.commit()
    except sqlite3.IntegrityError:
            pass

def import_csv_to_db():
    connector = sqlite3.connect('library.db')
    cursor = connector.cursor()
    file_name = "books.csv"
    try:
        df = pd.read_csv(file_name, index_col = 1)
        rows, columns = df.shape
        if df.index.has_duplicates == False:
            bk_name = list(df['BK_NAME'])
            bk_id = list(df.index)
            author_name = list(df['AUTHOR_NAME'])
            bk_status = list(df['BK_STATUS'])
            card_id = list(df['CARD_ID'])
            for i in range(0, rows, 1):
                add_record(bk_name[i], bk_id[i], author_name[i], bk_status[i],card_id[i])
            print('Successfully Added')
            mb.showinfo('Import Status', 'Successful\nPlease choose Edit->Show to display Records')
        else:
            print('Book ID must be unique')
            
    except Exception as e:
        print(e,'Error in Opening File Or in the Data')
        mb.showinfo('Import Status', 'Failed')

def export_to_csv():
    connector = sqlite3.connect('library.db')
    cursor = connector.cursor()
    curr = connector.execute("SELECT * FROM Library")
    data = curr.fetchall()

    try:
        file = open("exported_data.csv","w")
        for i in data:
            file.write(str(i)[1:-1])
            file.write("\n")
        print("Successfully Exported")
    except:
        print("Error Occured")
    file.close()
