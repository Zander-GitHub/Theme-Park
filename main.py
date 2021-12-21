wallet = 1500

guests = 0

day = 1

rating = ""

rides = []

restauraunts = []

ridecosts = {
  'wooden coaster' : 1500,
  'fast coaster' : 2000,
  'indoor coaster' : 3000
}

mpd = {
  "fast coaster" : 300,
  "indoor coaster" : 500,
  "wooden coaster" : 100
}

restm = {
  "burgers" : 700,
  "pizza" : 500,
  "drinks" : 40
}

def res():
  global mpd
  global wallet
  restauraunts.count("burgers")
  restauraunts.count("drinks")
  restauraunts.count("pizza")
  wallet += restm["burgers"] * restauraunts.count("burgers")
  wallet += restm["pizza"] * restauraunts.count("pizza")
  wallet += restm["drinks"] * restauraunts.count("drinks")

def moneyperday():
  global mpd
  global wallet
  rides.count("wooden coaster")
  rides.count("fast coaster")
  rides.count("indoor coaster")
  wallet += mpd["indoor coaster"] * rides.count("indoor coaster")
  wallet += mpd["fast coaster"] * rides.count("fast coaster")
  wallet += mpd["wooden coaster"] * rides.count("wooden coaster")

def foodmenu():
  global guests
  global ridecount
  global wallet
  print("Your balance is : $", wallet)
  print("Pizzaria", "$" ,restm["pizza"])
  print("Refreshments:", "$" ,restm["drinks"])
  print("Burger Shop:", "$" ,restm["burgers"])
  print("\nWhat would you like to purchase?")
  buy = input()
  buy = buy.lower()
  if buy == "burger shop":
    print('Purchaced.')
    guests += 4
    wallet -= 700
    restauraunts.append("burger shop")
  elif buy == "pizzaria":
    print('Purchaced.')
    guests += 6
    wallet -= 500
    restauraunts.append("pizzaria")
  elif buy == "refreshments":
    print('Purchaced.')
    guests += 2
    wallet -= 40
    restauraunts.append("drinks")
  else:
    "Purchase unsuccessful. Please type 'food' again."

def buymenu():
  global guests
  global ridecount
  global wallet
  print("Your balance is : $", wallet)
  print("Wooden Coaster:", "$" ,ridecosts["wooden coaster"])
  print("Fast Coaster:", "$" ,ridecosts["fast coaster"])
  print("Indoor Coaster:", "$" ,ridecosts["indoor coaster"])
  print("\nWhat would you like to purchase?")
  buy = input()
  buy = buy.lower()
  if buy == "wooden coaster":
    print('Purchaced.')
    rides.append("wooden coaster") 
    guests += 3
    wallet -= 1500
  elif buy == "indoor coaster":
    print('Purchaced.')
    rides.append("indoor coaster") 
    guests += 5
    wallet -= 2000
  elif buy == "fast coaster":
    print('Purchaced.')
    rides.append("fast coaster") 
    guests += 7 
    wallet -= 3000
  else:
    "Purchase unsuccessful. Please type 'shop' again."

while wallet > -10000:
    if guests < 20:
      rating = "1 star."
    elif guests > 30 and guests < 40 or guests == 30:
      rating = "2 stars." 
    elif guests > 40 and guests < 50 or guests == 40:
      rating = "3 stars."
    elif guests > 50 and guests < 60 or guests == 50:
      rating = "4 stars."
    elif guests > 60 or guests == 60:
      rating = "5 stars."
    if rating == "5 stars.":
      print("\nCongratulations!\nYou got to 5 stars!\nYou can continue playing if you would like.\n")
    r = input('What do you wanna do? You can type "help" for help.\n')
    r = r.lower()
    if r == "help":
        print('\nThe following commands are available:\n')
        print('Shop: Opens the store\n')
        print('Food: Buy restauraunts.\n')
        print('Owned: Shows your owned rides/items\n')
        print("Quit: Quits the game (DOESN'T SAVE YET.)\n")
        print('Balance: Displays money amount\n')
        print('Guests: Shows amount of current guests.\n')
        print('Rating: Displays your rating out of 5 stars.\n')
        print("Tutorial: Shows you how to play!\n")
        print("Credits: Shows the credits.")
    elif r == "credits":
      print("Concept by the many theme park builders in the world!")
      print("Created and programmed by: Zander Franks")
      print("Thank you to my teacher Mr. Neimitalio for teaching me python!")
    elif r == "tutorial":
      print("To play this game, first type 'shop'\nHere you can choose what to buy.\nThe better the ride, the more your rating goes up.\nYou win when you reach 5 stars!\nYou will lose if you go under -10000 dollars.\nGood Luck!")
    elif r == "food":
      print('\nRestauraunt store!')
      foodmenu()
    elif r == "shop":
        print('\nEpic coaster store!')
        buymenu()
    elif r == "skip":
        print('Skipping day.')
        moneyperday()
    elif r == "balance":
        print("Your balance is : $", wallet)
    elif r == "rating":
        print("Your rating is", rating)
    elif r == "guests":
        print("guests:", guests)
    elif r == "motherlode":
        print("free money xd (+$50000)")
        wallet += 50000
    elif r == "owned":
        print("we have not added this yet lmao")
    elif r == "quit":
        print("Thanks for playing.")
        break
    else:
        print("\nCommand not recognized.\n")
print("You went bankrupt or quit game.")