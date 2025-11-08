# Dictionary of products with price and quantity sold as strings
products = {
    "Apple": ["1.20", "50"],   # "Item": [price, quantity sold]
    "Banana": ["0.50", "100"],
    "Cherry": ["2.50", "25"],
    "Mango": ["1.75", "40"]
}
total_sales_list = []

for product, product_info in products.items():
    price = float(product_info[0])
    quantity_sold = int(product_info[1])
    total_sales = price * quantity_sold
    print(f"Total sales for {product}: ${total_sales}")
    total_sales_list.append(total_sales)

total_sum = sum(total_sales_list)
min_sales = min(total_sales_list)
max_sales = max(total_sales_list)

print(f"Total sum of all sales: ${total_sum}\n"
      f"Minimum sales: ${min_sales}\n"
      f"Maximum sales: ${max_sales}")