import csv
import psycopg2

DATABASE_URI = 'postgresql://troyperment@localhost:5432/ph1' 


def insert_records_from_csv(csv_file_path):
    # Connect to the PostgreSQL database
    conn = psycopg2.connect(DATABASE_URI)
    cursor = conn.cursor()
    
    with open(csv_file_path, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        
        for row in reader:
            # Insert each row into the "rawbrokers" table
            cursor.execute(
                """
                INSERT INTO rawbrokers (contacted, lastfollowupdate, firstname, lastname, phonenumber, emailaddress, 
                                     address1, address2, city, state, zip, companyname, notes)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
                """, 
                (row['contacted'], row['lastfollowupdate'], row['firstname'], row['lastname'], 
                 row['phonenumber'], row['emailaddress'], row['address1'], row['address2'], 
                 row['city'], row['state'], row['zip'], row['companyname'], row['notes'])
            )
        
        conn.commit()

    # Close the cursor and connection
    cursor.close()
    conn.close()


if __name__ == '__main__':
    insert_records_from_csv('/Users/troyperment/Development/DataFiles/input/brokers.csv')


