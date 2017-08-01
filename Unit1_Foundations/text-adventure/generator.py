#namegenerator
import random


print("I can generate a name for you! Are you male or female?")
user_input = input()


firstNameFemale = ["Rebecca", "Jessica", "Mary", "Camille", "Belle", "Tina", "Melissa", "Lucy", "Tara", "Lauren", "Selena"]
firstNameMale = ["Mark", "Jack", "Max", "Kevin", "Daniel", "Justin", "Alan", "Zach", "Brian", "Ryan", "Ralph"]
lastName = ["Smith", "Peters", "Feldman", "Lee", "King", "Garfield", "Russo", "Bryant]

while user_input != "female" and user_input != "male":
    print ("I can generate a name for you! Are you male or female?")
    user_input = input()

if user_input == "female":
    print(random.choice(firstNameFemale) + " " + random.choice(lastName))
    # print(random.choice(lastName))

elif user_input == "male":
    print(random.choice(firstNameMale) + " " + random.choice(lastName))
    #print(random.choice(lastName))



#dinnermenu
#entrees = ["double cheeseburger", "parmesean chicken", "fettucinne alfredo", "shrimp pasta", "chicken and cheese quesadilla"]
#sides = ["french fries", "mashed potatoes", "carrots", "broccoli", "sweet potatoes"]
#drinks = ["water", "lemonade", "coke", "sprite", "seltzer", "iced tea", "root beer"]
#desserts = ["chocolate fudge sundae", "banana sundae", "chocolate mousse", "cheesecake"]

#print("Entree: " + random.choice(entrees))
#print("Side: " + random.choice(sides))
#print("Drink: " + random.choice(drinks))
#print("Dessert: " + random.choice(desserts))
