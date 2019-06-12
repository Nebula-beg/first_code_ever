beg = input("Enter your name, let me know what to call you: ")
print()

def name(beg):
    if beg == "Satan":
        return "I don't like you! ... but I guess we can still talk."
    else:
        return "Your name is " + beg + "." + " That is a really cool name."

print(name(beg))

print()

print("I am Orb. I am just a small program.")
print()

age = input("Enter you age: ")
print("You are " + str(age) + " years old.")
print()
print("Wow, you are so old!")
print()

def future_years(age):
    future_years = 100 - int(age)
    if future_years < 100 and future_years >= 1:
        return "You will be 100 years old in " + str(future_years) + " years."
    else:
        return "You are too old and wise for me."

print(future_years(age))
print("You have been alive for such a long time!\nWhat do you want to do with the time you have left?")
print()
print("1) Dance")
print("2) Sing")
print("3) Read")
print("4) Sleep")
print("5) Nothing")
print()

question = str(input("Out of these options Orb asks you to pick one.\n Which is it?: "))

def hobby(question):
    if question == "Dance":
        return "Amazing!"
    elif question == "Sing":
        return "I love that!"
    elif question == "Read":
        return "I love reading too!"
    elif question == "Sleep":
        return "Oh, sleep is the best!"
    elif question == "Nothing":
        return "But there must be something you like!"
    else:
        return "That is not one of your choices!!"

print(hobby(question))
print("I like you, you know?\n    We will get along, I know it!\n     Orb has to go now but we'll talk soon!")



