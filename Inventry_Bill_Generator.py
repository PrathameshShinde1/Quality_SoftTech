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

    # if user_choice == "redmi":
    #     print(f"Available {user_choice} mobile are here -->")
    #     for index, (model, price) in enumerate(products[user_choice].items()):
    #         letter = chr(97 + index)
    #         print(f" {letter} - {model} & {price} ₹")
    # elif user_choice == "realme":
    #     print(f"Available {user_choice} mobile are here -->")
    #     for index, (model, price) in enumerate(products[user_choice].items()):
    #         letter = chr(97 + index)
    #         print(f" {letter} - {model} & {price} ₹")
    # elif user_choice == "apple":
    #     print(f"Available {user_choice} mobile are here -->")
    #     for index , (model, price) in enumerate(products[user_choice].items()):
    #         letter = chr(97 + index)
    #         print(f" {letter} - {model} & {price} ₹")
    # elif user_choice == "vivo":
    #     print(f"Available {user_choice} mobile are here -->")
    #     for index, (model, price) in enumerate(products[user_choice].items()):
    #         letter = chr(97 + index)
    #         print(f" {letter} - {model} & {price} ₹")
    # elif user_choice == "poco":
    #     print(f"Available {user_choice} mobile are here -->")
    #     for index, (model, price) in enumerate(products[user_choice].items()):
    #         letter = chr(97 + index)
    #         print(f" {letter} - {model} & {price} ₹")
    # elif user_choice == "oneplus":
    #     print(f"Available {user_choice} mobile are here -->")
    #     for index, (model, price) in enumerate(products[user_choice].items()):
    #         letter = chr(97 + index)
    #         print(f" {letter}  - {model} & {price} ₹")
    # elif user_choice == "samsung":
    #     print(f"Available {user_choice} mobile are here -->")
    #     for index, (model, price) in enumerate(products[user_choice].items()):
    #         letter = chr(97 + index)
    #         print(f" {letter}  - {model} & {price} ₹")
    # else:
    #     print("Please enter a valid Company name!!!")
    
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

