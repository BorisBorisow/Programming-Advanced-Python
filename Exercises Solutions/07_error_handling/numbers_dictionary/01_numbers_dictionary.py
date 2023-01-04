numbers_dictionary = {}

line = input()

while line != "Search":
    try:
        number_as_string = line
        number = int(input())
        numbers_dictionary[number_as_string] = number
    except ValueError:
        print("The variable number must be an integer") # Passing non-integer type to the variable number
    line = input()

line = input()
while line != "Remove":
    try:
        searched = line
        print(numbers_dictionary[searched])
    except KeyError:
        print("Number does not exist in dictionary") # Searching for a non-existent number
    line = input()

line = input()
while line != "End":
    try:
        searched = line
        del numbers_dictionary[searched]
    except KeyError:
        print(f"Number does not exist in dictionary") # Removing a non-existent number
    line = input()
print(numbers_dictionary)
