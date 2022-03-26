#Prompt & read unit price from user
unitPrice = float(input("Enter the unit price: "))
#Prompt & read quantity from user
quantity = int(input("Enter the quantity: "))

#Calculate revenue
extendedPrice = unitPrice * quantity

#Print the extendedPrice
print("The extendedPrice is $", extendedPrice, ".", sep='')
