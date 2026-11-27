fuel_type = input("Enter fuel type (Petrol/Diesel): ")
quantity = float(input("Enter quantity in litres: "))
price = float(input("Enter price per litre: "))

total = quantity * price

print("\n----- Fuel Bill -----")
print("Fuel Type:", fuel_type)
print("Quantity:", quantity, "litres")
print("Price per litre: Rs.", price)
print("Total Cost: Rs.", total)
