from replit import clear
from art import logo
print(logo)
#HINT: You can call clear() to clear the output in the console.

bid_log = []
def bidding(bid_name, bid_amount):
    bids = {}
    bids["name"] = bid_name
    bids["bid"] = int(bid_amount)
    bid_log.append(bids)

process = False
while not process:
  bid_name_value = input("What is your name?")
  bid_amount_value = input("What is your bid amount? $")
  bidding(bid_name_value, bid_amount_value)
  yes_no_checker = input("Do you need one more bid yes or no?")
  if yes_no_checker == "no":
    process = True
  elif yes_no_checker == "yes":
    clear()
  

# need to undestad qhat is the biggest velue in in bid_amount 
def find_highest_bidder(bid_log):
  highest_bid = 0
  highest_bidder = ""
  for bid in bid_log:
    if bid["bid"] > highest_bid:
      highest_bid = bid["bid"]
      highest_bidder = bid["name"]
  if highest_bid:
    print(f"The winner is {highest_bidder} with bid {highest_bid}")

find_highest_bidder(bid_log)

