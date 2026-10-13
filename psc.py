#passwordstrenghtchecker
import re

#fucction to check strenght of password

def password_strenght_checker(password):
    if len(password)<8:
        return "minimum pasword is 8 digit please enter a 8 digit of password."
    
    if not any (char .isupper()for char in password):
        return "weak password add upper case alphabate"
    
    if not any(char .islower()for char in password):
        return "weak password.please! add lower alphaate"
    
    if not any(char .isdigit()for char in password):
        return "weak password.please! add digit in your password"

    if not any(char .isalnum()for char in password):
        return "weak password palese! add some special chareacter "

    if not re.search("[!@#$%^&*(),??/]",password):

        return "stronge password:-"


def password_checker():


    #main function for password checker

    print("welcome to password checker:-")

    while True:
        password =input("\nenter your password(or type 'exit to quit):-")

        if password.lower()=="exit":
            print("thanks uou for using the password strenght checker.")
            break

        result = password_strenght_checker(password)
        print(result)


# runthe password checker tool

if __name__ == "__main__":
    password_checker()
