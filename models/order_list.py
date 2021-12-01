from models.order import Order


order1 = Order("Jonny Cash", "12/11/21", 3, 349.99, "Black Suit", 1)
order2 = Order("Pat Cash", "11/11/21", 7, 69.99, "Tennis Racquet", 2)
order3 = Order("Willy Wonka", "29/12/21", 12, 5.99, "Insulin", 8)
order4 = Order("Bernard Mathews","18/11/21", 6, 69.99, "Turkey Drumsticks", 5)
order5 = Order("Albert Einstien", "30/11/21", 1, 9.99, "Comb", 19)
order6 = Order("Pat Cash", "01/12/21", 7, 69.99, "Tennis Racquet", 29)

orders = [order1, order2, order3, order4, order5, order6]
headings = ["Order No", "Date", "Customer", "Description", "Unit Price", "No", "Total Price"]