import csv
import psycopg2
import argparse
import sys 

def create_table_from_csv(dbname, csvfilepath, csvfilename, user='troyperment', password='', host='localhost', port='5432'):
    # Connect to the PostgreSQL server
    conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host, port=port)
    cur = conn.cursor()
    fullfilepath = csvfilepath + csvfilename +'.csv'
    
    def infer_datatype(value):
        try:
            int(value)
            return 'INTEGER'
        except ValueError:
            pass

        try:
            float(value)
            return 'REAL'
        except ValueError:
            pass

        if value.lower() in ['true', 'false']:
            return 'BOOLEAN'
        
        return 'VARCHAR'

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
                column_type = infer_datatype(row[col])
                
                # If the type is not TEXT, and is more specific than the current type,
                # update the type for the column
                if col not in column_types or column_types[col] == 'VARCHAR(200)':
                    column_types[col] = column_type

    # Create the table in PostgreSQL using the inferred data types
    column_definitions = ", ".join([f"{col} {column_types[col]}" for col in columns])
    create_table_sql = f"CREATE TABLE {csvfilename} ({column_definitions});"   

    # Execute the create table query
    cur.execute(create_table_sql)
    conn.commit()


    # Insert the data from the CSV file into the table
    with open(fullfilepath, 'r', encoding='utf-8') as f:
        next(f)  # Skip the header row
        table_name = csvfilename
        cur.copy_from(f, table_name, sep=',', null='')  # Adjust the separator and null treatment if needed
    conn.commit()

    # Close the cursor and the connection
    cur.close()
    conn.close()
    return(dbname, csvfilename,fullfilepath, user, password, host, port)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Create a table in PostgreSQL from a CSV file.")
    parser.add_argument('dbname', help='Name of the PostgreSQL database')
    parser.add_argument('csvfilepath', help='Path to the CSV file')
    parser.add_argument('csvfilename', help='Name of the CSV file')
    #parser.add_argument('--user', default= 'troyperment', help='Username for the PostgreSQL database')
    #parser.add_argument('--password', default='', help='Password for the PostgreSQL database')
    #parser.add_argument('--host', default='localhost', help='Host of the PostgreSQL database')
    #parser.add_argument('--port', default='5432', help='Port of the PostgreSQL database')

    args = parser.parse_args()

    #results = create_table_from_csv(args.dbname, args.csvfilepath, args.csvfilename)    
    #sys.stdout.write(str(results))
    create_table_from_csv(args.dbname, args.csvfilepath, args.csvfilename)    


# Example usage:
# python3 create_table_from_csv.py ph1 /Users/troyperment/Development/awscloudsync-laptop/ Businesses
