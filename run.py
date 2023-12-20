import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('Perceive Stress Scale')

# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

#-- To print or display the worksheet--
# stress = SHEET.worksheet('Perceive Stress Scale')

# data = stress.get_all_values()

# print(data)
#----

def input_answers():
    print("How stressed are you?")
    print("Please answer the ten questions from 0 - 4")
    print("0 = never, 1 = almost never, 2 = sometimes, 3 = fairly often, 4 = very often")

    print("1. In the last month, how often have you been upset because of something that happened unexpectedly?")
    first_answer = input("Answer: ")
    print(f"Your answer on the first question is {first_answer}")

    print("2. In the last month, how often have you felt that you were unable to control the important things in your life?")
    second_answer = input("Answer: ")
    print(f"Your answer on the first question is {second_answer}")

    print("3. In the last month, how often have you felt nervous and stressed?")
    third_answer = input("Answer: ")
    print(f"Your answer on the first question is {third_answer}")

    print("4. In the last month, how often have you felt confident about your ability to handle your personal problems?")
    fourth_answer = input("Answer: ")
    print(f"Your answer on the first question is {fourth_answer}")

    print("5. In the last month, how often have you felt that things were going your way?")
    fifth_answer = input("Answer: ")
    print(f"Your answer on the first question is {fifth_answer}")

    print("6. In the last month, how often have you found that you could not cope with all the things that you had to do?")
    sixth_answer = input("Answer: ")
    print(f"Your answer on the first question is {sixth_answer}")

    print("7. In the last month, how often have you been able to control irritations In your life?")
    seventh_answer = input("Answer: ")
    print(f"Your answer on the first question is {seventh_answer}")

    print("8. In the last month, how often have you felt that you were on top of Things?")
    eight_answer = input("Answer: ")
    print(f"Your answer on the first question is {eight_answer}")

    print("9. In the last month, how often have you been angered because of things that happened That were outside of your control?")
    ninth_answer = input("Answer: ")
    print(f"Your answer on the first question is {ninth_answer}")

    print("10. In the last month, how often have you felt difficulties were piling up so high that You could not overcome them?")
    tenth_answer = input("Answer: ")
    print(f"Your answer on the first question is {tenth_answer}")

    
input_answers()
