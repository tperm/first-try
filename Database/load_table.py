import csv
import psycopg2
import argparse
import sys 
from createtabledupe import createtabledupe

def load_table(dbname, fullfilepath, table_name, user='troyperment', host='localhost', port='5432', schema='raw'):
    # Connect to the PostgreSQL server
    conn = psycopg2.connect(dbname=dbname, user=user, password='', host=host, port=port)
    cur = conn.cursor()
    qualified_table_name = f"{schema}.{table_name}"
    
    # Insert the data from the CSV file into the table
    with open(fullfilepath, 'r', encoding='utf-8') as f:
        next(f)  # Skip the header row
        cur.copy_from(f, qualified_table_name, sep=',', null='')  # Adjust the separator and null treatment if needed
    conn.commit()

    # Close the cursor and the connection
    cur.close()
    conn.close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Load data into a PostgreSQL table from a CSV file.")
    parser.add_argument('dbname', help='Name of the PostgreSQL database')
    parser.add_argument('fullfilepath', help='Path to the CSV file')
    parser.add_argument('table_name', help='Name of the table to create')
    parser.add_argument('--user', default= 'troyperment', help='Username for the PostgreSQL database')
    parser.add_argument('--host', default='localhost', help='Host of the PostgreSQL database')
    parser.add_argument('--port', default='5432', help='Port of the PostgreSQL database')
    parser.add_argument('--schema', default='raw', help='Schema of the PostgreSQL database')

    args = parser.parse_args()
    results = createtabledupe(args.dbname, args.fullfilepath, args.table_name, args.user, args.host, args.port, args.schema)
    load_table(results[0], results[1], results[2], results[3], results[4], results[5], args.schema)
    print(f"Data loaded into {args.schema}.{args.table_name} successfully!")
