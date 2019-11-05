"""Generate despot names randomly."""
import sys
import random


def main():
    """Use the user's name to generate a truly terrifying dictator name."""
    print("Despotifier V1.0. Trademark MELadbrook.\n\n")
    print("Welcome to Despotifier!TM.\n")
    user_name = input("What is your name?: \n\n")

    title = ('Emporer', 'King', 'Viceroy', 'Grand Duke', 'Archduke',
             'Prince', 'Duke', 'Earl', 'Count', 'Viscount', 'Baron')

    qual_num = (1, 2, 3)
    qual = ('PhD', 'MD', 'DPhil', 'JD', 'DO', 'Prof', 'DBA')

    abbr = ('VC', 'OBE', 'DSO', 'MC', 'CBE')

    suffix = (' The Big News', ' Grunts', ' Tinkie Winkie', ' DumDum',
              ' Beenie-Weenie', ' Stinkbug', ' Pottin Soil', ' The Squirts',
              ' Jazz Hands')

    while True:
        title_name = random.choice(title)
        last_name = random.choice(suffix)
        qual_name_list = random.choices(qual, k=random.choice(qual_num))
        qual_name = ''
        for i in qual_name_list:
            qual_name += i


        print("\n\n")
        print("{} {} {} {}".format(title_name, user_name, qual_name,
                                   last_name), file=sys.stderr)
        print("\n\n")

        try_again = input("\n\nAgain? (Press Enter else n to quit)\n ")
        if try_again.lower() == "n":
            break

        input("\nPress Enter to exit.")


if __name__ == "__main__":
    main()
