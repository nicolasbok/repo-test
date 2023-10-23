# I created a file from zero

def string_checker(word):
    counter = 0
    for item in word:
        if item == "a":
            counter = counter + 1
    return counter

print(string_checker("halla"))