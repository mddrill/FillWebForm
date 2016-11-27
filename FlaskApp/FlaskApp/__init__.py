from flask import Flask, render_template, request, redirect, url_for
from forms import TestForm
import sqlite3

app = Flask(__name__)
app.secret_key = "fdsafdsafdsa"

@app.route('/')
def homepage():
	return render_template("main.html", form=TestForm())
	
@app.route('/post', methods=['POST'])
def post():
	conn = sqlite3.connect("sample.db")
	cur = conn.cursor()
        test_form=request.form['test_form']
	cur.execute("CREATE TABLE if not exists test_table(test_column)")
	cur.execute("INSERT INTO test_table VALUES('{0}')".format(test_form))
	conn.commit()
	conn.close()
	return redirect(url_for('homepage'))

if __name__ == "__main__":
	app.run(debug=True)
