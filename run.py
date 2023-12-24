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


print("How stressed are you?")
print("Please answer the ten questions from 0 - 4")
print("0 = never, 1 = almost never, 2 = sometimes, 3 = fairly often, 4 = very often\n")

#-- To print or display the worksheet--
stress = SHEET.worksheet('Perceive Stress Scale')
questions = stress.get_all_values()


def theQuestions():
    for row in questions:
        print(row[0] + "\n")
        print(row[1] + "\n")
        print(row[2] + "\n")
        print(row[3] + "\n")
        print(row[4] + "\n")

       


def validate_allAnswers():
    answers = input("Please enter your five answers here: \n")
    allAnswers = list(map(int, answers.split(",")))
    #[int(answers) for answers in allAnswers]
    print(allAnswers)
    try:
        if len(allAnswers) != 5:
            raise ValueError(
                f"Please give the five answers. You gave {len(allAnswers)}"
            )
    except ValueError as e:
        print(f"Invalid Entry: {e}, Please give your answers from 0 to 4 again.\n")

    while True:
        print("please proceed...")
        break

    
    
theQuestions()
validate_allAnswers()






    
#

    #while True:        
      
#print(stress)
# data = stress.get_all_values()
# def to_validate_answer():
#    if answer <= 4 and answer >= 0:
#       print("Please proceed...")
#    else:
#        print("Your answer should be from 0 - 4!")