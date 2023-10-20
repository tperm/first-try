from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        return f"Name: {name}, Age: {age}"
    return render_template('form.html')

if __name__ == '__main__':
    app.run(host="localhost", port=8000, debug=True)
