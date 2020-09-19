from MainFunctions import *
from main_tools import *

def main():
    file_name = 'data.json'
    fill_the_file(file_name)
    action = None
    authenticated = False
    while not authenticated:
        authenticated = False
        while not authenticated:
            if authenticate():
                authenticated = True
            else:
                print("Incorrect password, please try again")
    while True:
        print("Do you want to store password? If YES, type y, if you want to get one of your passwords, type n")
        print("If you want to change your password for this app, type change")
        stores = Answer('')
        stores.get_user_input('If you want to try our game mode type interactive')
        mode = GameMode('')
        if not stores.text:
            break
        if stores.answer_is_yes():
            mode.mode = 'Store'
            print("Storing")
        elif stores.answer_is_no():
            mode.mode = 'read'
        elif stores.answer_is_change():
            update_authentication_password()
        elif stores.answer_is_interactive():
            mode.mode = 'interactive'
        else:
            print("Invalid input, going back to the main menu ")

        if mode.mode:
            x = mode.execute(file_name)
            if x == -1:
                break
    print("You closed our app")
    print("Thank you for using our app")

main()