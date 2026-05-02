data = [
  (749.17, "Investment Return"),
  (-11.54, "Utilities"),
  (-247.58, "Online Shopping"),
  (981.17, "Investment Return"),
  (-410.65, "Rent"),
  (310.60, "Rent"),
  (563.70, "Gift"),
  (220.79, "Salary"),
  (-49.85, "Car Maintenance"),
  (308.49, "Salary"),
  (-205.55, "Car Maintenance"),
  (870.64, "Salary"),
  (-881.51, "Utilities"),
  (518.14, "Salary"),
  (-264.66, "Groceries")
]

def print_transactions(data):
  for transactions in data:
    amount, statement = transactions
    print(f"${amount} - {statement}")
  

def print_summary(transactions):
  deposits = [transaction[0] for transaction in transactions if transaction[0] >= 0] 
  total_deposited = sum(deposits)
  print(total_deposited)
  withdrawls = [transaction[0] for transaction in transactions if transaction[0] < 0]
  total_withdrawn = sum(withdrawls)
  print(total_withdrawn)
  balance =total_deposited + total_withdrawn
  print(balance)


def analyze_transactions(transactions):
  transactions.sort()
  largest_deposit = transactions[-1]
  print(largest_deposit)
  largest_withdrawl = transactions[0]
  print(largest_withdrawl)
  deposits = [t[0] for t in transactions if t[0] >= 0]
  total_deposit = sum(deposits)
    
  if len(deposits) > 0:
      average_deposit = total_deposit / len(deposits)
  else:
      average_deposit = 0
  print(average_deposit)

  withdrawls = [t[0] for t in transactions if t[0] <= 0]
  total_withdrawls = sum(withdrawls)

  if len(withdrawls) > 0:
    average_withdrawl = total_withdrawls / len(withdrawls)
  else:
    average_withdrawl = 0
  print(average_withdrawl)    


while True:
  print("\nChoose an option:")
  print("1. Print summary (type 'print')")
  print("2. Analyze transactions (type 'analyze')")
  print("3. Stop program (type 'stop')")
  
  choice = input("Enter your option: ") 
  
  if choice.lower() == "print": 
    print_summary(data) 
  elif choice.lower() == "analyze":
    analyze_transactions(data) 
  elif choice.lower() == "stop":
    break
  else:
    print("Invalid choice")


  
