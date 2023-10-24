from create_table_csv import create_table_csv
from load_table import load_table   

dbname = 'ph1'
csvfilepath = '/Users/troyperment/Development/awscloudsync-laptop/'
csvfilename = 'businesses'
user = 'troyperment'
host = 'localhost'
port = '5432'
schema = 'raw'

qualified_table_name = create_table_csv(dbname, csvfilepath, csvfilename, user, host, port, schema)
print(qualified_table_name)

load_table(dbname, qualified_table_name, csvfilepath, csvfilename, user, host, port, schema=schema)