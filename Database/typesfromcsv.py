import csv
import psycopg2

# Define the connection parameters
conn_params = {
    'dbname': 'ph1',
    'user': 'troyperment',
    'password': '',
    'host': 'localhost',
    'port': '5432'
}

# Connect to the PostgreSQL server
conn = psycopg2.connect(**conn_params)
cur = conn.cursor()

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
    
    return 'TEXT'

# Read the CSV file to get the headers (column names) and sample data for type inference
column_types = {}
csvfilepath = '/Users/troyperment/Development/awscloudsync-laptop/' 
csvfilename = 'Businesses' 
with open(csvfilepath + csvfilename +'.csv', 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    columns = reader.fieldnames

    # We'll check the first 5 rows to infer the data type.
    # Adjust this number as needed.
    for _ in range(5):
        row = next(reader)
        for col in columns:
            column_type = infer_datatype(row[col])
            
            # If the type is not TEXT, and is more specific than the current type,
            # update the type for the column
            if col not in column_types or column_types[col] == 'TEXT':
                column_types[col] = column_type

# Create the table in PostgreSQL using the inferred data types
column_definitions = ", ".join([f"{col} {column_types[col]}" for col in columns])
create_table_sql = f"CREATE TABLE {csvfilename} ({column_definitions});"

# Execute the create table query
cur.execute(create_table_sql)
conn.commit()

# Close the cursor and the connection
cur.close()
conn.close()
