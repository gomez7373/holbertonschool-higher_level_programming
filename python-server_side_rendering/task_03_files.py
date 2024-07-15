import json
import csv
import sqlite3
from flask import Flask, request, render_template

app = Flask(__name__)

def read_json():
    with open('products.json') as file:
        return json.load(file)

def read_csv():
    products = []
    with open('products.csv') as file:
        reader = csv.DictReader(file)
        for row in reader:
            products.append(row)
    return products

def read_sql():
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Products')
    products = cursor.fetchall()
    conn.close()
    return [{'id': row[0], 'name': row[1], 'category': row[2], 'price': row[3]} for row in products]

@app.route('/products')
def products():
    source = request.args.get('source')
    if source == 'json':
        products = read_json()
    elif source == 'csv':
        products = read_csv()
    elif source == 'sql':
        products = read_sql()
    else:
        return render_template('product_display.html', error="Wrong source")

    product_id = request.args.get('id')
    if product_id:
        products = [p for p in products if str(p['id']) == product_id]
        if not products:
            return render_template('product_display.html', error="Product not found")

    return render_template('product_display.html', products=products)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
