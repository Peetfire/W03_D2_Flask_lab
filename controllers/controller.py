from app import app
from models.order_list import orders

@app.route('/view-orders')
def index():
    return "Hello, World!"