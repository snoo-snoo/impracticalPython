""" Find palindromes (letter palingrams) in a dictionary file."""

from chapterTwo.load_dictionary import load


def find_palindromes(file):
    """Find palindromes in a dictionary file."""
    word_list = load(file)
    pali_list = []

    for word in word_list:
        if len(word) > 1 and word == word[::-1]:
            pali_list.append(word)

    print("\nNumber of palindromes found = {}\n".format(len(pali_list)))
    print(*pali_list, sep='\n')
