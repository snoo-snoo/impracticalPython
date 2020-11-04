""" Find all word-pair palingrams in a dictionary file. """

from chapterTwo.load_dictionary import load

def find_palingrams(file):
    """ Find all word-pair palingrams in a dictionary file. """

    word_list = set(load(file))
    pali_list = []

    for word in word_list:
        end = len(word)
        rev_word = word[::-1]
        if end > 1:
            for i in range(end):
                if word[i:] == rev_word[:end - i] and rev_word[end - i:] in word_list:
                    pali_list.append((word, rev_word[end - i:]))
                if word[:i] == rev_word[end - i:] and rev_word[:end - i] in word_list:
                    pali_list.append((rev_word[:end - i], word))
    return pali_list
