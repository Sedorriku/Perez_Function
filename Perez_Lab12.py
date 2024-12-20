#listahan ng mga pagkains
Bakasyonna = {
1: "Food",
2: "Drinks",
3: "Desserts"
}

Sarap = {
"Food": {
1: ("Chicken", 90),
2: ("Pizza", 180),
3: ("Burger", 60),
4: ("Spaghetti", 100),
5: ("Burger Steak", 80)
},
"Drinks": {
6: ("Coke", 50),
7: ("Ice Tea", 60),
8: ("Water", 25),
9: ("Pineapple", 70),
10: ("Coke_Float", 100),
},
"Desserts": {
11: ("Fries", 75),
12: ("Apple Pie", 55),
13: ("Peach Apple pie", 60),
14: ("Hotdog", 65),
15: ("ICe_Cream", 35),
},
}
#using functionnnnnn n displaying and choosing the categoriesszz
def display_categories():
    print("Choose a Category:")
    for toilet, skibidi in Bakasyonna.items():
        print(f"{toilet} {skibidi}")

def display_items(category):
    print(f"The Food Available in {category} are:")
    for testvar, (name, price) in Sarap[category].items():
        print(f"{testvar} {name} - ₱{price:.2f}")

print("Welcome to The Delicious Food Ordering System")

display_categories()

while True:
    try:
        sleepy = int(input("\nEnter the number of your chosen category: "))
        if sleepy in Bakasyonna:
            tamaba = Bakasyonna[sleepy]
            print(f"The Chosen Category is: {tamaba}")
            break
        else:
            print("Invalid choice. Please select a valid category that we showed")
    except ValueError:
        print("Invalid input. Please enter a number within 1, 2 or 3.")

display_items(tamaba)

while True:
    try:
        itemchoice = int(input("\nEnter the item number you want to order: "))
        if itemchoice in Sarap[tamaba]:
            productname, productprice = Sarap[tamaba][itemchoice]
            print(f"\nThe Product You Selected is: {productname} With The Price of ₱{productprice:.2f}")
            break
        else:
            print("Invalid choice. Please select a valid Food from the provided menu.")
    except ValueError:
        print("Invalid input. Please enter a number only.")

while True:
    try:
        money = float(input(f"The Total Food Payment is ₱{productprice:.2f}. Enter Your Payment Amount: ₱"))
        if money >= productprice:
            change = money - productprice
            print(f"Payment accepted. Your change is ₱{change:.2f}.")
            break
        else:
            print(f"Insufficient Payment Amount. You need at least ₱{productprice - money:.2f} More Pesos To Pay For The Food.")
    except ValueError:
        print("Invalid input. Please enter a valid amount of cash.")

print("\nThank You For Ordering Our Valued Customer")
