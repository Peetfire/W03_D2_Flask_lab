from app import app
from models.order_list import orders
from flask import render_template

@app.route('/orders')
def index():
    return render_template('index.html', title='Orders', orders=orders)