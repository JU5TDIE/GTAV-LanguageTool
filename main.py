import os

def changelanguage(path):
    print("(1) American")
    print("(2) French")
    print("(3) Italian")
    print("(4) German")
    print("(5) Spanish")
    print("(6) Japanese")
    print("(7) Russian")
    print("(8) Polish")
    print("(9) Portuguese")
    print("(10) Chinese")
    print("(11) Mexican")
    print("(12) Korean")
    language = input("Choose a language (Type the number) : ")

    if language == "1":
        contents = "-uilanguage american"
    elif language == "2":
        contents = "-uilanguage french"
    elif language == "3":
        contents = "-uilanguage italian"
    elif language == "4":
        contents = "-uilanguage german"
    elif language == "5":
        contents = "-uilanguage spanish"
    elif language == "6":
        contents = "-uilanguage japanese"
    elif language == "7":
        contents = "-uilanguage russian"
    elif language == "8":
        contents = "-uilanguage polish"
    elif language == "9":
        contents = "-uilanguage portuguese"
    elif language == "10":
        contents = "-uilanguage chinese"
    elif language == "11":
        contents = "-uilanguage mexican"
    elif language == "12":
        contents = "-uilanguage korean"
    else:
        print("Error, type the number again")

    f = open("%s/commandline.txt" % path, 'w+')
    f.write(contents)
    f.close()


if os.path.exists("history.txt"):
    with open('history.txt', 'r') as f:
        gtapath = f.read()
        changelanguage(gtapath)

else:
    while True:
        gtapath = input("Copy & Paste or Type GTA V folder path : ")

        try:
            file_list = os.listdir(gtapath)

            if "GTA5.exe" in file_list:
                changelanguage(gtapath)
                history = open("history.txt", 'w+')
                history.write(gtapath)
                history.close()
                break
        except:
            print("Type the GTA V folder path again")