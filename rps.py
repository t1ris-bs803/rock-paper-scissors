# num : Program's choose
# rps : Player's choose

# 1 : rock
# 2 : paper
# 3 : scissors

rpslist = ["rock", "paper", "scissors"]

import random

same = "Same!"
win = "You Win!"
lose = "You Lose!"

def rockpaperscissors(rps):
  num = random.randint(1, 3)

  if num == rps:
    return same
  elif (num == 1 and rps == 2) or (num == 2 and rps == 3) or (num == 3 and rps == 1):
    return = win
  else:
    return = lose

while True: 
  rps = input("choose Rock-Scissors-Paper : ").lower().strip()
  if rps not in rpslist:
    print ("please choose in list\nList : rock, scissors, paper")
  else:
    if rps == "rock":
      rps = 1
    elif rps == "paper":
      rps = 2
    else:
      rps = 3

    result = rockpaperscissors(rps)
    print(f"\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n {result}")
    
    
