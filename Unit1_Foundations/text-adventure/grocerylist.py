import random

fruits = ["watermelon", "apples", "mangos"]

vegetables = ["broccoli", "pepper"]

groceryList = [fruits, vegetables, "milk", "cookies"]

print(groceryList[0])

print(random.choice(groceryList))

#defining a function
def onList(item_name, groceryList):
        for item in groceryList:
                if item == item_name:
                        print("%s is already on the list" %item_name)
                        return groceryList
                else:
                    groceryList.append(item_name)
                    print("Added %s to the list" %item_name)
                    return groceryList

print(onList("apples", groceries)) #calling the function

def findSum(num1, num2):
    return num1 + num2
print(10 - findSum(2.7))
