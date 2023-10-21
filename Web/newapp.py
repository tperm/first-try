from flask import Flask, render_template, request, redirect, url_for, flash
import psycopg2

app = Flask(__name__)
app.secret_key = 'some_secret_key'

DATABASE_URI = 'postgresql://troyperment@localhost:5432/ph1'

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Fetch data from form
        data = {
            'contacted': request.form.get('contacted', 'false') == 'true',
            'lastfollowupdate': request.form['lastfollowupdate'],
            'firstname': request.form['firstname'],
            'lastname': request.form['lastname'],
            'phonenumber': request.form['phonenumber'],
            'emailaddress': request.form['emailaddress'],
            'address1': request.form['address1'],
            'address2': request.form['address2'],
            'city': request.form['city'],
            'state': request.form['state'],
            'zip': request.form['zip'],
            'companyname': request.form['companyname'],
            'notes': request.form['notes']
        }
        
        # Insert data into the database
        conn = psycopg2.connect(DATABASE_URI)
        cursor = conn.cursor()

        cursor.execute(
            """
            INSERT INTO rawbrokers (contacted, lastfollowupdate, firstname, lastname, phonenumber, emailaddress, 
                                 address1, address2, city, state, zip, companyname, notes)
            VALUES (%(contacted)s, %(lastfollowupdate)s, %(firstname)s, %(lastname)s, %(phonenumber)s, 
                    %(emailaddress)s, %(address1)s, %(address2)s, %(city)s, %(state)s, %(zip)s, 
                    %(companyname)s, %(notes)s);
            """, data
        )
        
        conn.commit()
        cursor.close()
        conn.close()

        flash('Data successfully stored!', 'success')
        return redirect(url_for('index'))

    return render_template('form.html')



if __name__ == "__main__":
    app.run(debug=True)
