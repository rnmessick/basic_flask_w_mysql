from flask import Flask, render_template
from DBConnection import MySQLConnector

app = Flask(__name__)

# Create DB connection
mysql = MySQLConnector(app, 'ice_cream_db')



@app.route('/', methods=["GET"])
def ice_cream_index():
    ice_creams = mysql.query_db("SELECT name FROM ice_creams")

    return render_template('icecream.html', icecreams = ice_creams)

if __name__ == "__main__":
    app.run(debug=True)
