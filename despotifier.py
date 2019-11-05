"""Generate despot names randomly."""
import sys
import random


def create_segment(num, segment_list):
    """Randomly generate a section of the despoiler's name."""
    choices = segment_list
    segment = ''
    for m in range(random.choice(num)):
        random.shuffle(choices)
        segment += choices.pop() + ' '
    segment = segment[:-1]
    return segment


def main():
    """Use the user's name to generate a truly terrifying dictator name."""
    print("Despotifier V1.0. Trademark MELadbrook.\n\n")
    print("Welcome to Despotifier!TM.\n")
    user_name = input("What is your name?: \n\n")

    title = ('Emperor', 'King', 'Viceroy', 'Grand Duke', 'Archduke',
             'Prince', 'Duke', 'Earl', 'Count', 'Viscount', 'Baron')

    qual_num = (1, 2)
    qual = ['PhD', 'MD', 'DPhil', 'JD', 'DO', 'Prof', 'DBA']

    abbr_num = (1, 2)
    abbr = ['VC', 'OBE', 'DSO', 'MC', 'CBE']

    suffix_1 = ('Ruler of ', 'Master of ', 'Defeater of ', 'Destroyer of ',
                'Commander of ', 'Despoiler of ')

    suffix_2 = ('all the animals of the land', 'all the fishes of the sea',
                'all the peasants in the land', 'the sky, earth and sea')

    while True:
        title_name = random.choice(title)
        abbr_name = create_segment(abbr_num, abbr)
        suffix_name = random.choice(suffix_1) + random.choice(suffix_2)
        qual_name = create_segment(qual_num, qual)

        print("\n\n")
        print("{} {} {} {}, {}".format(title_name, user_name, qual_name,
                                      abbr_name, suffix_name), file=sys.stderr)
        print("\n\n")

        try_again = input("\n\nAgain? (Press Enter else n to quit)\n ")
        if try_again.lower() == "n":
            break

        input("\nPress Enter to exit.")


if __name__ == "__main__":
    main()
