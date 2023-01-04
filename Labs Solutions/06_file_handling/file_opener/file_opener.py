try:
    with open("text.txt", "r") as file:
        print('File found')
except FileNotFoundError:
    print("File not found")

# ---------------------------Second_way------------------------------------
# try:
#     file = open("text.txt", "r")
# except FileNotFoundError:
#     print("File not found")
# finally:
#     print("File found")