from app import app
from models.order_list import *
from models.order import *
from flask import render_template

@app.route('/orders')
def index():
    return render_template('index.html', title='Orders', orders=orders)

@app.route('/orders/<order_id>')
def order(order_id):
    order_num = int(order_id)
    for order in orders:
        if order.order_no == order_num:
            index = orders.index(order)
    return render_template('order.html', title="Order No: ", order_id=order_id, order=orders[index])
