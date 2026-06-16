import random
import string

# Password length
length = int(input("Enter password length: "))

# Character sets
uppercase = string.ascii_uppercase
lowercase = string.ascii_lowercase
numbers = string.digits
special = string.punctuation

# Ensure at least one character from each category
password = [
    random.choice(uppercase),
    random.choice(lowercase),
    random.choice(numbers),
    random.choice(special)
]

# Fill remaining length with random characters
all_characters = uppercase + lowercase + numbers + special

for _ in range(length - 4):
    password.append(random.choice(all_characters))

# Shuffle the password
random.shuffle(password)

# Convert list to string
password = "".join(password)

print("\nGenerated Password:")
print(password)