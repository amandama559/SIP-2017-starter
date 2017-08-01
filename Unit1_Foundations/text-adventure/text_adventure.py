start ="""
Today, Amanda is plannning to head out to NYC for a fun-filled day!
Her agenda for today is to first to meet her friends in Soho to shop and eat lunch.
Then she has a hair appointment at 1:30 pm and dinner with her sister at 6:00 pm.
She begins her morning when she wakes up at 9:30 am.
Because it takes an hour to get to Soho from where she is in Brooklyn, should she spend time
eating breakfast or skip breakfast to meet earlier with her friends?"""

print(start)

shops = ["Pacsun", "American Eagle", "Zara", "Sephora", "Mac", "Aerie", "Primark", "Adidas", "Forever 21"]
user_input = ""

while user_input != "eat" and user_input != "skip":
    print("Type 'eat' to leave later or 'skip' to leave now.")
    user_input = input()


    shopsToVisit = []
    shopsToGo = []
if user_input == "eat":
    print("""
Amanda decides to sit and eat breakfast at home.
She ends up leaving at 10:00 am and gets to Soho at 11:00 am to meet her friends.
Now, they need to decide which stores to shop in.
Because they need an hour to eat lunch, and since Amanda has her hair appointment at 1:30 pm,
they can only go to a few shops.
They will spend 30 minutes at each shop, so Amanda must pick 3 to go to.
Out of Pacsun, American Eagle, Zara, Sephora, Mac, Aerie, Primark, Adidas, and Forever 21
what three shops should Amanda go to?
    """)
    def onList1(shop_name, shopsList):
        isValid = False
        while isValid == False:
            if shop_name in shopsList:
                shopsToVisit.append(shop_name)
                isValid = True
            else:
                shop_name = input("Choose a shop from the dang list. ")
    while len(shopsToVisit) < 3:
        if len(shopsToVisit) < 1:
            shop = input("Choose Amanda's first shop: ")
            onList1(shop, shops)
        else:
            shop = input("Choose another shop: ")
            onList1(shop, shops)
    print("Amanda decides to shop at %s, %s, and %s." %(shopsToVisit[0], shopsToVisit[1], shopsToVisit[2]))
    print("She bought 2 items at %s, 3 from %s, and 3 from %s." %(shopsToVisit[0], shopsToVisit[1], shopsToVisit[2]))

elif user_input == "skip":
    print("""
    Amanda skips breakfast entirely and heads out for an early start.
    She meets with her friends in Soho at 10:00 am.
    She will spend 30 minutes at each shop, so she can go to 5 shops in total before lunch.
    Out of Pacsun, American Eagle, Zara, Sephora, Mac, Aerie, Primark, Adidas, and Forever 21,
    what five shops should Amanda go to?""")
    def onList(shop_name, shopsList):
        isValid = False
        while isValid == False:
            if shop_name in shopsList:
                shopsToGo.append(shop_name)
                isValid = True
            else:
                shop_name = input("Choose a shop from the dang list. ")
    while len(shopsToGo) < 5:
        if len(shopsToGo) < 1:
            shop = input("Choose Amanda's first shop: ")
            onList(shop, shops)
        else:
            shop = input("Choose another shop: ")
            onList(shop, shops)
    print("Great! Amanda went to %s, %s, %s, %s, and %s." %(shopsToGo[0], shopsToGo[1], shopsToGo[2], shopsToGo[3], shopsToGo[4]))
    print("She bought two items from each shop and is very happy with her purchases.")

lunch = []
print("""   Now, it is 12:30 - Lunch Time!
Amanda and her friends are very indecisive, so what kind of food do you suggest they have for lunch:
burgers, sushi, pizza, chinese food, thai food, or seafood?""")
pick_lunch = input()

while pick_lunch != "burgers" and pick_lunch != "sushi" and pick_lunch != "pizza" and pick_lunch != "chinese food" and pick_lunch != "thai food" and pick_lunch != "seafood":
    pick_lunch = input("Choose one of the options! ")
if pick_lunch == "burgers":
        print(" You suggested burgers! Great choice! Amanda and her friends chose to eat at Shake Shack.")
if pick_lunch == "sushi":
        #while pick_lunch != "burgers" and pick_lunch != "sushi" and pick_lunch != "pizza" and pick_lunch != "chinese food" and pick_lunch != thai food and picklunch != "seafood":
        print(" Ooooh sushi! Yum! Amanda and her friends decided to eat at Soho Sushi.")
if pick_lunch == "pizza":
        print(" Good choice! Pizza is a classic! Amanda and her friends went to eat at Prince Street Pizza.")
if pick_lunch == "chinese food":
        print(" Yum! Chinese food is Amanda's favorite (not really)! Her and her friends ate at The Bao for the great Chinese food.")
if pick_lunch == "thai food":
        print(" Amanda loves thai food! Her and her friends went to eat at Soho Thai.")
if pick_lunch == "seafood":
        print(" Great suggestion! Amanda and her friends headed to Ed's Lobster Bar for amazing seafood.")

print("""   The time is almost 1:30 pm, and Amanda needs to get going for her hair appointment in Lower Manhattan.
She says goodbye to her friends and heads off.
When she gets to the salon, she realizes she didn't think everything through.
She wants to cut and dye her hair, but is unsure of the length and color.
Help Amanda decide her new hairstyle!""")

hair_length = input("""Should she just get a trim, a mid-length haircut, or a cut up to her shoulders?
 Type 'trim', 'mid-length', or 'shoulder-length'. """)

while hair_length != "trim" and hair_length != "mid-length" and hair_length != "shoulder-lenth":
     hair_length = input("Choose a hair length! ")
if hair_length == "trim":
     print("    Phew! Amanda doesn't want to let go of her hair just yet.")
if hair_length == "mid-length":
    print(" Good choice! Mid-length is just right.")
if hair_length == "shoulder-length":
    print(" Ahh, it's time for a big chop! Amanda thinks it's time for a change though!")

hair_color = input("Now it's time to choose a color! Should Amanda go for brown, auburn, rose gold, dark blue, or pastel purple? ")
hairColor = ["brown", "auburn", "rose gold", "dark blue", "pastel purple"]
while hair_color != "brown" and hair_color != "auburn" and hair_color != "rose gold" and hair_color != "dark blue" and hair_color != "pastel purple":
    hair_color = input("Choose a color! ")
if hair_color == "brown":
    print(" Playing it safe! Amanda doesn't want to get anything too crazy, so she'll go with a brown balayage this time.")
if hair_color == "auburn":
    print(" Good choice! Amanda decides to get an auburn hairstyle, and she's loving the result!")
if hair_color == "rose gold":
    print(" Rose gold ooh la la! Amanda is definitely satisfied with this choice!")
if hair_color == "dark blue":
    print(" Amanda has always wanted dark blue hair! Now is her chance, and she couldn't be happier with the finishing result!")
if hair_color == "pastel purple":
    print(" Amanda loves pastels! She decides to go for pastel purple hair, and she couldn't be happier with the result!")


if hair_color == "rose gold" or hair_color =="dark blue" or hair_color == "pastel purple":
    print("""   Since Amanda decided to go for a fancier color, her appointment took longer than expected and finished at 7!
Which means she's now running later for dinner with her sister!")
When she arrives, her sister is fuming because of her tardiness and refuses to pay for her dinner like she planned to.
Amanda had to pay for her own $100 meal, but it was worth it!
What an amazing day in the city! """)
else:
    print("""   Man, that hair appointment took a long time! Now it's nearly 6:00 pm.
Amanda has to head to dinner with her sister in Manhattan, and she just makes it on time.
Amanda's sister decides to pay for both their dinners because Amanda is such an amazing sibling!
Wow, what a great ending to a spectacular day in the city!""")



# def onList(shop_name, shopsList):
#     for shop in shopsList:
#         if shop == shop_name:
#             print("Amanda chooses to shop at " + shop_name)
#             shopsToVisit.append(shop_name)
#             print(shopsToVisit)
#         else:
#             print("Pick 3 shops for Amanda to go to.")
# shop2 = input("Choose Shop 2: ")
# def onList2(shop_name, shopsList):
#     for shop2 in shopsList:
#         if shop2 != shop_name:
#             print("Choose Shop 2: ")
# onList2(input(), shops))
#
# shop3 = input("Choose Shop 3: ")
# def onList3(shop_name, shopsList):
#     for shop3 in shopsList:
#         if shop2 in shopsList:
#             print("Choose Shop 3: ")
# onList3(input(), shops))
# shopsToVisit = [shop1, shop2, shop3]
