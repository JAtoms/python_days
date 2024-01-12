import shutil

path = "test.txt"

# File detection
# if os.path.exists(path):
#     print("The location exists")
# else:
#     print("The location dosen't exists")

# Read a file
# with open(path) as file:
#     print(file.read())

# Write a file
# with open(path, 'w') as file:
#     file.write("\nWhoops")
#
# with open(path) as file:
#     print(file.read())

# Append a file
# with open(path, 'a') as file:
#     file.write("\nWhoops")
#
# with open(path) as file:
#     print(file.read())

# Copying files
shutil.copy(path, "abuj.txt")
