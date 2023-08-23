# Best Time to Buy and Sell Stock
# https://www.geeksforgeeks.org/best-time-to-buy-and-sell-stock/

# prices= [7, 1, 5, 3, 6, 4]
prices= [7, 6, 4, 3, 1] 
buy=prices[0]
max_profit=0
for i in prices[1:]:
    if buy > i:
        buy=i
    elif i-buy > max_profit:
        max_profit=i-buy 
print(max_profit)