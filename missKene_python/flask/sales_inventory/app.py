from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to our Sales Inventory Management System"

@app.route('/categories')
def categories():
    return "Product Categories"

@app.route('/items')
def items():
    return "Inventory Items"

@app.route('/orders')
def orders():
    return "Customer Orderes"

if __name__ == '__main__':
    app.run(debug=True)