#Task 1
def RailwayForm():
    print("**\t Welcome to Indian Railway **")
    print("")

    print("Good Morning, Sir/Madam.")
    print("Welcome to Indian Railways Survey. We appreciate your valuable time.")
    print("We would like to ask a few questions about your travel experience to help improve our railway services.")

    print("")
    print("What is your name?")
    name = str(input(""))
    print("")

    print("Enter your Gender")
    Gender = str(input("")) 
    print("")

    print("Which train did you travel on today?")
    TrainName = str(input(""))
    print("")

    print("From which station did you board the train? ")
    Board_Station = str(input(""))
    print("")

    print("What was your destination station?")
    Destinatin = str(input(""))
    print("")

    print("How would you rate [0-5] the cleanliness of the train?")
    Clean = int(input(""))
    print("")

    print("Were the train timings accurate and punctual? ")
    OnTime = str(input(""))
    print("")

    print("How was the behavior of the railway staff during your journey?")
    Staff = str(input(""))
    print("")

    print("Did you face any problems while booking your ticket? ")
    Problem = str(input(""))
    print("")

    print("Was your seat or berth comfortable?")
    confort = str(input(""))
    print("")

    print("How would you rate [0-5] the food and water facilities on the train? ")
    Facility = str(input(""))
    print("")

    print("Did you feel safe during the journey? ")
    Safe = str(input(""))
    print("")

    print("Were the toilets clean and properly maintained? ")
    Toilet = str(input(""))
    print("")

    print("How would you rate [0-5] the crowd management at the station? ")
    Crowd = str(input(""))
    print("")

    print("What improvements would you like to suggest for railway services? ")
    Improvement = str(input(""))
    print("")

    print("Would you prefer traveling by railway again in the future? Why?")
    Again = str(input(""))
    print("")


    print("Welcome to Indian Railways Survey.")
    print("Thank you for your valuable time and cooperation.")
    print("We hope you had a safe and comfortable journey.")

    print(f"✨ Thank You, {name} ✨")
# RailwayForm()

#Task 2

products = {
    "redmi" : {
        "Redmi A4 5G" : 11999.0, 
        "Redmi 13 5G" : 15499.0,
        "Redmi 14C 5G" : 12999.0,
        "Redmi Note 15 5G" : 29500.0
    },

    "realme" : {
        "Realme P4 Lite" : 13999.0,
        "Realme Narzo 100 Lite" : 14488.0,
        "Realme 11 Pro" : 8999.0
    },

    "apple" : {
        "iPhone 14" : 32599.0,
        "iPhone 15" : 67500.0,
        "iPhone 16" : 69000.0,
        "iPhone 17" : 82500.0 
    }, 

    "vivo" : {
        "Vivo T5x 5G" : 22999.0,
        "Vivo T4x 5G" : 14500.0,
        "Vivo Y31 5G" : 19999.0
    },

    "poco" :  {
        "POCO M6 Pro" : 8500.0,
        "POCO M7 Pro" : 11500.0,
        "POCO F7" : 35699.0
    },

    "oneplus" : {
        "OnePlus Nord" : 17500.0,
        "OnePlus 10 Pro" : 11500.0,
        "OnePlus 5T" : 6000.0,
        "OnePlus 3T" : 4500.0,
        "OnePlus 12 5G" : 38000.0
    }, 
    
    "samsung" : {
        "Samsung Galaxy A35 5G" : 30000.0,
        "Samsung Galaxy S25 Ultra" : 90000.0,
        "Samsung Galaxy M17 5G" : 14600.0,
        "Samsung Galaxy S25 FE" : 48500.0
    }
}

def Inventory():
    for company, item in products.items():
        print(f"Company : {company}")

        for model, price in item.items():
            print(f"    - {model} & {price} ₹ ")

    cart = []

    while True:
        buy = str(input("Do you want to purchase anything (Y/N) : ").lower())

        if buy != 'y':
            print("<======Cart======>")
            for item in cart:
                print(item['model'], "-", item['price'])

            total = 0
            for item in cart:
                total += item['price']
            
            print("Total amount : ", total)

            print("Thank you for visiting!")
            break;

        user_choice = input("Enter the company name which you want to buy a mobile : ").lower()

        if user_choice not in products:
            print("Enter a available items...")
            continue;

        print(f"\nAvailable {user_choice} mobiles are here -->")

        for index, (model, price) in enumerate(products[user_choice].items()):
            letter = chr(97 + index)
            print(f"{letter} - {model} & ₹{price}")
            
        models = list(products[user_choice].items())
        choice = input("Enter the Character of Model : ").lower()
        index = ord(choice) - ord("a")

        if index < 0 or index >= len(models):
            print("Invalid model Choice")
            continue

        model_name, price = models[index]

        cart.append({
            "model" : model_name,
            "price" : price
        })
        # print("Added items - ", cart)
        print("Cart added successfully!")

# Inventory()


#Task 3
#Quiz

#Task 4
#logical Operator

def Logical_Operator():
    while True:
        x = int(input("Enter a value : "))
        y = int(input("Enter a value : "))

        sign = input("Enter operation sign [+, -, *, /] : ")
        
        if sign == '/':
            if (y == 0):
                print("Denominator must not be Zero.")
                break
            else:
                continue

        match sign:
            case  '+':
                sum = x + y
                print("Addition : ",sum)
            case '-':
                sub = x - y
                print("Subtraction : ", sub)
            case '*':
                mul = x * y
                print("Multiplication : ", mul)
            case '/':
                div = x / y
                print("Division : ", div)
            case '_':
                print("Enter a valid sign...")

Logical_Operator()