import csv
import os
import sys
from csv import writer
from prettytable import from_csv, PrettyTable


# classify rock samples based on users' input
# the rock samples will be identified by using the rock list as reference
def identifyRock():
    rocktype = input('Enter rock type: ')
    inputColor = input('Enter rock color(please separate with "/" if has multiple colors): ')
    texture = input('Enter rock texture: ')
    filename = './rock-list.csv'

    with open(filename, 'r') as csvfile:
        datareader = csv.reader(csvfile)
        f_count = 0
        table = PrettyTable()
        for row in datareader:
            inColor = inputColor.split('/')
            color = row[3].lower().split('/')
            if any(x in inColor for x in color):
                match = set(inColor) & set(color)
                count = len(match)
                if (texture.lower() in row[2].lower()) & (rocktype.lower() in row[0].lower()):
                    f_count += 1
                    result = list((row[1], match, count))
                    table.add_row(result)
            continue
        print('FOUND', f_count, 'MATCHES')
        table.field_names = ['ROCK NAME', 'COLORS MATCHED', 'COLORS MATCHED COUNT']
        print(table)


# creates the inventory
def createRockInventory():
    with open('./rock-inventory.csv', 'w') as file:
        csv_writer = writer(file, lineterminator='\n')
        header = ('NAME OF ROCK SAMPLE', 'LOCATION OF SAMPLE', 'NUMBER OF SAMPLES RETRIEVED')
        csv_writer.writerow(header)
        file.close()


# checks if the inventory is created, create if not
def isInventoryCreated():
    if os.path.isfile('./rock-inventory.csv'):
        return
    else:
        # calling the function to create the inventory
        createRockInventory()


# add rock samples in the inventory
def addRockSample():
    name = (input("name of rock sample:"))
    location = (input("Location of sample: "))
    count = int(input("Number of samples retrieved (enter integer only): "))
    with open('./rock-inventory.csv', 'a') as file:
        csv_writer = writer(file, lineterminator='\n')
        data = (name, location, count)
        csv_writer.writerow(data)
        file.close()
        print(name, "is added to your inventory")


# view rock samples in the inventory
def viewInventory():
    with open("./rock-inventory.csv", "r") as file:
        table = from_csv(file)
        file.close()
        print(table)


# search rock samples in the inventory by providing the name of the rock samples
def searchInventory():
    inp = input('Enter name of rock sample: ')
    csv_file = csv.reader(open('./rock-inventory.csv', "r"), delimiter=",")

    table = PrettyTable()
    search_count = 0
    for row in csv_file:
        if inp == row[0]:
            search_count += 1
            table.add_row(row)

    if search_count != 0:
        table.field_names = ['NAME OF ROCK SAMPLE', 'LOCATION OF SAMPLE', 'NUMBER OF SAMPLES RETRIEVED']
        print(table)
    else:
        print('NO RECORDS FOUND.')


def main():
    while True:
        isInventoryCreated()
        print("Hello Engineer! Welcome to the Rock Identifier and Inventory.")
        print("What do you want to do today? Your options include:")
        print("OPTIONS")

        print("Enter '1' to add items to your inventory.")
        print("Enter '2' to view inventory.")
        print("Enter '3' to search inventory.")
        print("Enter '4' to identify rock sample.")
        print("Enter '5' to exit inventory.")
        print()

        option = int(input("Option chosen: "))

        if option == 1:
            addRockSample()
        elif option == 2:
            viewInventory()
        elif option == 3:
            searchInventory()
        elif option == 4:
            identifyRock()
        elif option == 5:
            sys.exit(0)


if __name__ == '__main__':
    main()
