from MainFunctions import *


class GameMode:
    def __init__(self, mode):
        self.mode = mode

    def execute(self, file):
        if self.mode == 'Store':
            self.StorePassword(file)
        elif self.mode == 'read':
            print('here')
            self.ReadPassword(file)
        elif self.mode == 'interactive':
            game_mode(file)

    def StorePassword(self, file):
        user_account = get_user_input("Enter your account ")
        user_password = get_user_input("Enter your password ")

        if not user_password or not user_account:
            return

        Password = {user_account: user_password}
        File_obj = File(file)
        data = File_obj.readFile()
        exists = False
        for d in data:
            if d.get(user_account):
                exists = True
                if exists:
                    update_pass = get_user_input("Password for this account already exists, do you want to update it? ")
                    if not update_pass:
                        return -1
                    if answerIsYes(update_pass):
                        d[user_account] = user_password
                        print("Password successfully updated")
                    else:
                        print("Password not updated, going back to the main menu.")
        if not exists:
            data.append(Password)
            print("___Password successfully stored___")

        data = json.dumps(data)
        f = File(file)
        f.writeFile(data)

    def ReadPassword(self, file):
        print('called this')
        data = readFile(file)
        interactive_printing = get_user_input("Do you want interactive listing of all of your passwords? ")
        if not interactive_printing:
            return -1
        if answerIsYes(interactive_printing):
            self.print_with_table(data)
            print("Total number of passwords is", len(data))
            return
        user_account = get_user_input("Enter the account ")
        if not user_account:
            return -1

        for d in data:
            if d.get(user_account):
                print(d[user_account])
                return
        print("Not found")

    def print_with_table(self, password_list):
        for password in password_list:
            for account in password.keys():
                print('|', account, password[account], '|')

    def game_mode(self, file):
        data = readFile("data.json")
        score_records = readFile("score_records.json")
        view_results = get_user_input("If you want to play, type yes, if you want to view the results, type no ")
        if not view_results:
            return -1
        if answerIsNo(view_results):
            self.print_with_table(score_records)
            print("Total number of records is", len(score_records))
        else:
            score = 0
            already_asked = []

            amount_of_passwords = len(data)
            number_of_questions = amount_of_passwords // 2
            for i in range(number_of_questions):
                n = 0
                not_found = True
                while not_found:
                    n = randint(0, amount_of_passwords - 1)
                    if data[n] not in already_asked:
                        already_asked.append(data[n])
                        not_found = False

                question_account = data[n]
                print(get_key(question_account))
                guess = get_user_input("Enter the password you remember for this account ")
                if not guess:
                    return -1
                if guess == question_account[get_key(question_account)]:
                    print("!!!!!CORRECT!!!!!")
                    score += 1
                else:
                    print("!!!!!WRONG!!!!!")
            print("Your final score is", score)
            data = readFile("score_records.json")
            data.append({str(date.today()): score})
            data = json.dumps(data)
            writeFile("score_records.json", data)


def number_is_even(number):
    if n % 2 == 0:
        return True
    return False
