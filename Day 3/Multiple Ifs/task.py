print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0
photo_price = 3
if height >= 120 :
    print("You can ride the rollercoaster")
    age = int(input("What's your age in years?"))
    if age < 12:
        bill = 5
        print("Child ticket is $5")
    elif age <= 18:
        bill = 7
        print("youth ticket is $7")
    else:
        bill = 12
        print("Adult ticket is $12")
    wants_photo = input("do you want a photo? 'Yes or No' ")
    yes = bill + photo_price
    no = bill
    if wants_photo == "yes":
        print(f"your bill is {yes}")
    else:
        print(f"your bill is {bill}")


else:
    print("Sorry you have to grow taller before you can ride.")
