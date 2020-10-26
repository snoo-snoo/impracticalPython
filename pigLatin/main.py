""" Pig Latin Generator """

VOWELS = ('a', 'e', 'i', 'o', 'u')


def form_pig_latin():
    """Take a user input and form a pig latin word."""
    word = input("Please input a word: \n")

    if word.isalpha():
        if word.startswith(VOWELS):
            pig_latin = word + "way"
        else:
            pig_latin = word[1:len(word)] + word[0] + "ay"

        print("Your pig latin is: " + pig_latin)

    else:
        print("The given input looks like its not a word, please try again.")
        form_pig_latin()


if __name__ == '__main__':
    form_pig_latin()
