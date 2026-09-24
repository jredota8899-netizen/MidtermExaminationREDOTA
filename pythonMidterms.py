itemName = ""
quantitySold = 0
pricePerUnit = 0

print ("=" * 39)
print ("        SALES RECORD MANAGEMENT")
print("=" * 39)
print("1. add sales record")
print("2. View All Record & Summary Statistics")
print("3. Clear All Sales")
print("Exit System")
print("=" * 39)



choice = input("select an option (1-4): ")
if choice == "1":
    itemName = input("Enter the Item Name: ")
    quantitySold = int(input("Enter Quantity sold: "))
    pricePerUnit = float(input("Enter Price per Unit: "))
    totalAmount = quantitySold * pricePerUnit
    print(f"Item Name: {itemName}, Quantity Sold: {quantitySold}, Price Per Unit: {pricePerUnit}, Total Amount: {totalAmount}")
    exit()

elif choice == "2":
    fname = input("Enter file name: ")
    fhand = open(fname)

elif choice == "4":
    print("Thank you for using the Sales Record Management System.")
    exit()

