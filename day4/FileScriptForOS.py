import os

file_name = input("File name: ")
directory = str(input("What is the directory you want to create the file in?: "))
os.chdir(f"C:/Users/ChiedozieChukwurah/PycharmProjects/pythonBasics/{directory}")
os.mkfifo(file_name)
