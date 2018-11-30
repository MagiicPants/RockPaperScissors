import random
import time

items = ["rock", "paper", "scissors"]
score = 0
comp_score = 0

game = input("Would you like to play Rock-Paper-Scissors? yes or no - ")
if game == 'yes':
    print("\n")
    print(
        "\tINSTRUCTIONS:\nYou will select one of three items: rock, paper, or scissors.\nRock beats scissors,scissors beats paper, and paper beats rock.\nYour opponent will select one of the three choices too.\nWhoever's choice beats the other wins.\nBest out of 3.")
    print("\n")
    # loop
    while game == 'yes':
        choice = input("\tPick your item: rock, paper, scissors- ")
        comp_choice = random.choice(items)

        if choice == comp_choice:
            print("3")
            time.sleep(0.8)
            print("2")
            time.sleep(0.8)
            print("1")
            time.sleep(0.8)
            print(f"You chose:\t\tYour opponent chose:\n%s\t\t\t%s" % (choice, comp_choice))
            print("\tIt was a tie!")
            score += 0
            comp_score += 0
            print(f"Your score:{score}\tOpponents score:{comp_score}")

        elif choice == 'rock':
            if comp_choice == 'paper':
                print("3")
                time.sleep(0.8)
                print("2")
                time.sleep(0.8)
                print("1")
                time.sleep(0.8)
                print(f"You chose:\t\tYour opponent chose:\n%s\t\t\t%s" % (choice, comp_choice))
                print("\tYou Lose!")
                score += 0
                comp_score += 1
                print(f"Your score:{score}\tOpponents score:{comp_score}")
            else:
                print("3")
                time.sleep(0.8)
                print("2")
                time.sleep(0.8)
                print("1")
                time.sleep(0.8)
                print(f"You chose:\t\tYour opponent chose:\n%s\t\t\t%s" % (choice, comp_choice))
                print("\tYou Win!")
                score += 1
                comp_score += 0
                print(f"Your score:{score}\tOpponents score:{comp_score}")

        elif choice == 'paper':
            if comp_choice == 'rock':
                print("3")
                time.sleep(0.8)
                print("2")
                time.sleep(0.8)
                print("1")
                time.sleep(0.8)
                print(f"You chose:\t\tYour opponent chose:\n%s\t\t\t%s" % (choice, comp_choice))
                print("\tYou Win!")
                score += 1
                comp_score += 0
                print(f"Your score:{score}\tOpponents score:{comp_score}")
            else:
                print("3")
                time.sleep(0.8)
                print("2")
                time.sleep(0.8)
                print("1")
                time.sleep(0.8)
                print(f"You chose:\t\tYour opponent chose:\n%s\t\t\t%s" % (choice, comp_choice))
                print("\tYou Lose!")
                score += 0
                comp_score += 1
                print(f"Your score:{score}\tOpponents score:{comp_score}")

        elif choice == 'scissors':
            if comp_choice == 'rock':
                print("3")
                time.sleep(0.8)
                print("2")
                time.sleep(0.8)
                print("1")
                time.sleep(0.8)
                print(f"You chose:\t\tYour opponent chose:\n%s\t\t\t%s" % (choice, comp_choice))
                print("\tYou Lose!")
                score += 0
                comp_score += 1
                print(f"Your score:{score}\tOpponents score:{comp_score}")
            else:
                print("3")
                time.sleep(0.8)
                print("2")
                time.sleep(0.8)
                print("1")
                time.sleep(0.8)
                print(f"You chose:\t\tYour opponent chose:\n%s\t\t\t%s" % (choice, comp_choice))
                print("\tYou Win!")
                score += 1
                comp_score += 0
                print(f"Your score:{score}\tOpponents score:{comp_score}")
        if score == 3:
            print("You Win against opponent!")
            break
        elif comp_score == 3:
            print("You lose against opponent!")
            break
            '''       
            if choice == 'rock':
            print("3")
            time.sleep(0.8)
            print("2")
            time.sleep(0.8)
            print("1")
            time.sleep(0.8)
            print("\n")
            print(f"You chose:\t\tYour opponent chose:\n%s\t\t\t%s" % (choice, comp_choice))
            
            '''