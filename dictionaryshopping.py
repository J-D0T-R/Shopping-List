###   Shopping List   ###
###   James Rutley   ###
###   Start date: 10/21/2021   ###
###   End date: 10/21/2021   ###

# Imports
# lets me round the floating point to give the final
# cost to 2 decimal places
import decimal

# Arrays
# the shopping list
shopping_list = []

# the price list
price_list = []

# Functions
def shopping():
    while True:
        item = input("Please enter an item to add to your shopping list:  ").lower()

        if item == "done":
            break

        else:
            shopping_list.append(item)
        
        try:
            item = float(input(("How much does it cost?  ")))
            price_list.append(item)
    
        except ValueError:
            print("Sorry, I don't know what you mean.")
            shopping_list.remove(item)
            continue
    
    #Combines the two lists into a dictionary
    shopping_dictionary = dict(zip(shopping_list,price_list))
    
    print()
    print("Don't Forget To Buy:")
    print()

    print(shopping_dictionary)

# making changes to their shopping list.
def editing():
    while True:
        edit = input("Enter the item you want to add or remove:  ").lower()
        if str(edit) in shopping_list:
            shopping_list.remove(edit)
            more_changes = input("Are you happy with your list?(y/n)  ")
            
            if "y" in str(more_changes):
                print()
                print("Here's your new list:")
                print()
                    
                print(shopping_dictionary)
                break
            
            else:
                continue

        
            try:
                edit_price = float(input("Enter its price:  "))
                
                if edit_price in price_list:
                    price_list.remove(edit_price)
                    shopping_dictionary = dict(zip(shopping_list,price_list))
                    
                    print()
                    print("Here's your new list:")
                    print()
                    
                    print(shopping_dictionary)
                    
                    more_changes = input("Are you happy with your list?(y/n)  ")
                    
                    if "y" in str(more_changes):
                        break
                    
                    else:
                        continue
                               
            except ValueError:
                print("That's not a number.")
                continue
            
        else:
            shopping_list.append(edit)
        
        try:
            item = float(input(("How much does it cost?"  )))
            price_list.append(item)
            more_changes = input("Are you happy with your list?(y/n)  ")
            
            if "y" in str(more_changes):
                print()
                print("Here's your new list:")
                print()
                    
                print(shopping_dictionary)
                break
        
            else:
                continue
    
        except ValueError:
            print("Sorry, I don't know what you mean.")
            shopping_list.remove(item)
            continue
            

# Main code #
print("""
This lovely program creates a shopping list for you!
Please enter the items you need to buy and how much they cost.
When entering price, don't bother with signs designating currency.
When you're finished, type "done" to end your list and see the result.
If you want to change something, say no to "Is this what you wanted?".
""")

shopping()
   
total = round((sum(price_list)), 2)

print()
print(f"Your total cost is ${total}.")
print()

edit = input("Is this what you wanted?"  ).lower()

if "y" in str(edit):
    print("Great, happy shopping!")
    
else:
    editing()