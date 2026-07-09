# Topic 10 Collaborative Assignment
# Your Name: Steve Young  
# Date: 7-9-2026

#Screw Inventory
class FeederScrew:
  def __init__(self, part_number, quantity):
    self.part_number = part_number
    self.quantity = quantity

  def issue_screws(self, amount):
    if amount < 0:
      print("Error: Enter a positive quantity.")
    elif amount > self.quantity:
      print("Error: Not enough feeder screws in inventory.")
    else:
      self.quantity -= amount
      print(f"{amount} screws issued.")
      print(f"Remaining inventory: {self.quantity}")

#Instance
inventory = FeederScrew("S18/19" , 20)

print("***Feeder Screw Inventory System***")
print(f"Part Number: {inventory.part_number}")
print(f"Current Quantity: {inventory.quantity}")

#Exception
try:
  amount = int(input("Enter the number of feeder screws to issue: "))
  inventory.issue_screws(amount)

except ValueError:
  print("Error: Please enter a whole number.")

print("Inventory transaction complete.")
