import json
import csv
import sqlite3
from flask import Flask, request, render_template

app = Flask(__name__)

def read_json(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

def read_csv(file_path):
    products = []
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            row['id'] = int(row['id'])
            row['price'] = float(row['price'])
            products.append(row)
    return products

def read_sqlite(db_path):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, category, price FROM Products")
    rows = cursor.fetchall()
    products = []
    for row in rows:
        product = {
            'id': row[0],
            'name': row[1],
            'category': row[2],
            'price': row[3]
        }
        products.append(product)
    conn.close()
    return products

@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id', type=int)
    data = []

    if source == 'json':
        data = read_json('products.json')
    elif source == 'csv':
        data = read_csv('products.csv')
    elif source == 'sql':
        data = read_sqlite('products.db')
    else:
        return render_template('product_display.html', error="Wrong source")

    if product_id is not None:
        data = [product for product in data if product['id'] == product_id]
        if not data:
            return render_template('product_display.html', error="Product not found")
    
    return render_template('product_display.html', products=data)

if __name__ == '__main__':
    app.run(debug=True, port=5000)