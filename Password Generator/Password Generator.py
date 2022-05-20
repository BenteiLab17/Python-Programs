import random
import os


def password_generate(no_paswd, length):  # This function generates all the possible passwords based on length and no.
    string_of_symbols = "012345abcdefghi6789jklmnopqrxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$stuvw%^&*()_,+-/."
    final_list = []
    print("\n")
    for item in range(no_paswd):
        password = ""
        for char in range(length):
            password = password + random.choice(string_of_symbols)
        print(f'Pasword number {item+1} = {password}')
        final_list.insert(item, password)
    return final_list


def ask_password_details():     # This function prompts the user to enter the no. of passwords he wants and its length
    no_passwords = int(input("\n\nEnter how many passwords you want to generate: "))
    pass_length = int(input("Enter the length(size) of the password you want to be generated: "))
    list_of_pass = password_generate(no_passwords, pass_length)
    print(f'\n\nThe Lists of passwords generated are {list_of_pass}')


os.system('cls')
print("WELCOME TO THE PASSWORD GENERATOR PROGRAM")
ask_password_details()