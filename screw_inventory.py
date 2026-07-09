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
      return False
    elif amount > self.quantity:
      print("Error: Not enough feeder screws in inventory.")
      return False
    else:
      self.quantity -= amount
      print(f"{amount} screws issued.")
      print(f"Remaining inventory: {self.quantity}")
      return True

#Instance
inventory = FeederScrew("S18/19" , 20)

print("***Feeder Screw Inventory System***")
print(f"Part Number: {inventory.part_number}")
print(f"Current Quantity: {inventory.quantity}")

#Exception
while True:
  try:
    amount = int(input("Enter the number of feeder screws to issue: "))
    if inventory.issue_screws(amount):
      break

  except ValueError:
    print("Error: Please enter a whole number.")

print("Inventory transaction complete.")
