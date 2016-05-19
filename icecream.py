from flask import Flask, render_template
from DBConnection import MySQLConnector

app = Flask(__name__)

# Create DB connection
mysql = MySQLConnector(app, 'ice_cream_db')

@app.route('/', methods=["GET"])
def ice_cream_index():
    return render_template('icecream.html')

if __name__ == "__main__":
    app.run(debug=True)
