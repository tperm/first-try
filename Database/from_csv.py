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
csvfilepath = '/Users/troyperment/Development/awscloudsync-laptop/' 
csvfilename = 'Businesses' 
# Read the CSV file to get the headers (column names)
with open(csvfilepath + csvfilename +'.csv', 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    columns = next(reader)  # Get the header

# Create the table in PostgreSQL. For simplicity, assuming all columns are TEXT type.
# In a real-world scenario, you might want to detect or define data types accordingly.
column_definitions = ", ".join([f"{col} VARCHAR(200)" for col in columns])
create_table_sql = f"CREATE TABLE {csvfilename} ({column_definitions});"

# Execute the create table query
cur.execute(create_table_sql)
conn.commit()

# Close the cursor and the connection
cur.close()
conn.close()
