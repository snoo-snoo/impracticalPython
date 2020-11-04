from chapterTwo.palingrams import find_palingrams

palingrams = find_palingrams('chapterTwo/2of4brif.txt')

palingrams_sorted = sorted(palingrams)
print("\nNumber of palingrams = {}\n".format(len(palingrams_sorted)))
for first, second in palingrams_sorted:
    print("{} {}".format(first, second))