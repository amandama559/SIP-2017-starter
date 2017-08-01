import csv
import string

# Open the CSV File and read it in.
f = open('countries.csv')
data = f.read()
countries = data.split('\n')
length = len(countries)

print("Enter one of the following countries:")
user_input = input()

while user_put in countries:
    if user_input > "Japan":
        del(countries[1:17])
        print(countries)
    elif user_input < "Japan":
        del(countries[16:32])
        print(countries)
    elif user_input == "Japan":
        print("Japan")



# average = sum(countries)/len(countries)
#
# while user_input in countries
#     if user_input > average;




# Split the data into an array of countries.




# print(countries[1])
# print(countries)
