import os


folders = input("Enter a list of folder paths separated by spaces: ").split()



for folder in  folders:

    try:

        files = os.listdir(folder)

    except FileNotFoundError:

        print("please provide a valid folder name, looks like the folder does not exixt: " + folder)

    break




    print("=== listing file for the folder" + folder)
    print(files)

    for file in files:
        print(file)