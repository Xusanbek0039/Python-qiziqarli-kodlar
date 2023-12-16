import random

strength = 100
level = 1
rounds = 10

def play():
  
  print_intro()
  
  for round in range(1,rounds+1):
    
    print(f"Round: {round}")
    
    choose_action()
    
    if check_win():
      print("You win!")
    else:
      print("You lose!")
      
    print_status()
      
  print("Game over!")

def print_intro():
  print("Welcome to the game!")

def choose_action():
  action = input("Write (attack) or (stop): ")
  if action == "attack":
    battle()
  else:
    print("Game stopped!")
    exit()
  
def battle():
  attacker = ["🦍","🔥","🦧","⚔️"] 
  defender = ["🦍","⚔️","🦧","🔥"]
  outcome = random.choice(["win","lose"])
  
  if outcome == "win":
    print(random.choice(attacker), random.choice(defender))
    print("You win!")
    update_stats()
  else:
    print(random.choice(attacker), random.choice(defender))
    print("You lose!")
  
def update_stats():
  global strength, level  
  strength += 100
  level += 1
  
def print_status():
  print(f"Strength: {strength}")
  print(f"Level: {level}")
  
play()