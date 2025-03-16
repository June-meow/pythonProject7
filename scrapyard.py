from PIL import Image
import time

questions = [
    {
        1: "What is 1 + 1: ",
        2: ["A. 2", "B. 4"],
        3: "A"

    },
]


def run_questions(questions):
    score = 0
    for x in questions:
        print(x[1])
    for option in x[2]:
        print(option)
    answer = input("Enter your answer A or B: ")
    if answer == x[3]:
        print("Incorrect. The answer was F. Window.")
    elif answer == "F.":
        print("CORRECT! YES, IT IS F. Window!!!")
    elif answer == "F. Window":
        print("YES YOU ARE CORRECT")

    else:
        print("Incorrect. The answer was F. Window.")

    time.sleep(3)
    img = Image.open("Window.png")
    img.show()

    print("Your score: 0")



    # scrappy



run_questions(questions)