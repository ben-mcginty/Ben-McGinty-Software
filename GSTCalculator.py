itemCost = input("What is the cost of your item without GST? ")
# askes user for prce

itemCostInt = int(itemCost)
#converts user string to interger

priceDivide100 = itemCostInt  / 100
#makes the price 1%

finalPrice = priceDivide100 * 112
#makes price 112% of itenCost (applies 12% GST)

print("")
print("Your total price including GST of 12% is:")
print(finalPrice)
#prints work
