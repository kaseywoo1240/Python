class Account:
  def  __init__(self, filepath):
    self.filepath = filepath
    with open(filepath, 'r') as file:
      self.balance = int(file.read())

  def withdraw(self, amount):
    self.balance = self.balance - amount

  def deposit(self, amount):
    self.balance = self.balance + amount

  def commit(self):
    with open(self.filepath, 'w') as file:
      file.write(str(self.balance))

class Checking(Account):
  def __init__(self, filepath):
    Account.__init__(self, filepath)

  def transfer(self, amount):
    self.balance = self.balance - amount


que = input("What do you want to do?\n Press 'd' for Deposit, 't' for Transfer, 'w' for Withdraw.")

checking = Checking("balance.txt")
account = Account("balance.txt")

if que == "d":
  x = int(input("Enter the Amount to Deposit: "))
  account.deposit(x)
  print("Your transaction is successful")
  print("Balance Left: {}".format(account.balance))
  account.commit()

elif que == "w":
  y = int(input("Enter the amount to Withdraw: "))
  account.withdraw(y)
  print("Your transaction is successful")
  print("Balance Left: {}".format(account.balance))
  account.commit()

elif que == "t":
  z = int(input("Enter the amount to Transfer: "))
  checking.withdraw(z)
  print("Your transaction is successful")
  print("Balance Left: {}".format(checking.balance))
  checking.commit()
