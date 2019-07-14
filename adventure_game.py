# Find the near grocery marcket and buy a baby milk for your baby!
import time
import random

clock = 5
item = []
bar_item = random.choice(['beer', 'sparkling water', 'milk'])


def print_pause(message, sec):
    print(message)
    time.sleep(sec)


def intro(clock):
    print_pause("Tick tock..", 1)
    print_pause("It's " + str(clock) + "PM.", 1)
    print_pause("You've done work today.", 1)
    print_pause("Hey David, we're going to the pub. Are you in?", 1)
    print_pause("What do you want?\n", 1)


def work(item, clock, bar_item):
    # Things that happen to the player in the field
    choice = input("Enter 1 to go back to your home.\n"
                   "Enter 2 to go to the pub\n")
    if choice == '1':
        # Going to home
        print_pause("I am sorry, I think I cannot make it."
                    "I have to go back to home, today.", 2)
        home(item)
    elif choice == '2':
        # Going to the pub
        print_pause("Sure, let's go!", 1)
        pub(bar_item)
    elif choice not in ['1', '2']:
        if clock < 9:
            # Work more by 9PM when the user types wrong number
            print_pause("You are not done yet. Go back to work!\n", 1)
            print_pause("...", 1)
            clock += 1
            # Add one more hr for wrong type
            work(item, clock, bar_item)
            print(clock)
        else:
            print_pause("It's " + str(clock) +
                        "PM. Your are done, Go home!\n\n", 2)
            home(item)


def order(item):
        print_pause("Honey, we don't have a milk anymore.", 1)
        print_pause("Could you buy it for Daniel, now?", 1)
        print_pause("Your wife is asking you to buy a baby milk", 1)
        print_pause("Do you wanna go to the grocery store?", 1)
        response = input("Please enter: 'yes' or 'no'\n").lower()
        if 'yes' in response:
            print_pause("Sure sweety, I will come back soon.", 1)
            print_pause("...", 1)
            print_pause("You got the milk.\n", 1)
            item.append('milk')
            home(item)
        elif 'no' in response:
            print_pause("Sweety, I just came back. "
                        "I will buy it after 30min break..", 1)
            print_pause("...", 1)
            print_pause("30 mins later...", 1)
            print_pause("Honey, it's time to go!", 1)
            print_pause("Okay, I will be back!", 1)
            item.append('milk')
            home(item)
        else:
            print_pause("Sorry, I cannot hear you! What did you say?", 1)
            order(item)


def home(item):
    # Things that happen to the player in the house
    print_pause("Sweety, Daniel~ Daddy is here!", 1)
    if "milk" in item:
        happy_ending()
    else:
        if "beer" in item:
            print_pause("Honey, did you drink?", 1)
            response = input("Please enter: 'yes' or 'no'.\n").lower()
            if 'yes' in response:
                print_pause("Hoeny, don't drink too much.", 1)
                order(item)
            elif 'no' in response:
                print_pause("EEEK Smell... You are lier.", 1)
                print_pause("She doesn't want to talk with you anymore.", 1)
                print_pause("GAME OVER!!", 2)
                while True:
                    replay = input("Would you like to play again? (yes/no)").lower()
                    if 'yes' in replay:
                        adventure_game(clock, bar_item)
                    elif 'no' in replay:
                        print_pause("Good Bye", 1)
                        break
        else:
            order(item)


def pub(bar_item):
    # Things that happen to the player in the cave
    print_pause("You are heading to the pub with your friends.", 1)
    print_pause("...", 1)
    print_pause("Ring~ Ring~ Ring~ Ring~ Ring~", 1)
    print_pause("Your wife is calling you.", 1)
    print_pause("Honey, where are you?", 1)
    print_pause("I am going to pub with friends. "
                "I will go back to home around 7PM", 1)
    print_pause("Okay, but can you buy more milk for Daniel?", 1)
    print_pause("Sure, I will get it", 1)
    print_pause("Thank you.", 1)
    print_pause("...", 1)
    print_pause("...", 1)
    print_pause("Oh, it's almost 7PM. I have to go! "
                "See you guys tomorrow!\n", 2)
    item.append(bar_item)
    home(item)


def happy_ending():
    print_pause("Sweety, here is a milk.", 1)
    print_pause("Honey, Thank you so much!", 1)
    print_pause("KISS!!", 1)
    print_pause("Happy Ending. You win!", 2)


def sad_ending():
    print_pause("I am sorry, I forgot it...", 1)
    print_pause("I asked you the milk!!!", 1)
    print_pause("FIGHT!", 1)
    print_pause("Sad Ending. You lose", 2)


def adventure_game(clock, bar_item):
    intro(clock)
    work(item, clock, bar_item)


adventure_game(clock, bar_item)
