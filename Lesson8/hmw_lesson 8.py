# Write a function that can read contents of a file and can handle cases when provided file name does not exist:
# Handle Error cases gracefully displaying an informative message to the user.
# What Error type can we use here?  (check Python documentation)


try:
    with open("C:\\Users\\mayum\\PycharmProjects\\Homework\\my_first_git_homework_Mayumi.txt", "r") as txt_file:
        content = txt_file.readlines()
        raise Exception
        print(content)

except: FileNotFoundError #exception FileNotFoundError Raised when a file or directory is requested but doesn’t exist. Corresponds to errno ENOENT.
print("The file path is incorrect.")