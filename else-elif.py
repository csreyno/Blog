#in class example

# age = input("How old are you?\n")

if int(age) == 21:
    print("You are a great age to party")
elif int(age) >= 21:
    print("You are old enough")
else:     #can also be 'elif' doesnt have to end in 'else'
    print("You are too young!")

#Exercise
rando_number = input("Gimme a random number!\n")

if int(rando_number) > 42:
    print("Number too high!")
elif int(rando_number) < 42:
    print("number too low!")
elif int(rando_number) == 42:
    print("number is correct")