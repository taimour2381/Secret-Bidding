logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
print(logo)
participant = {}
do = "yes"
while do == "yes":
    name = input("Enter the name of bidder: ")
    bid = int(input("Enter the bid amount: $"))
    participant[name] = bid
    do = input("do you want to add more participants to the bid? 'yes' or 'no'\n : ")

# print (participant)
highest_bid = 0
winner = ""
for bidder in participant:
    bid_amount = participant[bidder]
    if bid_amount > highest_bid:
        highest_bid = bid_amount
        winner = bidder
    else:
        bid_amount = bid_amount

print(f"{winner} won the bidding with highest bid of ${highest_bid}")
