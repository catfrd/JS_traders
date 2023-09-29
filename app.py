from flask import Flask, g,render_template, request, redirect, session, url_for
from dotenv import load_dotenv
import os



app = Flask(__name__)
app.secret_key = "your_secret_key"

load_dotenv()

PORT = os.environ.get('PORT')


@app.route("/", methods=['GET','POST'])
def home():
    return render_template('index.html')

@app.route("/products", methods=['GET','POST'])
def events():
    return render_template('products.html')


@app.route("/contact", methods=['GET','POST'])
def contact():
    return render_template('contact.html')



if __name__ == '__main__':

    app.run(debug=True, host='0.0.0.0', port=PORT)


