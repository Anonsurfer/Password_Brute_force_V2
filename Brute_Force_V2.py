# Simple script to bruteforce all alphabet passwords.
import random  # Random Module
list_of_words_number = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o",
                        "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z","1","2","3","4","5","6","7","8","9","0"]  # List of alphabets and numbers ( Feel free to add more) ;-)
password_to_bruteforce = input("Enter a password to bruteforce:" )
bruteforced_password = ""  # bruteforced password.
for y in range(0, len(password_to_bruteforce) ):  #Password_To_BruteForce
    for x in range(0, len(list_of_words_number) ):  #Bruteforcing the password !
        if (list_of_words_number[x] == password_to_bruteforce[y]):
            bruteforced_password = bruteforced_password + password_to_bruteforce[y]
            break
        else:
          print("Sorry, The Program Was Not Able To Brute-Force The Password You Entered ")
print("Bruteforced password: {}".format(bruteforced_password))
