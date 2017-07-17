start ="""
Today, Amanda is plannning to head out to the New York City for a fun-filled day! Her agenda for today is to first to meet her friends in Soho to shop and eat lunch.
Then she has a hair appointment at 1:30 pm and dinner in Manhattan with her sister at 6:00 pm. She begins her morning when she wakes up at 9:30 am.
Because it takes an hour to get to Soho from where she is in Brooklyn, should she spend time eating breakfast or skip breakfast to meet earlier
with her friends?"""

print(start)

user_input = ""

while user_input != "eat breakfast" and user_input != "skip breakfast":
    print("Type 'eat breakfast' to leave later or 'skip breakfast' to leave now.")
    user_input = input()

if user_input == "eat breakfast":
    print("""
Amanda decides to sit down and eat breakfast at home, so she ends up leaving at 10:00 am and gets to Soho at 11:00 am to meet her friends.
Now, they need to decide which stores to shop in.
Because they need an hour to eat lunch, and since Amanda has her hair appointment at 1:30 pm, they can only go to a few shops.
They will spend 30 minutes at each shop, so Amanda must pick 3 to go to.
Out of Pacsun, American Eagle, Zara, Sephora, Mac, Aerie, Primark, and Adidas, what three shops should Amanda go to?
    """)
    three_shops = input("Pick 3 shops for Amanda to go to. ")
elif user_input == "skip breakfast":
    print("""
    Amanda decides to skip breakfast entirely and head out to the city for an early start.
    She meets with her friends in Soho at 10:00 am. She and her friends will need an hour for lunch, and Amanda's hair appointment is at 1:30 pm.
    She will spend 30 minutes at each shop, so she can go to 5 shops in total. Which 5 shops should Amanda go to?""")
    five_shops = input("Pick 5 shops for Amanda to go to. ")

shops = ["Pacsun", "American Eagle", "Zara", "Sephora", "Mac", "Aerie", "Primark", "Adidas"]

# def onList(shop_name, shopsList):
#     for shop in shopsList:
#         if shop == shop_name:
#             print("Amanda chooses to shop at " + shop_name)
#             shopsToVisit.append(shop_name)
#             print(shopsToVisit)
#         else:
#             print("Pick 3 shops for Amanda to go to.")

shopsToVisit = []

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
if len(shopsToVisit) < 4:
    print("Amanda decides to shop at %s, %s, and %s." %(shopsToVisit[0], shopsToVisit[1], shopsToVisit[2]))


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
shopsToGo = []
def onList1(shop_name, shopsList):
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
        onList1(shop, shops)
    else:
        shop = input("Choose another shop: ")
        onList1(shop, shops)
if len(shopsToGo) < 6:
    print("Amanda bought 2 items at %s, 3 from %s, and 3 from %s." %(shopsToGo[0], shopsToGo[1], shopsToGo[2]), shopsToGo[3], shopToGo[4]))


print("Great! Amanda went to %s, %s, %s, %s, and %s." %(shopsToGo[0], shopsToGo[1], shopsToGo[2], shopsToGo[3], shopsToGo[4]))
