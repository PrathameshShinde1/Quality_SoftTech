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

for questionId, details in Quiz.items():
    for question, option in details.items():
        print(f"/t Questions - {details[question]}")
