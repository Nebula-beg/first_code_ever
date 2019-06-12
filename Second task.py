start = int(input("Give me a number: "))

def number(start):
    if start%4 == 0:
        return "That is a multiple of 4, right?"
    elif start%2 == 0:
        return "That is an even number."
    elif start%2 != 0:
        return "That is an odd number."


print(number(start))

num = int(input("Give me another number: "))
check = int(input("Give me a number to divide it by: "))

def result(num, check):
    if num%check == 0:
        return "Now this is what I call an even division!"
    else:
        return "This is not an even division."

print(result(num, check))