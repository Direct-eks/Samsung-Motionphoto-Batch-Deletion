from multiprocessing import Process
from CLI.process_thread import folder_process
import re

if __name__ == '__main__':

    print("Program started", end='\n')
    print("This program can take up to 6 paths, "
          "for all paths, please enter absolute path", end='\n')

    path_checker = re.compile("^[A-Z]:(/[^<>:/|?*\"]*)+$")

    path1 = ""
    path2 = ""
    path3 = ""
    path4 = ""
    path5 = ""
    path6 = ""

    path_to1 = ""
    path_to2 = ""
    path_to3 = ""
    path_to4 = ""
    path_to5 = ""
    path_to6 = ""

    while True:
        choice = input("Do you want to proceed with 6 paths? y/n"
                       "\nChoosing n, the program will proceed with 3 threads"
                       "but you can always skip any thread: ")
        if choice == "y" or choice == "n":
            break
        else:
            print("Please enter y/n to proceed")

    # -----------------1-----------------
    while True:
        path1 = input("\nPlease enter the 1st input path, "
                      "enter \"skip\" to skip or type quit to exit: ")

        if path1 == "skip":
            break
        elif path1 == "quit":
            exit(0)

        if path_checker.match(path1) is None:
            print("Invalid path! Please re-enter!")
        else:
            break

    if path1 != "skip":
        while True:
            path_to1 = input("Please enter the 1st output path, "
                          "or type quit to exit: ")

            if path_to1 == "quit":
                exit(0)

            if path_checker.match(path_to1) is None:
                print("Invalid path! Please re-enter!")
            else:
                break

    # -----------------2-----------------
    while True:
        path2 = input("\nPlease enter the 2nd input path, "
                      "enter \"skip\" to skip or type quit to exit: ")

        if path2 == "skip":
            break
        elif path2 == "quit":
            exit(0)

        if path_checker.match(path2) is None:
            print("Invalid path! Please re-enter!")
        else:
            break

    if path2 != "skip":
        while True:
            path_to2 = input("Please enter the 2nd output path, "
                             "or type quit to exit: ")

            if path_to2 == "quit":
                exit(0)

            if path_checker.match(path_to2) is None:
                print("Invalid path! Please re-enter!")
            else:
                break

    # -----------------3-----------------
    while True:
        path3 = input("\nPlease enter the 3rd input path, "
                      "enter \"skip\" to skip or type quit to exit: ")

        if path3 == "skip":
            break
        elif path3 == "quit":
            exit(0)

        if path_checker.match(path3) is None:
            print("Invalid path! Please re-enter!")
        else:
            break

    if path3 != "skip":
        while True:
            path_to3 = input("Please enter the 3rd output path, "
                             "or type quit to exit: ")

            if path_to3 == "quit":
                exit(0)

            if path_checker.match(path_to3) is None:
                print("Invalid path! Please re-enter!")
            else:
                break

    if choice == "y":
        # -----------------4-----------------
        while True:
            path4 = input("\nPlease enter the 4th input path, "
                          "enter \"skip\" to skip or type quit to exit: ")

            if path4 == "skip":
                break
            elif path4 == "quit":
                exit(0)

            if path_checker.match(path4) is None:
                print("Invalid path! Please re-enter!")
            else:
                break

        if path4 != "skip":
            while True:
                path_to4 = input("Please enter the 4th output path, "
                                 "or type quit to exit: ")

                if path_to4 == "quit":
                    exit(0)

                if path_checker.match(path_to4) is None:
                    print("Invalid path! Please re-enter!")
                else:
                    break

        # -----------------5-----------------
        while True:
            path5 = input("\nPlease enter the 5th input path, "
                          "enter \"skip\" to skip or type quit to exit: ")

            if path5 == "skip":
                break
            elif path5 == "quit":
                exit(0)

            if path_checker.match(path5) is None:
                print("Invalid path! Please re-enter!")
            else:
                break

        if path5 != "skip":
            while True:
                path_to5 = input("Please enter the 5th output path, "
                                 "or type quit to exit: ")

                if path_to5 == "quit":
                    exit(0)

                if path_checker.match(path_to5) is None:
                    print("Invalid path! Please re-enter!")
                else:
                    break

        # -----------------6-----------------
        while True:
            path6 = input("\nPlease enter the 6th input path, "
                          "enter \"skip\" to skip or type quit to exit: ")

            if path6 == "skip":
                break
            elif path6 == "quit":
                exit(0)

            if path_checker.match(path6) is None:
                print("Invalid path! Please re-enter!")
            else:
                break

        if path6 != "skip":
            while True:
                path_to6 = input("Please enter the 6th output path, "
                                 "or type quit to exit: ")

                if path_to6 == "quit":
                    exit(0)

                if path_checker.match(path_to6) is None:
                    print("Invalid path! Please re-enter!")
                else:
                    break

    t1 = Process(target=folder_process, args=(path1, 1, path_to1))
    t2 = Process(target=folder_process, args=(path2, 2, path_to2))
    t3 = Process(target=folder_process, args=(path3, 3, path_to3))
    t4 = Process(target=folder_process, args=(path4, 4, path_to4))
    t5 = Process(target=folder_process, args=(path5, 5, path_to5))
    t6 = Process(target=folder_process, args=(path6, 6, path_to6))

    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t5.start()
    t6.start()

    t1.join()
    t2.join()
    t3.join()
    t4.join()
    t5.join()
    t6.join()

    exit(0)

