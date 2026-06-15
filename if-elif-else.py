#if-elif-else
print("🤵 Check which Person work as Indian President 🤵 from [1950-2026]")
year = int(input("Enter the year to see the president Info :  "))

if (year >= 1950 and year < 1962):
    print("Dr. Rajendra Prasad")
    print("Vice president : Sarvepalli Radhakrishnan ")
    print("Party : Indian National Congress")  #1

elif(year >= 1962 and year < 1967):
    print("Sarvepalli Radhakrishnan")
    print("Vice president : Zakir Husain ")
    print("Party : Independent")               #2

elif(year >= 1967 and year < 1969):
    print("Zakir Husain")
    print("Vice president : V. V. Giri ")
    print("Party : Independent")               #3

# elif(year >= 1969 and year < 1969): 
#     print("V. V. Giri")
#     print("Vice president : No Vice President ")
#     print("Party : No Party")                  #4
#     print("He only work 78 days as President of India.")

# elif(year >= 1969 and year < 1969): 
#     print("Mohammad Hidayatullah")
#     print("Vice president : No Vice President ")
#     print("Party : No Party")                  #5
#     print("He only work 35 days as President of India.")

elif(year >= 1969 and year < 1974):
    print("V. V. Giri")
    print("Vice president : Gopal Swarup Pathak ")
    print("Party : Independent")               #6

elif(year >= 1974 and year < 1977):
    print("Fakhruddin Ali Ahmed")
    print("Vice president : Gopal Swarup Pathak & B. D. Jatti ")
    print("Party : Indian National Congress (R)")               #7

# elif(year >= 1977 and year < 1977): 
#     print("B. D. Jatti")
#     print("Vice president : No Vice President ")
#     print("Party : No Party")                  #8
#     print("He only work 164 days as President of India.")

elif(year >= 1977 and year < 1982):
    print("Neelam Sanjiva Reddy")
    print("Vice president : B. D. Jatti & Mohammad Hidayatullah")
    print("Party : Janata Party")               #9

elif(year >= 1982 and year < 1987):
    print("Zail Singh")
    print("Vice president : Mohammad Hidayatullah & Ramaswamy Venkataraman")
    print("Party : Indian National Congress (I)")               #10

elif(year >= 1987 and year < 1992):
    print("Ramaswamy Venkataraman")
    print("Vice president : Shankar Dayal Sharma")
    print("Party : Indian National Congress (I)")               #11

elif(year >= 1992 and year < 1997):
    print("Shankar Dayal Sharma")
    print("Vice president : K. R. Narayanan")
    print("Party : Indian National Congress (I)")               #12

elif(year >= 1997 and year < 2002):
    print("K. R. Narayanan")
    print("Vice president : Krishan Kant")
    print("Party : Indian National Congress (I)")               #13

elif(year >= 2002 and year < 2007):
    print("A. P. J. Abdul Kalam")
    print("Vice president : Krishan Kant & Bhairon Singh Shekhawat")
    print("Party : Independent")               #14

elif(year >= 2007 and year < 2012):
    print("Pratibha Patil")
    print("Vice president : Hamid Ansari")
    print("Party : Indian National Congress")               #15

elif(year >= 2012 and year < 2017):
    print("Pranab Mukherjee")
    print("Vice president : Hamid Ansari")
    print("Party : Indian National Congress")               #16

elif(year >= 2017 and year < 2022):
    print("Ram Nath Kovind")
    print("Vice president : Hamid Ansari & Venkaiah Naidu")
    print("Party : Bharatiya Janata Party")               #17

elif(year >= 2022 and year == 2026):
    print("Droupadi Murmu")
    print("Vice president : Venkaiah Naidu & Jagdeep Dhankhar &  C. P. Radhakrishnan")
    print("Party : Bharatiya Janata Party")               #18

else:
    print("Enter correct year.")