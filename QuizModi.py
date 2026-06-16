import random

Quiz = {
    "Q1" : {
        "question" : "What is Square of 25?",
        "option" : ["2", "3", "4", "5"]
    },

    "Q2" : {
        "question" : "Which planet is known as the 'Red Planet'?",
        "option" : ["Venus", "Jupiter", "Mars", "Saturn"]
    },

    "Q3" : {
        "question" : "What is the capital of India?",
        "option" : ["Delhi", "Mumbai", "Bhopal", "Rajyasthan"]
    },

    "Q4" : {
        "question" : "What does CPU stand for?",
        "option" : ["Central Processing Unit", "Computer Processing Unit", "Central Program Unit", "Control Processing Unit"]
    },

    "Q5" : {
        "question" : "In SQL, which command is used to retrieve data from a table?",
        "option" : ["INSERT", "UPDATE", "SELECT", "DELETE"]
    },

    "Q6" : {
        "question" : "A train travels 240 km in 4 hours. What is its average speed?",
        "option" : ["50 km/h", "55 km/h", "60 km/h", "65 km/h"]
    },

    "Q7" : {
        "question" : "What is the next number in the series? --> 2, 6, 12, 20, 30, ?",
        "option" : ["36", "40", "42", "44"]
    },

    "Q8" : {
        "question" : "Which is the largest ocean on Earth?",
        "option" : ["Atlantic Ocean", "Arctic Ocean", "Indian Ocean", "Pacific Ocean"]
    },

    "Q9" : {
        "question" : "The national animal of India is?",
        "option" : ["Lion", "Elephant", "Tiger", "Peacock"]
    },

    "Q10" : {
        "question" : "Which of the following is NOT a programming language?",
        "option" : ["Java", "Python", "Oracle", "C++"]
    }
}

Answers = {
    "A1" : "5",
    "A2" : "mars",
    "A3" : "delhi",
    "A4" : "central processing unit",
    "A5" : "select",
    "A6" : "60 km/h",
    "A7" : "42",
    "A8" : "pacific ocean",
    "A9" : "tiger",
    "A10" : "oracle"
}
# while True:

#     UserAns = []
#     QuestionSet = random.sample(list(Quiz.items()), 8)
    
#     for index,(questionId, details) in enumerate(QuestionSet, start=1):
#             print(f"Questions {index} - {details['question']}")
#             print("Options - ")
#             for index, option in enumerate(details['option']):
#                 print(f"    {chr(97+index)} - {option}")

#             ans = input("Enter your Answer : ")
#             if ans!=['a','b','c','d']:
#                  print("Please give asnwer in a,b,c,d")
#             else:
#                 UserAns.append(ans)
#                 print("-"*40)
#     print(UserAns)
#     break


while True:

    score = 0
    UserAns = []

    QuestionSet = random.sample(list(Quiz.items()), 8)

    for q_no, (questionId, details) in enumerate(QuestionSet, start=1):

        print(f"\nQuestion {q_no} - {details['question']}")
        print("Options -")

        for opt_no, option in enumerate(details['option']):
            print(f"    {chr(97 + opt_no)} - {option}")

        while True:
            ans = input("Enter your Answer (a/b/c/d): ").lower().strip()

            if ans not in ['a', 'b', 'c', 'd']:
                print("Please enter a, b, c, or d")
            else:
                UserAns.append(ans)

                # Get selected option text
                selected_option = details['option'][ord(ans) - ord('a')].lower()

                # Get correct answer
                answer_key = f"A{questionId[1:]}"  # Q1 -> A1
                correct_answer = Answers[answer_key].lower()

                # Check answer
                if selected_option == correct_answer:
                    score += 1

                print("-" * 40)
                break

    wrong = len(QuestionSet) - score

    print("\nQuiz Finished!")
    print(f"Correct Answers : {score}")
    print(f"Wrong Answers   : {wrong}")
    print(f"Score           : {score}/{len(QuestionSet)}")

    break