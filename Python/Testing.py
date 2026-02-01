# Network Chuck's Ep1 of Learning Python

#print("""This is a test
#I am Testing
#Wow, a lot of Testing""")

# Using Triple Quotes will Allow me to have the Print Function on Multiple Lines (See in Action on Code lines 1-3)
# If I type in \n that will put text on a new line (See in Action on Code lines 12&17)

# Anything Between Quotes is a String

# Network Chuck's Ep2 of Learning Python

# This is a little Food Server Bot Thing I Made // I was messing around with Inputs and Variables
  #print("Hello, Welcome to my Store!")

  #name = input("What is your name?\n")

  #print("Hello " + name + ", Thank you for coming into my Store! Here is a Menu")
  #Menu = ("Pizza , Waffles , Taco Salad ")
  #print(Menu)
  #Order = input("What would You Like to Order?\n")
  #print("Thank you for Ordering " + Order, name + ". It will be Ready Shortly!")

#Following Along with NetChuck's Ep 3 of Python // Messing around with Numbers Now

#The Number Alone is an Integer // If I put Quotes around it, the number becomes a String
#Name Name Variable = String // Age Variable = Integer // Acutal_Age Variable = Floating Point Number AKA Float (Float = Decimal Number)
# + = Add // - = Subtract // * = Multiply // / = Divide // ** = Exponent
  #age = 23
  #actual_age = 23.58
    #math = 23 * -9 / 2 + 43 * 3 
    #results = age + actual_age + math
    #print(results)
    
      #Upgrades to Our Food Server Bot
#Task 1 = Create a Variable Named Price and Assign it an Integer // Everything is Same Price @ $10
#Task 2 = Have the Food Server Ask how Many of What Item they want and Have him Remember how many You Ordered
#Task 3 = Have the Food Server Give you the Total Cost of the Things you Ordered

print("Hello! Welcome to the Resturant.")

name = input("What is your name?\n")
menu = ("Pizza, Bacon Burger, Salad, Steak, Waffle")
price = 12

print("Hello " + name + "! Here is a Menu for You. \n" + menu)
order = input("What would you like to order?\n")

quantity = input("How Many " + order + "s would you like?\n")

total = price * int(quantity)

print("Thank you for Ordering " + quantity, order + "!")
print("Your Total is $" + str(total) + ". We will have your " + quantity,  order + " Ready Shortly!")

#To turn an Integer into a String use the "str" Function (Refer Line 55)
#To turn a String into an Integer use the "int" Function (Refer Line 52)


