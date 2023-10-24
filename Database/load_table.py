import psycopg2
import argparse

def load_table(dbname, table_name, csvfilepath, csvfilename, user, host, port, schema):
    # Connect to the PostgreSQL server
    conn = psycopg2.connect(dbname=dbname, user=user, password='', host=host, port=port)
    cur = conn.cursor()
    fullfilepath = csvfilepath + csvfilename +'.csv'
    
    # Insert the data from the CSV file into the table
    with open(fullfilepath, 'r', encoding='utf-8') as f:
        next(f)  # Skip the header row
        cur.execute(f'SET search_path TO {schema}')
        cur.copy_from(f, table_name, sep=',', null='')  # Adjust the separator and null treatment if needed
    conn.commit()

    # Close the cursor and the connection
    cur.close()
    conn.close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Load data into a PostgreSQL table from a CSV file.")
    parser.add_argument('dbname', help='Name of the PostgreSQL database')
    parser.add_argument('table_name', help='Name of the table to load the data into')
    parser.add_argument('csvfilepath', help='Path to the CSV file')
    parser.add_argument('csvfilename', help='Name of the CSV file')
    parser.add_argument('--user', default= 'troyperment', help='Username for the PostgreSQL database')
    parser.add_argument('--host', default='localhost', help='Host of the PostgreSQL database')
    parser.add_argument('--port', default='5432', help='Port of the PostgreSQL database')
    parser.add_argument('--schema', default='raw', help='Schema of the PostgreSQL database')
    args = parser.parse_args()
    print(f"Data loaded into {args.schema}.{args.table_name} successfully!")
