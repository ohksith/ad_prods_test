from flask import Flask, render_template, redirect, url_for
import requests

app = Flask(__name__, template_folder="templates", static_folder="static")

current_product_id = 1

def fetch_product_data(product_id):
    url = f"https://dummyjson.com/products/{product_id}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching product data: {e}")
        return {"error": str(e)}


@app.route("/")
def home():
    global current_product_id
    product = fetch_product_data(current_product_id)
    return render_template("index.html", product=product)

@app.route("/next")
def next_product():
    global current_product_id
    current_product_id += 1
    if current_product_id > 30:
        current_product_id = 1 
    return redirect(url_for('home'))

if __name__ == "__main__":
    app.run(debug=True)
