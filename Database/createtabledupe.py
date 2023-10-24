import csv
import psycopg2
import argparse
import sys 

def createtabledupe(dbname, csvfilepath, csvfilename, user, host, port, schema='raw'):
    # Connect to the PostgreSQL server
    conn = psycopg2.connect(dbname=dbname, user=user, password='', host=host, port=port)
    cur = conn.cursor()
    fullfilepath = csvfilepath + csvfilename +'.csv'
    table_name = csvfilename
    qualified_table_name = f"{schema}.{csvfilename}"

    # Read the CSV file to get the headers (column names) and sample data for type inference
    column_types = {}
    with open(fullfilepath, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        #reader = csv.DictReader(f,delimiter='|')
        columns = reader.fieldnames

        # We'll check the first 5 rows to infer the data type.
        # Adjust this number as needed.
        for _ in range(5):
            row = next(reader)
            for col in columns:
                column_type = 'VARCHAR'
                
                # If the type is not TEXT, and is more specific than the current type,
                # update the type for the column
                if col not in column_types or column_types[col] == 'VARCHAR':
                    column_types[col] = column_type

    # Create the table in PostgreSQL using the inferred data types
    column_definitions = ', '.join([f'{col} {column_types[col]}' for col in columns])
    qualified_table_name = f"{schema}.{csvfilename}"
    create_table_sql = f"CREATE TABLE {qualified_table_name} ({column_definitions});"   

    # Execute the create table query
    cur.execute(create_table_sql)
    conn.commit()

    # Close the cursor and the connection
    cur.close()
    conn.close()
    return(dbname, fullfilepath, table_name, user, host, port, schema)



if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Create a table in PostgreSQL from a CSV file.")
    parser.add_argument('dbname', help='Name of the PostgreSQL database')
    parser.add_argument('csvfilepath', help='Path to the CSV file')
    parser.add_argument('csvfilename', help='Name of the CSV file')
    parser.add_argument('--user', default='troyperment', help='Username for the PostgreSQL database')
    parser.add_argument('--host', default='localhost', help='Host of the PostgreSQL database')
    parser.add_argument('--port', default='5432', help='Port of the PostgreSQL database')
    parser.add_argument('--schema', default='raw', help='Schema of the PostgreSQL database')

    args = parser.parse_args()
    #createtabledupe(args.dbname, args.csvfilepath, args.csvfilename, args.user, args.host, args.port)
    results = createtabledupe(args.dbname, args.csvfilepath, args.csvfilename, args.user, args.host, args.port, args.schema)
    
    # Print or use the returned values
    print(f"dbname: {results[0]}")
    print(f"fullfilepath: {results[1]}")
    print(f"table_name: {results[2]}")  
    print(f"user: {results[3]}")
    print(f"host: {results[4]}")
    print(f"port: {results[5]}")
    print(f"schema: {args.schema}")
# Example usage:
# python3 createtabledupe.py ph1 /Users/troyperment/Development/awscloudsync-laptop/ Businesses troyperment localhost 5432 raw