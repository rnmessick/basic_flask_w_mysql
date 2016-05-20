from flask import Flask, render_template, request, redirect
from DBConnection import MySQLConnector

app = Flask(__name__)

# Create DB connection
mysql = MySQLConnector(app, 'ice_cream_db')



@app.route('/', methods=["GET"])
def ice_cream_index():
    query = "SELECT name FROM ice_creams"
    data = {}
    ice_creams = mysql.query_db(query, data)
    return render_template('icecream.html', icecreams = ice_creams)

@app.route('/icecreams', methods=["POST"])
def create_ice_creams():
    query = "INSERT INTO ice_creams (name, created_at, updated_at) VALUES ( :name, NOW(), NOW())"
    data = {
        "name" : request.form['name']
    }
    mysql.query_db(query, data)

    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)
