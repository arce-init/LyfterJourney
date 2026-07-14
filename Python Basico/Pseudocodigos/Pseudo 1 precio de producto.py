product_price = float(input("Type the price of the product: "))
discount = 0
final_price = 0
if product_price < 100:
    discount = product_price * 0.02
else:
     discount = product_price * 0.10

final_price = product_price - discount
print(f"The final price is: {final_price}")