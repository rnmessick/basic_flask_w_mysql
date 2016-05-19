from flask import Flask, render_template

app = Flask(__name__)

@app.route('/', methods=["GET"])
def ice_cream_index():
    return render_template('icecream.html')

if __name__ == "__main__":
    app.run(debug=True)
