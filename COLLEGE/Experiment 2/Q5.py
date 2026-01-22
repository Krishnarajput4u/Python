"""A shopkeeper buys an item and sells it. Cost Price is 500 rs selling price is 650 rs. Calculate and print profit or loss amt. SP-CP profit or the loss percentage and print whether its a profit or loss"""

cost_price = 500  # Cost Price in rs
selling_price = 650  # Selling Price in rs
if selling_price > cost_price:
    profit = selling_price - cost_price
    profit_percentage = (profit / cost_price) * 100
    print("Profit Amount:", profit, "rs")
    print("Profit Percentage:", profit_percentage, "%")
else:
    loss = cost_price - selling_price
    loss_percentage = (loss / cost_price) * 100
    print("Loss Amount:", loss, "rs")
    print("Loss Percentage:", loss_percentage, "%")