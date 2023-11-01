import psycopg2

# Database connection parameters
db_params = {
    'dbname': 'ph1',
    'user': 'troyperment',
    'host': 'localhost',
    'port': '5432'
}

# Establish connection
conn = psycopg2.connect(**db_params)
cur = conn.cursor()

# Call the stored procedure
cur.callproc('prod.fn_load_sales')  # Add parameters as needed

# If the stored procedure returns results, fetch them
result = cur.fetchall()

# Close the cursor and the connection
cur.close()
conn.close()

# Print the result (if any)
print(result)
