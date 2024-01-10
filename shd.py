def fuhdas():
    user_input = int(input("insert number: "))
    divsor = 1
    prime = []
    while divsor <= user_input:
        if user_input%divsor == 0:
            prime.append(divsor)
        divsor += 1
    print(prime)


def ashdhas():
    x = input("racecar")
    if x == x[::-1]:
        print("palidrome")
    

ashdhas()

if equip == "Y":
          item = input("What would you like to equip?").title()
          if item not in Users.inventory:
               print("clowner misspelled 🤡 ")
          if item in Users.inventory:
               equipped = False
               if equipped == False:
                    Users.add_item_from_equipped(item)
                    input(f"{item} is now equipped")
                    return True
               
               if equipped == True:
                    equip_diff_item = input(f"You already have {Users.equipped} equipped. Are you sure you want to equip a different item? Y/N: ").title()
                    if equip_diff_item == "Y":
                         Users.remove_item_from_equipped(Users.equipped)
                         Users.add_item_from_equipped(item)
                         input(f"You have now equipped {item}.")
                         
                    if equip_diff_item == "N":
                         input("Ok.. returning to main screen...")

equipped = False
               if equipped == False:
                    Users.equipped.append(buddy_wanna_equip)
                    input(f"{buddy_wanna_equip} is now equipped")
                    equipped = True
                    return equipped
               
               if equipped == True:
                    equip_diff_item = input(f"You already have {Users.equipped} equipped. Are you sure you want to equip a different item? Y/N: ").title()
                    if equip_diff_item == "Y":
                         Users.remove_item_from_equipped(Users.equipped)
                         Users.add_item_from_equipped(buddy_wanna_equip)
                         input(f"You have now equipped {buddy_wanna_equip}.")
                    
               if equip_diff_item == "N":
                    input("Ok.. returning to main screen...")